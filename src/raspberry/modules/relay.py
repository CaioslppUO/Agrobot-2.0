#!/usr/bin/env python3

"""
Módulo que gerencia o envio dos comandos para os relés.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó relay.
rospy.init_node("relay", anonymous=True)

# -------------------------- #
# -> Imports Condicionais <- #
# -------------------------- #

try: 
    import RPi.GPIO as GPIO
except:
    const_pub_log.publish("error$Warning$Could not include RPi.GPIO as GPIO in raspberry/modules/relay.py")

try:
    ## Definição do modo do GPIO.
    GPIO.setmode(GPIO.BOARD)
    ## Desabilitando os warnings do GPIO.
    GPIO.setwarnings(False)
except:
    const_pub_log.publish('error$Warning$Could not set up GPIO configs in raspberry/modules/relay.py')

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerencia os relés.
class Relay():
    ## Método que envia um sinal para o relé da placa A do hover board.
    def send_signal_to_board_one(self,signal):
        if(signal == 1):
            GPIO.setup(38, GPIO.OUT)
            GPIO.output(38, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(38, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(38, GPIO.OUT)
            GPIO.output(38, GPIO.LOW)

    ## Método que envia um sinal para o relé da placa B do hover board.
    def send_signal_to_board_two(self,signal):
        if(signal == 1):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(40, GPIO.OUT)
            GPIO.output(40, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(40, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(40, GPIO.OUT)
            GPIO.output(40, GPIO.LOW)

    ## Método que envia um sinal para o relé do pulverizador/uv.
    def send_signal_to_pulverizer(self,signal):
        if(signal == 1):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(35, GPIO.OUT)
            GPIO.output(35, GPIO.HIGH)
            time.sleep(0.2)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(35, GPIO.OUT)
            GPIO.output(35, GPIO.LOW)

    ## Método que trata os comandos recebidos pelo listener.
    def callback(self,msg):
        info = str(msg.data).split("$")
        if(info[0] == "sendSignalToPulverizer"):
            try:
                self.send_signal_to_pulverizer(int(info[1]))
            except:
                const_pub_log.publish('error$Warning$Could not send signal to pulverizer in raspberry/modules/relay.py')
        elif(info[0] == "sendSignalToBoardTwo"):
            try:
                self.send_signal_to_board_two(int(info[1]))
            except:
                const_pub_log.publish('error$Warning$Could not send signal to board two in raspberry/modules/relay.py')
        elif(info[0] == "sendSignalToBoardOne"):
            try:
                self.send_signal_to_board_one(int(info[1]))
            except:
                const_pub_log.publish('error$Warning$Could not send signal to board one in raspberry/modules/relay.py')
    
    ## Método que escuta do tópico relay e processa os comandos recebidos.
    def listener(self):
        rospy.Subscriber("relay", String, self.callback)   
        rospy.spin()

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == '__main__':
    try: 
        relay = Relay()
        const_pub_log.publish('startedFile$relay.py')
        relay.listener()
    except:
        const_pub_log.publish("error$Fatal$Could not run relay.py.")
