#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com os arduinos, enviando os comandos que serão enviados para o hover board.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,serial,sys,rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_log = rospy.Publisher('log', String, queue_size=10)
## Constante utilizada para acessar o conversor TTL 0
const_uart_0 = None
## Constante utilizada para acessar o conversor TTL 1
const_uart_1 = None

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('control_robot', anonymous=True) 

# ------------- #
# -> Funções <- #
# ------------- #

## Função que define e instancia a comunicação com os conversores TTL baseado na variável uart_amount.
def set_uart(uart_amount):
    global const_uart_0,const_uart_1
    if(uart_amount == 1):
        try:
            const_uart_0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            try:
                const_uart_0 = serial.Serial(
                    port='/dev/ttyUSB_CONVERSOR-1',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                )
            except:
                const_pub_log.publish("error$Warning$Error trying to set 1 Uart.")
    elif(uart_amount == 2):
        try:
            const_uart_0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

            const_uart_1 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-1',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            const_pub_log.publish("error$Warning$Error trying to set 2 Uarts.")

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência a comunicação com os arduinos.
class Control_robot():
    def __init__(self):
        ## Variável utilizada para enviar a velocidade. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.speed = "0000"
        ## Variável utilizada para enviar a direção. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.steer = "0000"
        ## Variável utilizada para enviar o limite. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.limit = "0000"

        try:
            self.uart_amount = sys.argv[1]
        except:
            self.uart_amount = 0
        try:
            set_uart(int(self.uart_amount))
        except:
            const_pub_log.publish("error$Warning$Could not set UART(s).")

    ## Método que transforma um valor inteiro para o padrão utilizado para enviar comandos ao arduino.
    # Padrão: SINAL_NÙMERO: o Sinal ocupa 1 posição, o número ocupa 3 posições.
    def get_stand_value(self, v):
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
    def set_values(self,speed,steer,limit):
        self.speed = self.get_stand_value(speed)
        self.steer = self.get_stand_value(steer)
        self.limit = self.get_stand_value(limit)

    ## Método que responde ao recebimento de comandos que serão enviados aos arduinos.
    # Envia os comandos para os arduinos. \n
    def callback_set_values(self,msg):
        info = str(msg.data).split("$")
        try:
            self.set_values(int(info[0]),int(info[1]),int(info[2]))
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
            if(int(self.uart_amount) == 1):  
                const_uart_0.write(str.encode(text))
            elif(int(self.uart_amount) == 2):
                const_uart_0.write(str.encode(text))
                const_uart_1.write(str.encode(text))
            else:
                time.sleep(0.02)
        except:
            const_pub_log.publish("error$Fatal$UART error.")

    ## Método que escuta do tópico Control_robot para tratar os comandos recebidos.
    def listen_values(self):
        rospy.Subscriber("control_robot", String, self.callback_set_values)  

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == '__main__':
    try: 
        control = Control_robot()
        const_pub_log.publish('startedFile$control_robot.py')
        control.listen_values()
        rospy.spin()
    except:
        const_pub_log.publish("error$Fatal$Could not run control_robot.py.")