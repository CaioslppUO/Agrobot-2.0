#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com os arduinos, enviando os comandos que serão enviados para o hover board.
"""

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

pubLog = rospy.Publisher('Log', String, queue_size=10)
rospy.init_node('ControlRobot', anonymous=True) 

###############################
#----> Variáveis Globais <----#
###############################

## Variável utilizada para acessar o conversor TTL 0
uart0 = None
## Variável utilizada para acessar o conversor TTL 1
uart1 = None

#####################
#----> Funções <----#
#####################

## Função que define e instancia a comunicação com os conversores TTL baseado na variável uartAmount.
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

##################################
#----> Classe Control Robot <----#
##################################

## Classe que gerência a comunicação com os arduinos.
class ControlRobot():
    def __init__(self):
        ## Variável utilizada para enviar a velocidade. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.speed = "0000"
        ## Variável utilizada para enviar a direção. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.steer = "0000"
        ## Variável utilizada para enviar o limite. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
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

    ## Método que transforma um valor inteiro para o padrão utilizado para enviar comandos ao arduino.
    # Padrão: SINAL_NÙMERO: o Sinal ocupa 1 posição, o número ocupa 3 posições.
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

    ## Método que seta os valores das variáveis recebidas.
    def setValues(self,speed,steer,limit):
        self.speed = self.getValue(speed)
        self.steer = self.getValue(steer)
        self.limit = self.getValue(limit)

    ## Método que responde ao recebimento de comandos que serão enviados aos arduinos.
    # Envia os comandos para os arduinos. \n
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

    ## Método que escuta do tópico ControlRobot para tratar os comandos recebidos.
    def listenValues(self):
        rospy.Subscriber("ControlRobot", String, self.callbackSetValues)  

#######################
#----> Main Loop <----#
#######################

if __name__ == '__main__':
    control = ControlRobot()
    pubLog.publish('startedFile$ControlRobot')
    control.listenValues()
    rospy.spin()