#!/usr/bin/env python3

""" 
Programa que gerência quais e como serão executados todos os módulos do sistema.
"""

import os
import sys
import rospy
import time
from std_msgs.msg import String
from launcherVariables import LauncherVariables

#Inicialização do ROS
os.system("roscore& ")
time.sleep(8)
os.system("clear && echo 'ROS has been successfully initialized'& ")

## Nó da classe no ROS. anonymous=True faz com que o nome do nó da classe seja registrado como anônimo.
rospy.init_node('Controller', anonymous=True)

## Variável que controla a publicação de textos no tópico da Controller.
pubController = rospy.Publisher('Controller', String, queue_size=10)

## Função que Recebe todas as variáveis inicias e inicia os módulos que foram requeridos.
def mainLoop():
    global pubController
    launcher = LauncherVariables()
    serverIp,enableUart,enableRelay,uartAmount,enableFaceDetect,rootPath = launcher.variableSeparator(sys.argv)

    #Define quais módulos base serão inicializados
    launchMsg = "python3 " + rootPath + "comunication/webServer.py " + serverIp + "& "
    launchMsg += "python3 " + rootPath + "comunication/commandPriorityDecider.py& "
    launchMsg += "python3 " + rootPath + "modules/commandAssembler.py& "
    
    #Define quais módulos opcionais serão inicializados
    if(enableRelay == "True"):
        launchMsg += "python3 " + rootPath + "modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "python3 " + rootPath + "modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableFaceDetect == "True"):
        launchMsg += "python3 " + rootPath + "modules/coputationalVision.py& "

    #Inicializa os módulos que foram requeridos
    os.system(launchMsg)

    #Mensagem de log
    logPublish = "Modules were started"
    while not rospy.is_shutdown():
        pubController.publish(logPublish)

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')
