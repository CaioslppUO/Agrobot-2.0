#!/usr/bin/env python3

"""
Módulo que lê os dados do lidar, e processa eles.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #


##Variavel de distancia para collisão, o codigo se baseia nela para mandar parar ou não
collision_distance = 1.5
##Ponto central do vetor de pontos
mf = 0
##Angulo para o vetor de pontos
angle_range = 16

pubProcessedData = rospy.Publisher("Lidar", String,queue_size=10)
# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('lidar_values', anonymous=True)
rospy.Publisher("Log",Strin,queue_size=10).publish("startedFile$lidarReader")

# ------------- #
# -> Funções <- #
# ------------- #

##Função que monta 3 vetores de pontos do lidar
#Recebe um vetor com 360 pontos do lidar, o angulo que deve ler dele e da onde deve começar a ler
#Retorna 3 vetores de pontos
def select_points(vet,range,central_point):
    i = 0
    direct_vet = []
    left_vet = []
    center_vet = []
    center_vet.append(vet[central_point])
    while(i < range/2):
        center_vet.append(vet[central_point+i])
        center_vet.append(vet[central_point-i])
        i=i+1
    i=0
    direct_vet.append(vet[central_point])
    left_vet.append(vet[central_point])
    while(i < range):
        direct_vet.append(vet[central_point+i])
        left_vet.append(vet[central_point-i])
        i = i+1
    return direct_vet,center_vet,left_vet


##Le o fator de distancia de colisão que vem do app
def callbabk_paramserver(data):
    global collision_distance
    if(str(data.data) != ''):
        vet = str(data.data).split('*')
        for variable in vet :
            newVariable = variable.split('$')
            if(newVariable[0] == 'detect'):
                collision_distance = float(newVariable[1])

##callback da chamada do topico do scan
#faz as devidas chamadas de funções e publica os resultadoss no topico Lidar
def callback(msg):
    global mf,angle_range
    RVet = []
    LVet = []
    CVet = []
    RVet,CVet,LVet = select_points(msg.ranges,angle_range,mf)
    rospy.Subscriber('/ParamServer', String, callbabk_paramserver)
    pubProcessedData.publish(str( get_closet_object(LVet) + "$" + get_closet_object(CVet) + "$" + get_closet_object(RVet) ))

##Verifica se tem algo perto do robô/sensor
#Rcebe um vetor de pontos
#Retorna free caso não houver nada na frente, ou busy caso houver algum ponto muito perto
def get_closet_object(Vet):
    global collision_distance
    for testValue in Vet:
        if(not isinstance(testValue, str)):
            if(testValue <= collision_distance):
                return "busy" 
    return "free"

def main():
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

try:
    main()
except KeyboardInterrupt:
    rospy.Publisher("Log",String,queue_size=10).publish("error$Warning$Program finalized")
    print('Program finalized')
