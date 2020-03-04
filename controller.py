#!/usr/bin/env python3

"""
    Version: ROS 1.0.9
    Date: 03/03/2020, 17:05
    Devs: Caio, Lucas, Levi

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

################################
#----> Ros Initialization <----#
################################

os.system("roscore& ")
time.sleep(8)
os.system("clear && echo 'ROS has been successfully initialized'& ")

################################
#----> Global Definitions <----#
################################

rospy.init_node('Controller', anonymous=True)

##############################
#----> Global Variables <----#
##############################

pubController = rospy.Publisher('Controller', String, queue_size=10)

#######################
#----> Main Loop <----#
#######################

def mainLoop():
    global pubController
    launcher = LauncherVariables()
    serverIp,enableUart,enableSensor,enableRelay,uartAmount = launcher.variableSeparator(sys.argv)

    #Define the base modules to be launched
    launchMsg = "cd .. && python3 comunication/webServer.py " + serverIp + "& "
    launchMsg += "cd .. && python3 comunication/comunication.py& "
    launchMsg += "cd .. && python3 modules/logs.py& "
    launchMsg += "cd .. && modules/controlModeDecider.py& "
    
    #Define wich optional modules will be launched
    if(enableRelay == "True"):
        launchMsg += "cd .. && python3 modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "cd .. && python3 modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableSensor == "True"):
        launchMsg += "cd .. && python3 modules/sensor.py& "

    #Launch all the required modules
    os.system(launchMsg)

    #Log Message
    logPublish = str(serverIp) + "$"
    logPublish += str(enableUart) + "$"
    logPublish += str(enableSensor) + "$"
    logPublish += str(enableRelay) + "$"
    logPublish += str(uartAmount)
    while not rospy.is_shutdown():
        pubController.publish(logPublish)

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')