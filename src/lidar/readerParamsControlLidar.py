import rospy
from std_msgs.msg import String
import json

##Variavel que recebera tudo que vem do App
dadosWrite = {}

##Escreve as varaiveis que vem do App em um arquivo .json
def writeJson():
  global dadosWrite
  with open('parameters.json','w') as file:
    json.dump(dadosWrite,file)
    pubCheck.publish("OK")

##Callback da leitura do topico ParamServer
def callback(data):
  global dadosWrite
  dadosNo = str(data.data).split('$')

  dadosWrite['limit'] = dadosNo[0]
  dadosWrite['tickDefault'] = dadosNo[1]
  dadosWrite['steerDefault'] = dadosNo[2]
  dadosWrite['speedDefault'] = dadosNo[3]
  dadosWrite['shiftDirection'] = dadosNo[4]
  dadosWrite['uv'] = dadosNo[5]
  dadosWrite['walkBy'] = dadosNo[6]
  dadosWrite['stopBy'] = dadosNo[7]

  writeJson()

##Função principal, que contem as chamadas de callback
def main():
  sub = rospy.Subscriber('/ParamServer', String, callback)
  rospy.spin()

##Declaração do nó write File
rospy.init_node('writeFile', anonymous=True)
pubCheck = rospy.Publisher("writeFile", String,queue_size=10)
main()
