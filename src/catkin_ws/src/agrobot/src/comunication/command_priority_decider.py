#!/usr/bin/env python3

"""
Módulo que gerencia qual comando terá prioridade de execução e o envia para o ROS.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from agrobot_msgs.msg import CompleteControl,Log
from std_msgs.msg import String
from command_standardizer import Command_standardizer

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)
## Instância que controla a publicação no tópico command_priority_decider.
const_pub_comunication: rospy.Publisher = rospy.Publisher('command_priority_decider', CompleteControl, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Iniciando o nó command_priority_decider.
rospy.init_node('command_priority_decider', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que faz logs.
def do_log(log_type: str,source_file: str,severity: str ="",msg: str ="",where: str =""):
    log: Log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que finaliza o módulo ao receber o comando certo no tópico shutdown.
def callback_shutdown(file_to_shutdown):
    if(str(file_to_shutdown.data) == "shutdown_command_priority_decider"):
        do_log("error","command_priority_decider.py","Warning","Command priority decider finalized.",
            "function callback_shutdown()")
        rospy.signal_shutdown("Command priority decider finalized")
        exit(0)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que contém as prioridades de cada emissor de comandos.
class Priorities():
    def __init__(self):
        # Quanto maior o valor da prioridade, mais prioridade um comando tem sobre o outro.
        ## Prioridade de controle por terminal.
        self.manual_pc: int = 1001
        ## Prioridade de controle pelo app.
        self.manual_app: int = 1000
        ## Prioridade de controle pelo modo automático, utilizando o lidar.
        self.rasp_lidar: int = 999
        ## Prioridade de controle pelo modo automático, utilizando a câmera.
        self.computaional_vision: int = 998
        ## Quantidade de comandos garantidos quando um novo nível de prioridade é requerido.
        self.guaranteed_commands: int = 50 #Quantidade de comandos que precisam ser executados antes da prioridade ser liberada

## Classe que gerencia a comunicação de todos os emissores de comando com o sistema ROS.
class Comunication():
    def __init__(self):
        ## Comando recebida pelo emissor.
        self.command_received = None
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
        const_pub_comunication.publish(self.command_standardizer.msg_handler(self.command_received))
        self.command_received = None

    ## Método que escuta o tópico web_server_manual e executa a rotina necessária para tratar os dados.
    def listen_web_server_manual(self):
        rospy.Subscriber("web_server_manual", CompleteControl, self.callback, self.priorities.manual_app) 

    ## Método que escuta o tópico computational_vision e executa a rotina necessária para tratar os dados.
    def listen_computational_vision(self):
        rospy.Subscriber("computational_vision", CompleteControl, self.callback, self.priorities.computaional_vision)

    ## Método que escuta o tópico control_outdoors e executa a rotina necessária para tratar os dados.
    def listen_outdoor_controls(self):
        rospy.Subscriber("control_outdoors", CompleteControl, self.callback, self.priorities.rasp_lidar)

    ## Método que escuta o tópico pc_manual e executa a rotina necessária para tratar os dados.
    def listen_pc_manual(self):
        rospy.Subscriber("pc_manual", CompleteControl, self.callback, self.priorities.manual_pc)
   
    ## Método que escuta o tópico control_lidar e executa a rotina necessária para tratar os dados.
    def listen_control_lidar(self):
        rospy.Subscriber("control_lidar", CompleteControl, self.callback, self.priorities.rasp_lidar)

    ## Método que define qual comando será executado baseado na prioridade.
    def callback(self,command_received: CompleteControl,priority: int):
        if(priority >= self.priority):
            self.priority = priority
            self.remaining_commands = self.priorities.guaranteed_commands
            self.command_received = command_received
            self.publish_selected_command()
        elif(self.remaining_commands == 0):
            self.priority = priority
            self.remaining_commands = self.priorities.guaranteed_commands
            self.command_received = command_received 
            self.publish_selected_command()
        else:
            self.remaining_commands = self.remaining_commands - 1

    ## Método que executa as rotinas de listen e envio dos comandos ao programa.
    def listen_commands(self):
        self.command_received = None
        self.listen_web_server_manual()
        self.listen_outdoor_controls()
        self.listen_computational_vision()
        self.listen_pc_manual()
        self.listen_control_lidar()
        rospy.Subscriber("shutdown", String, callback_shutdown)
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try:
    do_log("started_file","[essential] command_priority_decider.py")
    Comunication().listen_commands()
except:
    do_log("error","command_priority_decider.py","Fatal","Could not run command_priority_decider.py","main")
