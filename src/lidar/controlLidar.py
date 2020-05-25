#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import String

##Variavel que armazena a velocidade que será enviada para o robô
speed = 0
##Variavel que armazena a direção que será enviada para o robô
steer = 0
##Variavel de controle de tempo, para controlar o ciclo de chamadas que o robô vai andar para um lado
tick = 0
uv = 0
##Armazena qual direção do robô deve virar
correctdir = "None"

##Armazena a leitura do sensor na parte esquerda, se esta livre ou nao
leftArea = "None"
##Armazena a leitura do sensor na parte direita, se esta livre ou nao
rightArea = "None"
##Armazena a leitura do sensor na parte central, se esta livre ou nao
centerArea = "None"

##bollean que recebe se o robo pode andar ou não
walk = True

##Setter da variavel Speed
def setSpeed(speednew):
    global speed
    speed = int(speednew)

##Setter da variavel steer
def setSteer(steernew):
    global steer
    steer = int(steernew)

##Função que confere o clico de chamadas para direcionar o robô
def checkTick():
    global tick
    if(tick == 0):
        setCorrection()
    else:
        correctDirection()
    
##Checa se existe algo na frente do robô.
#Se houver ele para o robô, caso contrario continua andando
def checkFoward():
    global dataDefault,centerArea,uv
    if( centerArea == "free"):
        setSpeed(dataDefault['speedDefault'])
        checkTick()
        uv = dataDefault['uv']
    else:
        setSteer(0)
        setSpeed(0)
        uv = 0


##Função que ajusta a direção do robô baseado na leitura do sensor
def correctDirection():
    global correctdir,tick,steer,dataDefault
    if(tick == 1):
        setSteer(dataDefault['steerDefault'])
    elif(correctdir == "right"):
        setSteer(int(dataDefault['steerDefault']) - int(dataDefault['shiftDirection']))
    else:
        setSteer(int(dataDefault['steerDefault']) + int(dataDefault['shiftDirection']))
    tick = int(tick) - 1
    
##Função que lê os dados do sensor e fazz as devidas chamadas de funções
def setCorrection():
    global leftArea,rightArea,tick,correctdir,dataDefault
    if(leftArea == "busy"):
        tick = dataDefault['tickDefault']
        correctdir = "right"
    if(rightArea == "busy"):
        tick = dataDefault['tickDefault']
        correctdir = "left"

##Verifica se é para o robô andar, ou ficar parado
def checkAuto():
    global dataDefault
    if(int(dataDefault['limit']) == 0 and int(dataDefault['tickDefault']) == 0 and int(dataDefault['steerDefault']) == 0 and int(dataDefault['speedDefault']) == 0 and int(dataDefault['shiftDirection']) == 0 ):
        return False
    return True

##Setter do bollean, que diz se pode andar ou não
def setWalk(data):
    global walk
    if(str(data.data) == 'walk'):
        walk = True
    else:
        walk = False

def setVariables(data):
    global dataDefault
    if(str(data.data) != ''):
        vet = str(data.data).split('*')
        for variable in vet :
            newVariable = variable.split('$')
            if(newVariable[0] == 'limit'):
                dataDefault['limit'] = newVariable[1]
            elif(newVariable[0] == 'tick'):
                dataDefault['tickDefault'] = newVariable[1]
            elif(newVariable[0] == 'steer'):
                dataDefault['steerDefault'] = newVariable[1]
            elif(newVariable[0] == 'speed'):
                dataDefault['speedDefault'] = newVariable[1]
            elif(newVariable[0] == 'shift'):
                dataDefault['shiftDirection'] = newVariable[1]
            elif(newVariable[0] == 'uv'):
                dataDefault['uv'] = newVariable[1]

##callback da leitura do topico /Lidar
def callback(data):
    global dataDefault,leftArea,rightArea,steer,centerArea,walk,uv
    rospy.Subscriber('/Walk', String, setWalk)
    if(walk):
        if(checkAuto()):
            pointDirection = str(data.data).split('$')
            leftArea = pointDirection[0]
            centerArea = pointDirection[1]
            rightArea = pointDirection[2]

            checkFoward()
            commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(dataDefault['limit']) + "*powerA$0*powerB$0*pulverize$" + str(uv)
            pubControlCommand.publish(commandToPublish)
        else:
            commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
            pubControlCommand.publish(commandToPublish)
        rospy.Subscriber('/ParamServer',String,setVariables)
    else:
        commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$" + str(dataDefault['uv'])
        pubControlCommand.publish(commandToPublish)


##Função principal          
def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

##Inicialização do topico ControlLidar
rospy.init_node('ControlLidar', anonymous=True)

##Variável que controla a publicação de textos no tópico da ControlLidar
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
dataDefault = {}
dataDefault['limit'] = 0
dataDefault['tickDefault'] = 0
dataDefault['steerDefault'] = 0
dataDefault['speedDefault'] = 0
dataDefault['shiftDirection'] = 0
dataDefault['uv'] = 0
rospy.Subscriber('/ParamServer',String,setVariables)
main()
