#!/usr/bin/env python3

"""
Modulo que cuidado do tempo que o robô fica parado e andando
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy,time
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_control_command = rospy.Publisher("walk", String, queue_size=10)
const_pub_log = rospy.Publisher("log", String, queue_size=10)

const_walk_time = 0
const_stop_time = 0

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('walk', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que seta as variáveis de andar por 'x' e parar por 'y'.
def set_walk_by(msg):
  global const_walk_time,const_stop_time
  info = str(msg.data)
  if(info != ''):
      vet = info.split('*')
      for variable in vet :
          new_variable = variable.split('$')
          if(new_variable[0] == 'move'):
              const_walk_time = int(new_variable[1])
          elif(new_variable[0] == 'stop'):
              const_stop_time = int(new_variable[1])

## Função que executa as rotinas de escutar os valores de walk e stop e os publica no tópico walk, seguindo o tempo fornecido para cada um.
def main():
  while not rospy.is_shutdown():
    rospy.Subscriber('param_server',String,set_walk_by) #Leitura para verificar se os valores não foram alterados.
    stop_time = const_stop_time
    walk_time = const_walk_time
    if(const_walk_time != -1 and const_stop_time != -1):
      if(const_walk_time != 0 and const_stop_time != 0):
        const_pub_control_command.publish("stop")
        time.sleep(stop_time)
        const_pub_control_command.publish("walk")
        time.sleep(walk_time)
      else:
        const_pub_control_command.publish("walk")  
  

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try:
  const_pub_log.publish("startedFile$walk_and_stop.py")
  main()
except KeyboardInterrupt:
  const_pub_log.publish("error$Warning$walk_and_stop.py finalized.")