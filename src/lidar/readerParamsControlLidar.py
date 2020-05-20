import rospy
from std_msgs.msg import String
import json


dadosWrite = {}

def writeJson():
  global dadosWrite
  with open('parameters.json','w') as file:
    json.dump(dadosWrite,file)
    pubCheck.publish("OK")

def callback(data):
  global dadosWrite
  dadosNo = str(data.data).split('$')

  dadosWrite['limit'] = int(dadosNo[0])
  dadosWrite['tickDefault'] = int(dadosNo[1])
  dadosWrite['steerDefault'] = int(dadosNo[2])
  dadosWrite['speedDefault'] = int(dadosNo[3])
  dadosWrite['shiftDirection'] = int(dadosNo[4])
  dadosWrite['uv'] = float(dadosNo[5])
  dadosWrite['walkBy'] = int(dadosNo[6])
  dadosWrite['stopBy'] = int(dadosNo[7])

  writeJson()

def main():
  sub = rospy.Subscriber('/ParamServer', String, callback)
  rospy.spin()


rospy.init_node('writeFile', anonymous=True)
pubCheck = rospy.Publisher("writeFile", String,queue_size=10)
main()
