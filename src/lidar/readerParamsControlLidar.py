import rospy
from std_msgs.msg import String
import json


dadosWrite = {}

def writeJson():
  global dadosWrite
  with open('parameter.json','w') as file:
    json.dump(dadosWrite,file,ident=2,separators=(',',':'))
    pubCheck.publish("OK")



def callback(data):
  global dadosWrite
  dadosNo = str(data.data).split('$')

  dadosWrite['limit'] = dadosNo[0]
  dadosWrite['tickDefault'] = dadosNo[1]
  dadosWrite['steerDefault'] = dadosNo[2]
  dadosWrite['speedDefault'] = dadosNo[3]
  dadosWrite['shiftDirection'] = dadosNo[4]

  writeJson()

  

def main():
  sub = rospy.Subscriber('/ParamServer', String, callback)
  rospy.spin()


rospy.init_node('writeFile', anonymous=True)
pubCheck = rospy.Publisher("writeFile", String,queue_size=10)
main()