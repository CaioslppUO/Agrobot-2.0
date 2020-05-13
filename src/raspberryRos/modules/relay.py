#!/usr/bin/env python3

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

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#########################
#----> Classe Relay <----#
#########################

class Relay():
    #Envia o signal recebido para ligar ou desligar a placa A
    #Entrada: Sinal recebido(0 ou 1)
    #Retorno: Nenhum
    #Pré-condição: Nenhuma
    #Pós-condição: O sinal recebido é enviado para a placa A. Em caso de sinal inválido, o sinal 0 será enviado
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

    #Envia o signal recebido para ligar ou desligar a placa B
    #Entrada: Sinal recebido(0 ou 1)
    #Retorno: Nenhum
    #Pré-condição: Nenhuma
    #Pós-condição: O sinal recebido é enviado para a placa B. Em caso de sinal inválido, o sinal 0 será enviado
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

    #Envia o signal recebido para ligar ou desligar o pulverizador
    #Entrada: Sinal recebido(0 ou 1)
    #Retorno: Nenhum
    #Pré-condição: Nenhuma
    #Pós-condição: O sinal recebido é enviado para o pulverizador. Em caso de sinal inválido, o sinal 0 será enviado
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

    #Trata os dados recebidos pelo listenner
    #Entrada: Dados recebidos pelo listenner
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Caso a string recebida seja válida, o sinal recebido é enviado para o relé enviado pela mensagem
    def callback(self,data):
        cbAux = str(data.data).split(":")
        if(cbAux[0] == "sendSignalToPulverizer"):
            self.sendSignalToPulverizer(int(cbAux[1]))
        elif(cbAux[0] == "sendSignalToBoardTwo"):
            self.sendSignalToBoardTwo(int(cbAux[1]))
        elif(cbAux[0] == "sendSignalToBoardOne"):
            self.sendSignalToBoardOne(int(cbAux[1]))
    
    #Escuta o tópico do relé executa a rotina necessária para tratar os dados
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Ao escutar qualquer mensagem do tópico do relé, a envia para a rotina correta
    def listener(self):
        rospy.init_node('Relay', anonymous=True) 
        rospy.Subscriber("Relay", String, self.callback)   
        rospy.spin()

############################
#----> Loop principal <----#
############################

if __name__ == '__main__':
    relay = Relay()
    relay.listener()