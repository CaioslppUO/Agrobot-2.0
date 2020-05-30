#!/usr/bin/env python3

"""
Módulo que lê os dados do lidar e processa eles.
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

## Constante de distancia para collisão.
# Indica a qual distância os objetos devem ser considerados como 'próximos'.
const_detect_collision_distance = 1.5
## Ponto central(Frente do robô) do vetor de pontos.
const_center_point = 0
## Ângulo ou número de pontos a serem pegos para o cálculo no vetor de pontos(Em cada direção).
const_angle_range = 16

const_pub_processed_data = rospy.Publisher("lidar", String,queue_size=10)
const_pub_log = rospy.Publisher("log", String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('lidar_values', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que monta 3 vetores de pontos lidos do vetor de pontos do lidar.
def select_points(vet,range,central_point):
    i = 0
    right_vet = []
    left_vet = []
    center_vet = []

    center_vet.append(vet[central_point])
    while(i < range/2):
        center_vet.append(vet[central_point+i])
        center_vet.append(vet[central_point-i])
        i=i+1

    i=0
    right_vet.append(vet[central_point])
    left_vet.append(vet[central_point])

    while(i < range):
        right_vet.append(vet[central_point+i])
        left_vet.append(vet[central_point-i])
        i = i+1

    return right_vet,center_vet,left_vet

## Callback para o param_server. Lê e atualiza a distância de detecção de colisão.
def callback_paramserver(msg):
    global const_detect_collision_distance
    info = str(msg.data)
    if(info != ''):
        vet = info.split('*')
        for variable in vet :
            new_variable = variable.split('$')
            if(new_variable[0] == 'detect'):
                const_detect_collision_distance = float(new_variable[1])

## Callback do topico do scan do lidar. Processa a mensagem recebida e publica o resultado no tópico lidar.
def callback_lidar_scan(msg):
    r_vet,c_vet,l_vet = select_points(msg.ranges,const_angle_range,const_center_point)
    rospy.Subscriber('param_server', String, callback_paramserver)
    const_pub_processed_data.publish(str( get_closet_object(l_vet) + "$" + get_closet_object(c_vet) + "$" + get_closet_object(r_vet) ))

## Função que retorna se existe um objeto 'próximo' a um dos sensores do robô, baseado na distância de colisão.
def get_closet_object(vet):
    for test_value in vet:
        if(not isinstance(test_value, str)):
            if(test_value <= const_detect_collision_distance):
                return "busy" 
    return "free"

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try:
    const_pub_log.publish("startedFile$lidar_reader.py")
    rospy.Subscriber('scan', LaserScan, callback_lidar_scan)
    rospy.spin()
except KeyboardInterrupt:
    const_pub_log.publish("error$Warning$lidar_reader.py finalized.")
