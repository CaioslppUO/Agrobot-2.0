#!/usr/bin/env python3

"""
Módulo que gerencia a montageme e distribuição dos comandos para os devidos dispositivos(hardware).
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_log = rospy.Publisher('log', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('command_decider', anonymous=True) 

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência o recebimento dos comandos, separação e envio para os devidos dispositivos.
class Control_mode():
    ## Método que inicializa os tópicos em que serão publicados comandos.
    def __init__(self):
        self.pub_relay = rospy.Publisher('relay', String, queue_size=10)
        self.pub_control_robot = rospy.Publisher('control_robot', String, queue_size=10)

    ## Método que envia os valores corretos para cada dispositivo.
    def send_comands(self,speed,steer,limit,power_a,power_b,pulverizer):
        self.pub_control_robot.publish(str(speed) + "$" + str(steer) + "$" + str(limit))
        self.pub_relay.publish("sendSignalToBoardOne:" + str(power_a))
        self.pub_relay.publish("sendSignalToBoardTwo:" + str(power_b))
        self.pub_relay.publish("sendSignalToPulverizer:" + str(pulverizer))

    ## Método que trata os comandos recebidos.
    def callback_comunication(self,msg):
        if(str(msg.data) != "No connection established."):
            info = str(msg.data).split("$")
            self.send_comands(int(info[0]), int(info[1]), int(info[2]), int(info[3]), int(info[4]), int(info[5]))
    
    ## Método que escuta o tópico CommandPriorityDecider e chama a função que trata os comandos.
    def listen_commands(self):
        rospy.Subscriber("command_priority_decider", String, self.callback_comunication)   
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == '__main__':
    try:
        control = Control_mode()
        const_pub_log.publish('startedFile$command_assembler')
        control.listen_commands()
    except:
        const_pub_log.publish("error$Fatal$Could not run command_assembler.py.")