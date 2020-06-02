#!/usr/bin/env python3

"""
Módulo que gerencia a montagem e distribuição dos comandos para os devidos gerênciadores de dispositivos(hardware).
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)
## Instância que controla a publicação no tópico relay.
const_pub_relay = rospy.Publisher('relay', String, queue_size=10)
## Instância que controla a publicação no tópico control_robot.
const_pub_control_robot = rospy.Publisher('control_robot', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó command_decider.
rospy.init_node('command_decider', anonymous=True) 

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência o recebimento dos comandos, separação e envio para os devidos gerênciadores.
class Assembler():
    def __init__(self):
        ## Variável que guarda o último sinal enviado ao relé do pulverizador.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_pulverize_signal = 0
        ## Variável que guarda o último valor de speed.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_speed = 0
        ## Variável que guarda o último valor de steer.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_steer = 0
        ## Variável que guarda o último valor de limit.
        # Utilizada para evitar o envio de comandos desnecessários pelos tópicos do ROS.
        self.last_limit = 0
        
    ## Método que envia os valores corretos para cada gerênciador.
    def send_comands(self,speed,steer,limit,power_a,power_b,pulverizer):
        if(int(speed) != self.last_speed or int(steer) != self.last_steer or int(limit) != self.last_limit):
            self.last_speed = int(speed)
            self.last_steer = int(steer)
            self.last_limit = int(limit)
            const_pub_control_robot.publish(str(speed) + "$" + str(steer) + "$" + str(limit))
        if(int(power_a ) != 0):
            const_pub_relay.publish("sendSignalToBoardOne$" + str(power_a))
        if(int(power_b) != 0):
            const_pub_relay.publish("sendSignalToBoardTwo$" + str(power_b))
        if(int(pulverizer) != self.last_pulverize_signal):
            self.last_pulverize_signal = int(pulverizer)
            const_pub_relay.publish("sendSignalToPulverizer$" + str(pulverizer))

    ## Método que trata os comandos recebidos.
    def callback_comunication(self,msg):
        if(str(msg.data) != "No connection established."):
            info = str(msg.data).split("$")
            self.send_comands(int(info[0]), int(info[1]), int(info[2]), int(info[3]), int(info[4]), int(info[5]))
    
    ## Método que escuta o tópico command_priority_decider e chama a função que trata os comandos.
    def listen_commands(self):
        rospy.Subscriber("command_priority_decider", String, self.callback_comunication)   
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == '__main__':
    try:
        assembler = Assembler()
        const_pub_log.publish('startedFile$command_assembler')
        assembler.listen_commands()
    except:
        const_pub_log.publish("error$Fatal$Could not run command_assembler.py.")