import rospy
from std_msgs.msg import String
import time

def setVariables(data):
    global walkTime,stopTime
    if(str(data.data) != ''):
        vet = str(data.data).split('*')
        for variable in vet :
            newVariable = variable.split('$')
            if(newVariable[0] == 'move'):
                walkTime = int(newVariable[1])
            elif(newVariable[0] == 'stop'):
                stopTime = int(newVariable[1])

##Contme toda a alogica de andar ,parar e escrever no topico
def main():
  global walkTime,stopTime
  while not rospy.is_shutdown():
    if(walkTime != 0 and stopTime != 0):
      pubControlCommand.publish("walk")
      time.sleep(walkTime)
      pubControlCommand.publish("stop")
      time.sleep(stopTime)
    else:
      pubControlCommand.publish("walk")  
    rospy.Subscriber('/ParamServer',String,setVariables)


##Declaração do nó Walk
rospy.init_node('Walk', anonymous=True)
pubControlCommand = rospy.Publisher("Walk", String,queue_size=10)
walkTime = 0
stopTime = 0
try:
  main()
except KeyboardInterrupt:
  pass
