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
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)

standart_data = {}
standart_data['limit'] = 0
standart_data['tickDefault'] = 0
standart_data['steerDefault'] = 0
standart_data['speedDefault'] = 0
standart_data['shiftDirection'] = 0
standart_data['uv'] = 0

# ------------------- #
# -> Configurações <- #
# ------------------- #

##Inicialização do topico ControlLidar
rospy.init_node('ControlLidar', anonymous=True)
rospy.Subscriber('/ParamServer',String,set_variable)
rospy.Publisher("Log",String,queue_size=10).publish("startedFile$controlLidar")

# ------------- #
# -> Funções <- #
# ------------- #

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
        speed = standart_data['speedDefault']
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
        setSteer(standart_data['steerDefault'])
    elif(correct_for == "right"):
        setSteer(int(standart_data['steerDefault']) - int(standart_data['shiftDirection']))
    else:
        setSteer(int(standart_data['steerDefault']) + int(standart_data['shiftDirection']))
    tick = int(tick) - 1
    
##Função que lê os dados do sensor e fazz as devidas chamadas de funções
def set_corretion(tick):
    global left_area,direct_area,correct_for,standart_data
    if(left_area == "busy"):
        tick = standart_data['tickDefault']
        correct_for = "right"
    if(direct_area == "busy"):
        tick = standart_data['tickDefault']
        correct_for = "left"

##Verifica se é para o robô andar, ou ficar parado
def checkAuto():
    global standart_data
    if(int(standart_data['limit']) == 0 and int(standart_data['tickDefault']) == 0 and int(standart_data['steerDefault']) == 0 and int(standart_data['speedDefault']) == 0 and int(standart_data['shiftDirection']) == 0 ):
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
            newVariable = variable.split('$')
            if(newVariable[0] == 'limit'):
                standart_data['limit'] = newVariable[1]
            elif(newVariable[0] == 'tick'):
                standart_data['tickDefault'] = newVariable[1]
            elif(newVariable[0] == 'steer'):
                standart_data['steerDefault'] = newVariable[1]
            elif(newVariable[0] == 'speed'):
                standart_data['speedDefault'] = newVariable[1]
            elif(newVariable[0] == 'shift'):
                standart_data['shiftDirection'] = newVariable[1]
            elif(newVariable[0] == 'uv'):
                standart_data['uv'] = newVariable[1]

##callback da leitura do topico /Lidar
def callback(data):
    global standart_data,left_area,direct_area,central_area,walk,uv
    rospy.Subscriber('/Walk', String, setWalk, walk)
    if(checkAuto()):
        if(walk):
            pointDirection = str(data.data).split('$')
            left_area = pointDirection[0]
            central_area = pointDirection[1]
            direct_area = pointDirection[2]

            check_foward(speed,steer,uv,tick)
            commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(standart_data['limit']) + "*powerA$0*powerB$0*pulverize$" + str(uv)
            pubControlCommand.publish(commandToPublish)
        else:
            commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$" + str(standart_data['uv'])
            pubControlCommand.publish(commandToPublish)
    else:
        commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
        pubControlCommand.publish(commandToPublish)
    rospy.Subscriber('/ParamServer',String,set_variable)

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
