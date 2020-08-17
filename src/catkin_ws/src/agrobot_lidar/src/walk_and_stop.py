#!/usr/bin/env python3

"""
Modulo que cuidado do tempo que o robô fica parado e andando
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy,time
from agrobot_msgs.msg import CommandWebServer,Automatic,Log

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação do topico Walk.
const_pub_control_command = rospy.Publisher("walk", Automatic, queue_size=10)
## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', Log, queue_size=10)


const_walk_time = 0
const_stop_time = 0

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('walk', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que faz logs.
def do_log(log_type,source_file,severity="",msg="",where=""):
    log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que seta as variáveis de andar por 'x' e parar por 'y'.
def set_walk_by(msg):
  global const_walk_time,const_stop_time
  if(msg != None):
    const_walk_time = msg.walkTime
    const_stop_time = msg.stopTime

## Função que executa as rotinas de escutar os valores de walk e stop e os publica no tópico walk, seguindo o tempo fornecido para cada um.
def main():
  while not rospy.is_shutdown():
    rospy.Subscriber('param_server',CommandWebServer,set_walk_by) #Leitura para verificar se os valores não foram alterados.
    walk_stop_permission = Automatic()
    stop_time = const_stop_time
    walk_time = const_walk_time
    if(const_walk_time != -1 and const_stop_time != -1):
      if(const_walk_time != 0 and const_stop_time != 0):
        walk_stop_object.walk_permission = "stop"
        const_pub_control_command.publish(walk_stop_object)
        time.sleep(stop_time)
        walk_stop_object.walk_permission = "walk"
        const_pub_control_command.publish(walk_stop_object)
        time.sleep(walk_time)
      else:
        walk_stop_object.walk_permission = "walk"
        const_pub_control_command.publish(walk_stop_object)  
  

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try:
  do_log("started_file","[optional] walk_and_stop.py")
  main()
except KeyboardInterrupt:
  do_log("error","walk_and_stop.py","Fatal","Module interrupted: walk_and_stop.py.","main")