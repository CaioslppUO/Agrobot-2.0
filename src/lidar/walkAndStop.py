#!/usr/bin/env python3

"""
Modulo que cuidado do tempo que o robô fica parado e andando
"""
#####################
#----> Imports <----#
#####################

import rospy
from std_msgs.msg import String
import time

# ---------------- #
# -> Constantes <- #
# ---------------- #
pubControlCommand = rospy.Publisher("Walk", String,queue_size=10)
walk_time = 0
stop_time = 0

# ------------------- #
# -> Configurações <- #
# ------------------- #
rospy.init_node('Walk', anonymous=True)
rospy.Publisher("Log",Strin,queue_size=10).publish("startedFile$walkAndStop")

# ------------- #
# -> Funções <- #
# ------------- #

def set_variable(data):
  global walk_time,stop_time
  if(str(data.data) != ''):
      vet = str(data.data).split('*')
      for variable in vet :
          newVariable = variable.split('$')
          if(newVariable[0] == 'move'):
              walk_time = int(newVariable[1])
          elif(newVariable[0] == 'stop'):
              stop_time = int(newVariable[1])

##Contme toda a alogica de andar ,parar e escrever no topico
def main():
  global walk_time,stop_time
  while not rospy.is_shutdown():
    if(walk_time != 0 and stop_time != 0):
      pubControlCommand.publish("walk")
      time.sleep(walk_time)
      pubControlCommand.publish("stop")
      time.sleep(stop_time)
    else:
      pubControlCommand.publish("walk")  
    rospy.Subscriber('/ParamServer',String,set_variable)

try:
  main()
except KeyboardInterrupt:
  rospy.Publisher("Log",String,queue_size=10).publish("error$Warning$Program finalized")
  print('Program finalized')