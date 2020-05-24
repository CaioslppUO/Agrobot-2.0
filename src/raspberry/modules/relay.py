#!/usr/bin/env python3

"""
Módulo que gerencia o envio dos comandos para os relés.
"""

#####################
#----> Imports <----#
#####################

import time
import rospy
import RPi.GPIO as GPIO

from std_msgs.msg import String

################################
#----> Definições Globais <----#
################################

pubLog = rospy.Publisher('Log', String, queue_size=10)

## Definição do modo do GPIO
GPIO.setmode(GPIO.BOARD)
## Desabilitando os warnings do GPIO
GPIO.setwarnings(False)

#########################
#----> Classe Relay <----#
#########################

## Classe que gerencia os relés.
class Relay():
    ## Método que envia um sinal para o relé da placa A do hover board.
    def sendSignalToBoardOne(self,signal):
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
    def sendSignalToBoardTwo(self,signal):
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
    def sendSignalToPulverizer(self,signal):
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
    def callback(self,data):
        cbAux = str(data.data).split(":")
        if(cbAux[0] == "sendSignalToPulverizer"):
            self.sendSignalToPulverizer(int(cbAux[1]))
        elif(cbAux[0] == "sendSignalToBoardTwo"):
            self.sendSignalToBoardTwo(int(cbAux[1]))
        elif(cbAux[0] == "sendSignalToBoardOne"):
            self.sendSignalToBoardOne(int(cbAux[1]))
    
    ## Método que escuta do tópico Relay e processa os comandos recebidos.
    def listener(self):
        rospy.init_node('Relay', anonymous=True) 
        rospy.Subscriber("Relay", String, self.callback)   
        rospy.spin()

############################
#----> Loop principal <----#
############################

if __name__ == '__main__':
    relay = Relay()
    pubLog.publish('startedFile$Relay')
    relay.listener()