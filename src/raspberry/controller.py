#!/usr/bin/env python3

""" 
Programa que gerencia quais e como serão executados todos os módulos do sistema.
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
os.system("clear && echo 'Roscore has been successfully initialized'& ")

## Variável que controla a publicação de logs
pubLog = rospy.Publisher('Log', String, queue_size=10)

## Nó da classe no ROS. anonymous=True faz com que o nome do nó da classe seja registrado como anônimo.
rospy.init_node('Controller', anonymous=True)

## Função que Recebe todas as variáveis inicias e inicia os módulos que foram requeridos.
def mainLoop():
    global pubLog
    launcher = LauncherVariables()
    serverIp,enableUart,enableRelay,uartAmount,enableFaceDetect,rootPath = launcher.variableSeparator(sys.argv)

    #Define quais módulos base serão inicializados
    os.system("python3 " + rootPath + "modules/logs.py& ")
    print('Startind modules...')
    time.sleep(10)
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
    pubLog.publish("startedFile$Controller")
    time.sleep(5)
    
    #Mostra na tela quais módulos foram abertos
    print('Open modules: \n')
    os.system('cat ' + rootPath + "logs/startedFiles.log")

    #Indica a situação atual do sistema
    print('\nStatus: Running')
    
    #Mensagem de log
    while not rospy.is_shutdown():
        a = -1

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')
