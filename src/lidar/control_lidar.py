#!/usr/bin/env python3

"""
Módulo que controla o movimento do robô
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time
import rospy
from std_msgs.msg import String



# ---------------- #
# -> Constantes <- #
# ---------------- #

## Constante que define o que significa 'andar reto' para o robô.
const_default_foward = 0

## Constante que serve como 'folga' para o processamento de andar reto.
const_ignore_range = (5/100) * 360

##Variavel que armazena a velocidade que será enviada para o robô
speed = 0
##Variavel que armazena a direção que será enviada para o robô
steer = 0

##Variavel de controle de tempo, para controlar o ciclo de chamadas que o robô vai andar para um lado
tick = 0
uv = 0
##Armazena qual direção do robô deve virar
correct_for = "None"

##Armazena a leitura do sensor na parte esquerda, se esta livre ou nao
left_area = "None"
##Armazena a leitura do sensor na parte direita, se esta livre ou nao
direct_area = "None"
##Armazena a leitura do sensor na parte central, se esta livre ou nao
central_area = "None"

##bollean que recebe se o robo pode andar ou não
walk = True

##Variável que controla a publicação de textos no tópico da ControlLidar
pub_control_command = rospy.Publisher("control_lidar", String,queue_size=10)

standart_data = {}
standart_data['limit'] = 0
standart_data['tick_default'] = 0
standart_data['steer_default'] = 0
standart_data['speed_default'] = 0
standart_data['shift_direction'] = 0
standart_data['uv'] = 0

# ------------------- #
# -> Configurações <- #
# ------------------- #

##Inicialização do topico ControlLidar
rospy.init_node('control_lidar', anonymous=True)
rospy.Subscriber('/param_server',String,set_variable)
rospy.Publisher("Log",String,queue_size=10).publish("startedFile$controlLidar")

# ------------- #
# -> Funções <- #
# ------------- #

## Função que recebe o valor lido no acelerômetro e decide se tem que corrigir o movimento ou não.
# def choose_direction(msg):
    # value = int(msg.data)
    # if(value >= const_default_foward - const_ignore_range and value <= const_default_foward + const_ignore_range):
        # setSteer(dataDefault['steer_default'])
    # elif(value < const_default_foward - const_ignore_range):
        # return setSteer(int(dataDefault['steer_default']) - int(dataDefault['shift_direction']))
    # return setSteer(int(dataDefault['steer_default']) + int(dataDefault['shift_direction']))

##Função que confere o clico de chamadas para direcionar o robô
def check_tick(tick,steer):
    if(tick == 0):
        set_corretion(tick)
    else:
        correct_direction(tick,steer)
    
##Checa se existe algo na frente do robô.
#Se houver ele para o robô, caso contrario continua andando
def check_foward(speed,steer,uv,tick):
    global standart_data,central_area
    if( central_area == "free"):
        speed = standart_data['speed_default']
        uv = standart_data['uv']
        check_tick(tick,steer)
    else:
        steer = 0
        speed = 0
        uv = 0

##Função que ajusta a direção do robô baseado na leitura do sensor
def correct_direction(tick,steer):
    global correct_for,standart_data
    if(tick == 1):
        steer = standart_data['steer_default']
    elif(correct_for == "right"):
        steer = (int(standart_data['steer_default']) - int(standart_data['shift_direction']))
    else:
        steer = (int(standart_data['steer_default']) + int(standart_data['shift_direction']))
    tick = int(tick) - 1
    
##Função que lê os dados do sensor e fazz as devidas chamadas de funções
def set_corretion(tick):
    global left_area,direct_area,correct_for,standart_data
    if(left_area == "busy"):
        tick = standart_data['tick_default']
        correct_for = "right"
    if(direct_area == "busy"):
        tick = standart_data['tick_default']
        correct_for = "left"

##Verifica se é para o robô andar, ou ficar parado
def check_auto():
    global standart_data
    if(int(standart_data['limit']) == 0 and int(standart_data['tick_default']) == 0 and int(standart_data['steer_default']) == 0 and int(standart_data['speed_default']) == 0 and int(standart_data['shift_direction']) == 0 ):
        return False
    return True

##Setter do bollean, que diz se pode andar ou não
def setWalk(data,walk):
    if(str(data.data) == 'walk'):
        walk = True
    else:
        walk = False

def set_variable(data):
    global standart_data
    if(str(data.data) != ''):
        vet = str(data.data).split('*')
        for variable in vet :
            new_variable = variable.split('$')
            if(new_variable[0] == 'limit'):
                standart_data['limit'] = new_variable[1]
            elif(new_variable[0] == 'tick'):
                standart_data['tick_default'] = new_variable[1]
            elif(new_variable[0] == 'steer'):
                standart_data['steer_default'] = new_variable[1]
            elif(new_variable[0] == 'speed'):
                standart_data['speed_default'] = new_variable[1]
            elif(new_variable[0] == 'shift'):
                standart_data['shift_direction'] = new_variable[1]
            elif(new_variable[0] == 'uv'):
                standart_data['uv'] = new_variable[1]

##callback da leitura do topico /Lidar
def callback(data):
    global standart_data,left_area,direct_area,central_area,walk,uv
    rospy.Subscriber('/Walk', String, setWalk, walk)
    if(check_auto()):
        if(walk):
            point_direction = str(data.data).split('$')
            left_area = point_direction[0]
            central_area = point_direction[1]
            direct_area = point_direction[2]

            check_foward(speed,steer,uv,tick)
            rospy.Subscriber('angulo', String, choose_direction)
            command_to_publish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(standart_data['limit']) + "*powerA$0*powerB$0*pulverize$" + str(uv)
            pub_control_command.publish(command_to_publish)
        else:
            command_to_publish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$" + str(standart_data['uv'])
            pub_control_command.publish(command_to_publish)
    else:
        command_to_publish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
        pub_control_command.publish(command_to_publish)
    rospy.Subscriber('/param_server',String,set_variable)

##Função principal          
def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()


# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rospy.Publisher("Log",String,queue_size=10).publish("error$Warning$Program finalized")
        print('Program finalized')
