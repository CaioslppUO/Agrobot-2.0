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

#################################
#----> Classe Comunication <----#
#################################

class Comunication():
    def __init__(self):
        self.msg        = None
        self.priority   = None
        self.separator  = "*" #Símbolo utilizado para separa a mensagem padrão
        self.commandStandardizer = CommandStandardizer()

        #ROS
        self.pubComunication = rospy.Publisher('CommandPriorityDecider', String, queue_size=10)

    #Publica o comando para o tópico do ROS
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pré-condição: O tópico em que será publicada a mensagem deve estar definido. A mensagem deve estar definida
    #Pós-condição: A mensagem que teve a maior prioridade de execução é executada
    def execute(self):
        global webServersReaded,commandObservers
        if(webServersReaded == commandObservers):
            self.pubComunication.publish(self.commandStandardizer.webServerMsgHandler(self.msg))
            self.msg = None
            self.priority = None
            webServersReaded = 0
        else:
            self.pubComunication.publish("No connection established.")

    #Trata os dados recebidos pelo listenner
    #Entrada: Dados recebidos pelo listenner
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: A mensagem recebida é guardada para execução e posteriormente executada caso tenha a maior prioridade
    def callbackWebServerManual(self,data):
        global webServersReaded
        msg = str(data.data).split(self.separator)
        if(self.priority == None or int(msg[0]) < self.priority):
            self.priority = int(msg[0])
            self.msg = msg

        webServersReaded = webServersReaded + 1
        self.execute()

    #Trata os dados recebidos pelo listenner
    #Entrada: Dados recebidos pelo listenner
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: A mensagem recebida é guardada para execução e posteriormente executada caso tenha a maior prioridade
    def callbackComputationalVision(self,data):
        global webServersReaded
        msg = str(data.data).split(self.separator)
        if(self.priority == None or int(msg[0]) < self.priority):
            self.priority = int(msg[0])
            self.msg = msg

        webServersReaded = webServersReaded + 1
        self.execute()

    #Escuta o tópico WebServerManual e executa a rotina necessária para tratar os dados
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Ao escutar qualquer mensagem do tópico WebServerManual, a envia para a rotina correta
    def listenWebServerManual(self):
        rospy.Subscriber("WebServerManual", String, self.callbackWebServerManual) 

    #Escuta o tópico ComputationalVision e executa a rotina necessária para tratar os dados
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pŕe-condição: Nenhuma
    #Pós-condição: Ao escutar qualquer mensagem do tópico ComputationalVision, a envia para a rotina correta 
    def listenComputationalVision(self):
        rospy.Subscriber("ComputationalVision",String,self.callbackComputationalVision)

    #Executa as rotinas de listen e envio dos comandos ao programa
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pré-condição: Nenhuma
    #Pós-condição: Os comandos recebidos são processados e enviados ao programa
    def sendCommands(self):
        self.msg = None
        self.listenWebServerManual()
        self.listenComputationalVision()
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

try:
    comunication = Comunication()
    comunication.sendCommands()
except:
    pass