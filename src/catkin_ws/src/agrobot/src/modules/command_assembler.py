#!/usr/bin/env python3

"""
Módulo que gerencia a montagem e distribuição dos comandos para os devidos gerênciadores de dispositivos(hardware).
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from agrobot_msgs.msg import Relay,Control,CompleteControl,Log
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)
## Instância que controla a publicação no tópico relay.
const_pub_relay: rospy.Publisher = rospy.Publisher('relay', Relay, queue_size=10)
## Instância que controla a publicação no tópico control_robot.
const_pub_control_robot: rospy.Publisher = rospy.Publisher('control_robot', Control, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó command_decider.
rospy.init_node('command_decider', anonymous=True) 

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
    if(str(file_to_shutdown.data) == "shutdown_command_assembler"):
        do_log("error","command_assembler.py","Warning","Command assembler finalized.","function callback_shutdown()")
        rospy.signal_shutdown("Command assembler finalized")
        exit(0)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência o recebimento dos comandos, separação e envio para os devidos gerênciadores.
class Assembler():
    def __init__(self):
        ## Variável que guarda o último sinal enviado ao relé do pulverizador.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_pulverize_signal: str = "0"
        ## Variável que guarda o último valor de speed.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_speed: int = 0
        ## Variável que guarda o último valor de steer.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_steer: int = 0
        ## Variável que guarda o último valor de limit.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_limit: int = 0

    ## Método que verifica se os comandos de controle recebidos não estão duplicados. Evita excesso de envio de comandos pelo ROS.
    def check_repeated_controls(self,speed: int,steer: int,limit: int):
        return speed != self.last_speed or steer != self.last_steer or limit != self.last_limit or (speed == 0 and steer == 0 and limit == 0)
        
    ## Método que envia os comandos de controle de movimento.
    def send_control_command(self,control_command: Control):
        if(self.check_repeated_controls(control_command.speed,control_command.steer,control_command.limit)):
            self.last_speed = int(control_command.speed)
            self.last_steer = int(control_command.steer)
            self.last_limit = int(control_command.limit)
            control_command.power = 0 # Todo comando de controle não comanda o relé que liga ou desliga a placa do hover.
            const_pub_control_robot.publish(control_command)

    ## Método que envia os comandos de controle de relé.
    def send_relay_command(self,relay_command: Relay):
        if(int(relay_command.power_a) != 0):
            const_pub_relay.publish(relay_command)
        if(int(relay_command.power_b) != 0):
            const_pub_relay.publish(relay_command)
        if(str(relay_command.power_pulverize) != self.last_pulverize_signal):
            self.last_pulverize_signal = str(relay_command.power_pulverize)
            const_pub_relay.publish(relay_command)

    ## Método que envia os valores corretos para cada gerênciador.
    def send_comands(self,complete_control_command: CompleteControl):
        self.send_control_command(complete_control_command.control)
        self.send_relay_command(complete_control_command.relay)

    ## Método que trata os comandos recebidos.
    def callback_comunication(self,complete_control_command: CompleteControl):
        if(complete_control_command != None):
            self.send_comands(complete_control_command)
    
    ## Método que escuta o tópico command_priority_decider e chama a função que trata os comandos recebidos.
    def listen_commands(self):
        rospy.Subscriber("command_priority_decider", CompleteControl, self.callback_comunication)   
        rospy.Subscriber("shutdown", String, callback_shutdown)
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == '__main__':
    try:
        do_log("started_file","[essential] command_assembler.py")
        Assembler().listen_commands()
    except:
        do_log("error","command_assembler.py","Fatal","Could not run command_assembler.py.","main")