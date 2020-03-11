#!/usr/bin/env python3

"""
    Version: ROS 1.1.5
    Date: 06/03/2020, 15:32
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
    serverIp,enableUart,enableSensor,enableRelay,uartAmount,commandObservers,enableFaceDetect = launcher.variableSeparator(sys.argv)

    #Define the base modules to be launched
    launchMsg = "cd .. && python3 comunication/webServer.py " + serverIp + "& "
    launchMsg += "cd .. && python3 comunication/commandPriorityDecider.py " + str(commandObservers) + "& "
    launchMsg += "cd .. && python3 modules/logs.py& "
    launchMsg += "cd .. && modules/commandAssembler.py& "
    
    #Define wich optional modules will be launched
    if(enableRelay == "True"):
        launchMsg += "cd .. && python3 modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "cd .. && python3 modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableSensor == "True"):
        launchMsg += "cd .. && python3 modules/sensor.py& "
    if(enableFaceDetect == "True"):
        launchMsg += "cd .. && python3 modules/coputationalVision.py& "

    #Launch all the required modules
    os.system(launchMsg)

    #Log Message
    logPublish = "Modules were started"
    while not rospy.is_shutdown():
        pubController.publish(logPublish)

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')