#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

##Variavel de distancia para collisão, o codigo se baseia nela para mandar parar ou não
collisionDistance = 1.5
##Ponto central do vetor de pontos
mf = 0
##Angulo para o vetor de pontos
angleRange = 16

##Função que monta 3 vetores de pontos do lidar
#Recebe um vetor com 360 pontos do lidar, o angulo que deve ler dele e da onde deve começar a ler
#Retorna 3 vetores de pontos
def selectPoints(vet,range,centralPoint):
    i = 0
    RightVet = []
    LeftVet = []
    centerVet = []
    centerVet.append(vet[centralPoint])
    while(i < range/2):
        centerVet.append(vet[centralPoint+i])
        centerVet.append(vet[centralPoint-i])
        i=i+1
    i=0
    RightVet.append(vet[centralPoint])
    LeftVet.append(vet[centralPoint])
    while(i < range):
        RightVet.append(vet[centralPoint+i])
        LeftVet.append(vet[centralPoint-i])
        i = i+1
    return RightVet,centerVet,LeftVet


##Le o fator de distancia de colisão que vem do app
def callBackParamServer(data):
    global collisionDistance
    if(str(data.data) != ''):
        vet = str(data.data).split('*')
        for variable in vet :
            newVariable = variable.split('$')
            if(newVariable[0] == 'detect'):
                collisionDistance = float(newVariable[1])

##callback da chamada do topico do scan
#faz as devidas chamadas de funções e publica os resultadoss no topico Lidar
def callback(msg):
    global mf,angleRange
    RVet = []
    LVet = []
    CVet = []
    RVet,CVet,LVet = selectPoints(msg.ranges,angleRange,mf)
    rospy.Subscriber('/ParamServer', String, callBackParamServer)
    pubProcessedData.publish(str( getClosestObject(LVet) + "$" + getClosestObject(CVet) + "$" + getClosestObject(RVet) ))

##Verifica se tem algo perto do robô/sensor
#Rcebe um vetor de pontos
#Retorna free caso não houver nada na frente, ou busy caso houver algum ponto muito perto
def getClosestObject(Vet):
    global collisionDistance
    for testValue in Vet:
        if(not isinstance(testValue, str)):
            if(testValue <= collisionDistance):
                return "busy" 
    return "free"

##Declara um novo nó
rospy.init_node('lidar_values', anonymous=True)
pubProcessedData = rospy.Publisher("Lidar", String,queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
