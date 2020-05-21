#!/usr/bin/env python3

"""
Módulo que gerencia a montageme e distribuição dos comandos para os devidos dispositivos(hardware).
"""

#####################
#----> Imports <----#
#####################

import rospy
from std_msgs.msg import String

################################
#----> Definições Globais <----#
################################

rospy.init_node('CommandDecider', anonymous=True) 

#################################
#----> Classe Control Mode <----#
#################################

## Classe que gerência o recebimento dos comandos, separação e envio para os devidos dispositivos.
class ControlMode():
    ## Método que inicializa os tópicos em que serão publicados comandos
    def __init__(self):
        self.pubRelay = rospy.Publisher('Relay', String, queue_size=10)
        self.pubControlRobot = rospy.Publisher('ControlRobot', String, queue_size=10)
        self.pubCommandDecider = rospy.Publisher('CommandDecider', String, queue_size=10)

    ## Método que envia os valores corretos para cada dispositivo.
    def sendComands(self,speed,steer,limit,powerA,powerB,pulverizer):
        self.pubControlRobot.publish(str(speed) + "$" + str(steer) + "$" + str(limit))
        self.pubRelay.publish("sendSignalToBoardOne:" + str(powerA))
        self.pubRelay.publish("sendSignalToBoardTwo:" + str(powerB))
        self.pubRelay.publish("sendSignalToPulverizer:" + str(pulverizer))

    ## Método que trata os comandos recebidos.
    def callbackComunication(self,data):
        if(str(data.data) != "No connection established."):
            cbAux = str(data.data).split("$")
            self.sendComands(int(cbAux[0]), int(cbAux[1]), int(cbAux[2]), int(cbAux[3]), int(cbAux[4]), int(cbAux[5]))
            self.pubCommandDecider.publish("manual")
    
    ## Método que escuta o tópico CommandPriorityDecider e chama a função que trata os comandos.
    def listenComunication(self):
        rospy.Subscriber("CommandPriorityDecider", String, self.callbackComunication)   
        rospy.spin()

############################
#----> Loop Principal <----#
############################

if __name__ == '__main__':
    control = ControlMode()
    control.listenComunication()