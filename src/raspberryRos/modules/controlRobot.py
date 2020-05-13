#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import time
import serial
import sys
import rospy

from std_msgs.msg import String

################################
#----> Definições Globais <----#
################################

rospy.init_node('ControlRobot', anonymous=True) 

###############################
#----> Variáveis Globais <----#
###############################

uart0 = None
uart1 = None

#####################
#----> Funções <----#
#####################

#Define a quantidade de canais de comunicação UART que serão usadas e reserva as portas USB necessárias
#Entrada: Quantidade de canais de comunicação UART
#Retorno: Nenhum
#Pré-condição: Nenhuma
#Pós-condição: As portas USB em que a comunicação UART acontecerá são definidas
def setUart(uartAmount):
    global uart0,uart1
    if(uartAmount == 1):
        try:
            uart0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            try:
                uart0 = serial.Serial(
                    port='/dev/ttyUSB_CONVERSOR-1',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                )
            except:
                print('Error trying to set 1 Uart')
    elif(uartAmount == 2):
        try:
            uart0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

            uart1 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-1',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            print('Error trying to set 2 Uarts')
            pass

#Checa se a velocidade está correta e a corrige caso seja necessário
#Entrada: Velocidade
#Retorno: Velocidade recebida caso esteja correta ou a velocidade corrigida
#Pré-condição: Nenhuma
#Pós-condição: Caso a velocidade esteja errada, ela é corrigida
def checkSpeed(speed):
    if(speed < -100):
        return -100
    if(speed > 100):
        return 100
    return speed

#Checa se a direção está correta e a corrige caso seja necessário
#Entrada: Direção
#Retorno: Direção recebida caso esteja correta ou a direção corrigida
#Pré-condição: Nenhuma
#Pós-condição: Caso a direção esteja errada, ela é corrigida
def checkSteer(steer):
    if(steer < -100):
        return -100
    if(steer > 100):
        return 100
    return steer

#Checa se o limite está correta e a corrige caso seja necessário
#Entrada: Limite
#Retorno: Limite recebida caso esteja correta ou o limite corrigida
#Pré-condição: Nenhuma
#Pós-condição: Caso o limite esteja errada, ela é corrigida
def checkLimit(limit):
    if(limit < 0):
        return 0
    if(limit > 100):
        return 100
    return limit

##################################
#----> Classe Control Robot <----#
##################################

class ControlRobot():
    def __init__(self):
        self.speed = "0000"
        self.steer = "0000"
        self.limit = "0000"
        self.pub = rospy.Publisher('LOGRODANDO', String, queue_size=10)

        try:
            self.uartAmount = sys.argv[1]
        except:
            self.uartAmount = 0
        try:
            setUart(int(self.uartAmount))
        except:
            pass

    #Recebe um valor numérico e o transforma para string no formato: sinal (valor com três digitos)
    #Entrada: Valor para ser transformado
    #Retorno: Valor transformado
    #Pré-condição: O valor recebido deve ser um valor numérico entre -100 e 100
    #Pós-condição: O valor numérico é transformado para strig no formato do protocolo acima definido
    def getValue(self, v):
        if(v >= 0):
            r = '1'
        else:
            r = '0'
        if(v < 10 and v > -10):
            r += '00'
        elif(v < 100 and v > -100):
            r += '0'
        r += str(abs(v))
        return r

    #Define os valores das variáveis necessárias para controlar o robô
    #Entrada: Velocidade, direção e limite
    #Retorno: Nenhum
    #Pré-condição: Nenhuma
    #Pós-condição: As variáveis necessárias para controlar o robô são definidas
    def setValues(self,speed,steer,limit):
        spdCk = checkSpeed(speed)
        strCk = checkSteer(steer)
        lmtCk = checkLimit(limit)

        self.speed = self.getValue(spdCk)
        self.steer = self.getValue(strCk)
        self.limit = self.getValue(lmtCk)

    #Envia para o arduino os valores necessários para controlar o robô
    #Entrada: Dados recebidos pelo listenner
    #Retorno: Nenhum
    #Pré-condição: As variáveis devem estar corretas para serem executadas
    #Pós-condição: O comando recebido é executado
    def callbackSetValues(self,data):
        global uart0,uart1
        cbAux = str(data.data).split("$")

        try:
            self.setValues(int(cbAux[0]),int(cbAux[1]),int(cbAux[2]))
        except:
            self.speed = 0
            self.steer = 0
            self.limit = 0

        text = self.speed
        text += ','
        text += self.steer
        text += ','
        text += self.limit
        text += ';'

        try:
            if(int(self.uartAmount) == 1):  
                uart0.write(str.encode(text))
                self.pub.publish("Command send to arduino: " + str(text) + " Using " + str(self.uartAmount) + " Uarts")
            elif(int(self.uartAmount) == 2):
                uart0.write(str.encode(text))
                uart1.write(str.encode(text))
            else:
                self.pub.publish("Command send to arduino: None, Using " + str(self.uartAmount) + " Uarts")
            time.sleep(0.02)
        except:
            self.pub.publish("Uart Error")
        
    #Escuta o tópico controlRobot e executa a rotina necessária para tratar os dados
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Ao escutar qualquer mensagem do tópico controlRobot, a envia para a rotina correta
    def listenValues(self):
        rospy.Subscriber("ControlRobot", String, self.callbackSetValues)  

#######################
#----> Main Loop <----#
#######################

if __name__ == '__main__':
    control = ControlRobot()
    control.listenValues()
    rospy.spin()