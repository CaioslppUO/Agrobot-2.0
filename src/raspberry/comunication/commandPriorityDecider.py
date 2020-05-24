#!/usr/bin/env python3

"""
Módulo que gerencia qual comando terá prioridade de execução e o envia para o ROS.
"""

#####################
#----> Imports <----#
#####################

import rospy
from std_msgs.msg import String
from commandStandardizer import CommandStandardizer

################################
#----> Definições Globais <----#
################################

pubLog = rospy.Publisher('Log', String, queue_size=10)
rospy.init_node('CommandPriorityDecider', anonymous=True)

#################################
#----> Classe priorities <----#
#################################

## Classe que contém as prioridades de cada emissor de comandos
class priorities():
    def __init__(self):
        self.manual_pc = 1001
        self.manual_app = 1000
        self.rasp_lidar = 999
        self.computacional_vision = 998
        ## Quantidade de comandos garantidos quando um novo nível de prioridade é requerido.
        self.guaranteedCommands = 50 #Quantidade de comandos que precisam ser executados antes da prioridade ser liberada

#################################
#----> Classe Comunication <----#
#################################

## Classe que gerencia a comunicação de todos os emissores de comando com o sistema ROS.
class Comunication():
    def __init__(self):
        ## Comando recebida pelo emissor.
        self.msg        = None
        ## Símbolo utilizado para separar os dados recebidos no comando.
        self.separator  = "*"
        ## Instância da classe utilizada para padronizar os coamdnos recebidos.
        self.commandStandardizer = CommandStandardizer()
        ## Classe que contém os níveis de prioridade de cada emissor.
        self.priorities = priorities()
        ## Variável utilizada para gerenciar qual é a prioridade do comando atualmente sendo enviado.
        self.priority = 0
        ## Variável utilizada para saber quantos comandos com maior prioridade ainda restam. 
        self.leftCommands = 0

        #ROS
        self.pubComunication = rospy.Publisher('CommandPriorityDecider', String, queue_size=10)

    ## Método que publica o comando para o tópico do ROS.
    def execute(self):
        self.pubComunication.publish(self.commandStandardizer.webServerMsgHandler(self.msg))
        self.msg = None

    ## Método que escuta o tópico WebServerManual e executa a rotina necessária para tratar os dados.
    def listenWebServerManual(self):
        rospy.Subscriber("WebServerManual", String, self.callback,self.priorities.manual_app) 

    ## Método que escuta o tópico ComputationalVision e executa a rotina necessária para tratar os dados.
    def listenComputationalVision(self):
        rospy.Subscriber("ComputationalVision",String,self.callback,self.priorities.computacional_vision)

    ## Método que escuta o tópico ControlOutdoors e executa a rotina necessária para tratar os dados.
    def listenOutdoorControls(self):
        rospy.Subscriber("ControlOutdoors",String,self.callback,self.priorities.rasp_lidar)

    ## Método que escuta o tópico PcManual e executa a rotina necessária para tratar os dados.
    def listenPcManual(self):
        rospy.Subscriber("PcManual",String,self.callback,self.priorities.manual_pc)
   
    ## Método que escuta o tópico ControlLidar e executa a rotina necessária para tratar os dados.
    def listenControlLidar(self):
        rospy.Subscriber("ControlLidar", String, self.callback, self.priorities.rasp_lidar)

    ## Método que define qual comando será executado baseado na prioridade.
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

    ## Método que executa as rotinas de listen e envio dos comandos ao programa.
    def listenCommands(self):
        self.msg = None
        self.listenWebServerManual()
        self.listenOutdoorControls()
        self.listenComputationalVision()
        self.listenPcManual()
        self.listenControlLidar()
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

try:
    comunication = Comunication()
    pubLog.publish('startedFile$CommandPriorityDecider')
    comunication.listenCommands()
except:
    pass
