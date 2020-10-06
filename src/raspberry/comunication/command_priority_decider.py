#!/usr/bin/env python3

"""
Módulo que gerencia qual comando terá prioridade de execução e o envia para o ROS.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from std_msgs.msg import String
from command_standardizer import Command_standardizer

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)
## Instância que controla a publicação no tópico command_priority_decider.
const_pub_comunication = rospy.Publisher('command_priority_decider', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Iniciando o nó command_priority_decider.
rospy.init_node('command_priority_decider', anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que contém as prioridades de cada emissor de comandos.
class Priorities():
    def __init__(self):
        # Quanto maior o valor da prioridade, mais prioridade um comando tem sobre o outro.
        ## Prioridade de controle por terminal.
        self.manual_pc = 1001
        ## Prioridade de controle pelo app.
        self.manual_app = 1000
        ## Prioridade de controle pelo modo automático, utilizando o lidar.
        self.rasp_lidar = 999
        ## Prioridade de controle pelo modo automático, utilizando a câmera.
        self.computaional_vision = 998
        ## Quantidade de comandos garantidos quando um novo nível de prioridade é requerido.
        self.guaranteed_commands = 50 #Quantidade de comandos que precisam ser executados antes da prioridade ser liberada

## Classe que gerencia a comunicação de todos os emissores de comando com o sistema ROS.
class Comunication():
    def __init__(self):
        ## Comando recebida pelo emissor.
        self.msg = None
        ## Símbolo utilizado para separar os dados recebidos no comando.
        self.separator = "*"
        ## Instância da classe utilizada para padronizar os comandos recebidos.
        self.command_standardizer = Command_standardizer()
        ## Classe que contém os níveis de prioridade de cada emissor.
        self.priorities = Priorities()
        ## Variável utilizada para gerenciar qual é a prioridade do comando atualmente selecionado para ser enviado.
        self.priority = 0
        ## Variável utilizada para saber quantos comandos com maior prioridade ainda restam. 
        self.remaining_commands = 0

    ## Método que publica o comando para o tópico do ROS.
    def publish_selected_command(self):
        const_pub_comunication.publish(self.command_standardizer.msg_handler(self.msg))
        self.msg = None

    ## Método que escuta o tópico web_server_manual e executa a rotina necessária para tratar os dados.
    def listen_web_server_manual(self):
        rospy.Subscriber("web_server_manual", String, self.callback, self.priorities.manual_app) 

    ## Método que escuta o tópico computational_vision e executa a rotina necessária para tratar os dados.
    def listen_computational_vision(self):
        rospy.Subscriber("computational_vision", String, self.callback, self.priorities.computaional_vision)

    ## Método que escuta o tópico control_outdoors e executa a rotina necessária para tratar os dados.
    def listen_outdoor_controls(self):
        rospy.Subscriber("control_outdoors", String, self.callback, self.priorities.rasp_lidar)

    ## Método que escuta o tópico pc_manual e executa a rotina necessária para tratar os dados.
    def listen_pc_manual(self):
        rospy.Subscriber("pc_manual", String, self.callback, self.priorities.manual_pc)
   
    ## Método que escuta o tópico control_lidar e executa a rotina necessária para tratar os dados.
    def listen_control_lidar(self):
        rospy.Subscriber("control_lidar", String, self.callback, self.priorities.rasp_lidar)

    ## Método que define qual comando será executado baseado na prioridade.
    def callback(self,msg,priority):
        info = str(msg.data).split(self.separator)
        if(priority >= self.priority):
            self.priority = priority
            self.remaining_commands = self.priorities.guaranteed_commands
            self.msg = info
            self.publish_selected_command()
        elif(self.remaining_commands == 0):
            self.priority = priority
            self.remaining_commands = self.priorities.guaranteed_commands
            self.msg = info
            self.publish_selected_command()
        else:
            self.remaining_commands = self.remaining_commands - 1

    ## Método que executa as rotinas de listen e envio dos comandos ao programa.
    def listen_commands(self):
        self.msg = None
        self.listen_web_server_manual()
        self.listen_outdoor_controls()
        self.listen_computational_vision()
        self.listen_pc_manual()
        self.listen_control_lidar()
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try:
    comunication = Comunication()
    const_pub_log.publish('startedFile$command_priority_decider.py')
    comunication.listen_commands()
except:
    const_pub_log.publish("error$Fatal$CommandPriorityDecider could not run.")