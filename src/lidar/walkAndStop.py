import rospy
from std_msgs.msg import String
import json
import time

walktTime = 0
stopTime = 0

##Lê as varaiveis que vem do App em um arquivo .json
def readJson():
  with open('parameters.json','r') as file:
    return json.load(file)

##Faz a chamada de função para ler o arquivo .json e as devidas atribuições
def readFile(data):
  global walktTime,stopTime
  dataDefault = readJson()
  walktTime = int(dataDefault['walkBy'])
  stopTime = int(dataDefault['stopBy'])

##Contme toda a alogica de andar ,parar e escrever no topico
def main():
  global walktTime,stopTime
  rospy.Subscriber('/writeFile', String, readFile)
  if(walkTime != 0 and stopTime != 0):
    pubControlCommand.publish("walk")
    time.sleep(walkTime)
    pubControlCommand.publish("stop")
    time.sleep(stopTime)
  else:
    pubControlCommand.publish("walk")
  rospy.spin()

##Declaração do nó Walk
rospy.init_node('Walk', anonymous=True)
pubControlCommand = rospy.Publisher("Walk", String,queue_size=10)
main()