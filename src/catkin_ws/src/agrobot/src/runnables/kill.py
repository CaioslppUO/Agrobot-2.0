#!/usr/bin/env python3

"""
Módulo que finaliza a execução de um nó ROS .
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy,sys
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de comandos de desligamento.
const_shutdown_publisher = rospy.Publisher("shutdown", String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node("shutdown", anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que finaliza todos os nós ROS na ordem correta. Também finaliza o roscore.
def kill(node_name: str):
    command = "shutdown_" + node_name
    if(node_name == "" or node_name == "roscore"):
        command = "shutdown"
    const_shutdown_publisher.publish(command)

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try: # Finaliza o arquivo passado como parâmetro.
    kill(str(rospy.get_param("/param_to_kill")))
except: # Finaliza o roscore.
    kill("")
    