#!/usr/bin/env python3

"""
    Ver: ROS 1.1.6
    Data: 14/03/2020, 23:30
    Autores: Caio, Lucas, Levi

"""

#####################
#----> Imports <----#
#####################

import os
import sys
import rospy
import time
from std_msgs.msg import String
from launcherVariables import LauncherVariables

###################################
#----> Inicializações do ROS <----#
###################################

os.system("roscore& ") #Inicia o ROS
time.sleep(8)
os.system("clear && echo 'ROS has been successfully initialized'& ")

################################
#----> Definições Globais <----#
################################

rospy.init_node('Controller', anonymous=True)

###############################
#----> Variáveis Globais <----#
###############################

pubController = rospy.Publisher('Controller', String, queue_size=10)

############################
#----> Loop principal <----#
############################

def mainLoop():
    global pubController
    launcher = LauncherVariables()
    serverIp,enableUart,enableSensor,enableRelay,uartAmount,commandObservers,enableFaceDetect = launcher.variableSeparator(sys.argv)


    #Define quais módulos base serão inicializados
    launchMsg = "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 comunication/webServer.py " + serverIp + "& "
    launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 comunication/commandPriorityDecider.py " + str(commandObservers) + "& "
    launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 modules/logs.py& "
    launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && modules/commandAssembler.py& "
    
    #Define quais módulos opcionais serão inicializados
    if(enableRelay == "True"):
        launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableSensor == "True"):
        launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 modules/sensor.py& "
    if(enableFaceDetect == "True"):
        launchMsg += "cd /home/labiot/Agrobor-2.0/src/raspberryRos/ && python3 modules/coputationalVision.py& "

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