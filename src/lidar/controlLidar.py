#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import String
import json

##Variavel que armazena a velocidade que será enviada para o robô
speed = 0
##Variavel que armazena a direção que será enviada para o robô
steer = 0
##Variavel de controle de tempo, para controlar o ciclo de chamadas que o robô vai andar para um lado
tick = 0

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

##Função para ler o arquivo .json
def readJson():
    with open('parameters.json','r') as file:
        return json.load(file)

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
    global dataDefault,speed,centerArea 
    if( centerArea == "free"):
        setSpeed(dataDefault['speedDefault'])
        checkTick()
    else:
        setSteer(0)
        setSpeed(0)

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

##Faz a leitura do arquivo .json
def readFile(data):
    global dataDefault
    dataDefault = readJson()

##Setter do bollean, que diz se pode andar ou não
def setWalk(data):
    global walk
    if(data.data == 'walk'):
        walk = True
    else:
        walk = False


##callback da leitura do topico /Lidar
def callback(data):
    global dataDefault,leftArea,rightArea,steer,centerArea,walk
    rospy.Subscriber('/Walk', String, SetWalk)
    if(walk):
        if(checkAuto()):
            pointDirection = str(data.data).split('$')
            leftArea = pointDirection[0]
            centerArea = pointDirection[1]
            rightArea = pointDirection[2]

            checkFoward()
            commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(dataDefault['limit']) + "*powerA$0*powerB$0*pulverize$" + str(dataDefault['uv'])
            pubControlCommand.publish(commandToPublish)
            rospy.Subscriber('/writeFile', String, readFile)
        else:
            commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
            pubControlCommand.publish(commandToPublish)
            rospy.Subscriber('/writeFile', String, readFile)
    else:
        commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$" + str(dataDefault['uv'])
        pubControlCommand.publish(commandToPublish)
        rospy.Subscriber('/writeFile', String, readFile)


##Função principal          
def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

##Inicialização do topico ControlLidar
rospy.init_node('ControlLidar', anonymous=True)

##Variável que controla a publicação de textos no tópico da ControlLidar
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)

dataDefault = readJson()
main()
