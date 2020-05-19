#!/usr/bin/env python3

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

class ControlMode():
    def __init__(self):
        self.pubRelay = rospy.Publisher('Relay', String, queue_size=10)
        self.pubControlRobot = rospy.Publisher('ControlRobot', String, queue_size=10)
        self.pubCommandDecider = rospy.Publisher('CommandDecider', String, queue_size=10)

    #Envia os comandos para os nodes do ROS
    #Entrada: Velocidade,direção,limite,powerA,powerB e pulverizador
    #Retorno: Nenhum
    #Pré-condição: As variáveis devem estar corretas e dentro dos padrões para serem utilizadas
    #Pós-condição: Cada nó responsável por realizar o comando por trás das variáveis recebe as variáveis necessárias
    def sendComands(self,speed,steer,limit,powerA,powerB,pulverizer):
        self.pubControlRobot.publish(str(speed) + "$" + str(steer) + "$" + str(limit))
        self.pubRelay.publish("sendSignalToBoardOne:" + str(powerA))
        self.pubRelay.publish("sendSignalToBoardTwo:" + str(powerB))
        self.pubRelay.publish("sendSignalToPulverizer:" + str(pulverizer))

    #Trata os dados recebidos pelo listenner
    #Entrada: Dados recebidos pelo listenner
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Caso a conexão com a camada de comunicação esteja ativa, destina as variáveis para a função correta
    def callbackComunication(self,data):
        if(str(data.data) != "No connection established."):
            cbAux = str(data.data).split("$")
            self.sendComands(int(cbAux[0]), int(cbAux[1]), int(cbAux[2]), int(cbAux[3]), int(cbAux[4]), int(cbAux[5]))
            self.pubCommandDecider.publish("manual")
    
    #Escuta a camada de comunicação e executa a rotina necessária para tratar os dados
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Ao escutar qualquer mensagem da camada de comunicação, a envia para a rotina correta
    def listenComunication(self):
        rospy.Subscriber("CommandPriorityDecider", String, self.callbackComunication)   
        rospy.spin()

############################
#----> Loop Principal <----#
############################

if __name__ == '__main__':
    control = ControlMode()
    control.listenComunication()