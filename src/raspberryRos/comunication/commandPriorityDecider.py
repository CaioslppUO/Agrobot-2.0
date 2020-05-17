#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import sys
from std_msgs.msg import String
from commandStandardizer import CommandStandardizer

################################
#----> Definições Globais <----#
################################

rospy.init_node('CommandPriorityDecider', anonymous=True)

###############################
#----> Variáveis Globais <----#
###############################

webServersReaded = 0
commandObservers = int(sys.argv[1])

class priorities():
    def __init__(self):
        self.manual_pc = 1001
        self.manual_app = 1000
        self.rasp_lidar = 999
        self.computacional_vision = 998
        self.guaranteedCommands = 50 #Quantidade de comandos que precisam ser executados antes da prioridade ser liberada

#################################
#----> Classe Comunication <----#
#################################

class Comunication():
    def __init__(self):
        self.msg        = None
        self.separator  = "*" #Símbolo utilizado para separa a mensagem padrão
        self.commandStandardizer = CommandStandardizer()
        self.priorities = priorities()
        self.priority = 0
        self.leftCommands = 0

        #ROS
        self.pubComunication = rospy.Publisher('CommandPriorityDecider', String, queue_size=10)

    #Publica o comando para o tópico do ROS
    def execute(self):
        self.pubComunication.publish(self.commandStandardizer.webServerMsgHandler(self.msg))
        self.msg = None

    #Escuta o tópico WebServerManual e executa a rotina necessária para tratar os dados
    def listenWebServerManual(self):
        rospy.Subscriber("WebServerManual", String, self.callback,self.priorities.manual_app) 

    #Escuta o tópico ComputationalVision e executa a rotina necessária para tratar os dados
    def listenComputationalVision(self):
        rospy.Subscriber("ComputationalVision",String,self.callback,self.priorities.computacional_vision)

    #Escuta o tópico ControlOutdoors e executa a rotina necessária para tratar os dados
    def listenOutdoorControls(self):
        rospy.Subscriber("ControlOutdoors",String,self.callback,self.priorities.rasp_lidar)

    #Escuta o tópico PcManual
    def listenOutdoorControls(self):
        rospy.Subscriber("PcManual",String,self.callback,self.priorities.manual_pc)

    #Define qual comando será executado
    def callback(self,data,priority):
        msg = str(data.data).split(self.separator)
        if(priority >= self.priority):
            self.priority = priority
            self.leftCommands = self.priorities.guaranteedCommands
            self.msg = msg
            self.execute()
        elif(self.leftCommands == 0):
            self.priority = priority
            self.leftCommands = self.priorities.guaranteedCommands
            self.msg = msg
            self.execute()
        else:
            self.leftCommands = self.leftCommands - 1

    #Executa as rotinas de listen e envio dos comandos ao programa
    def listenCommands(self):
        self.msg = None
        self.listenWebServerManual()
        self.listenOutdoorControls()
        self.listenComputationalVision()
        self.listenOutdoorControls()
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

try:
    comunication = Comunication()
    comunication.listenCommands()
except:
    pass