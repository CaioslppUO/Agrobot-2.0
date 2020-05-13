import rospy
from std_msgs.msg import String
import json


dadosWrite = {}

def writeJson():
  with open('parameter.json','w') as file:
    json.dump(dadosWrite,file,ident=2,separators=(',',':'))


def callback(data):
  global dadosWrite
  dadosNo = str(data.data).split('$')

  dadosWrite['limit'] = dadosNo[0]
  dadosWrite['tickDefault'] = dadosNo[1]
  dadosWrite['steerDefault'] = dadosNo[2]
  dadosWrite['speedDefault'] = dadosNo[3]
  dadosWrite['shiftDirection'] = dadosNo[4]

  

def main():
  sub = rospy.Subscriber('/ParamServer', String, callback)
  rospy.spin()

main()