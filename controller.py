#!/usr/bin/env python3

"""
    Version: ROS 1.0.6
    Date: 26/02/2020, 16:11
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
time.sleep(5)
os.system("clear && echo 'ROS has been successfully initialized'& ")

##############################
#----> Global Variables <----#
##############################

rospy.init_node('Controller', anonymous=True)
pub = rospy.Publisher('Controller', String, queue_size=10)

#######################
#----> Main Loop <----#
#######################

def mainLoop():
    global pub
    launcher = LauncherVariables()
    serverIp,enableUart,enableSensor,enableRelay,uartAmount = launcher.variableSeparator(sys.argv)

    launchMsg = "cd .. && python3 comunication/webServer.py " + serverIp + "& "
    launchMsg += "cd .. && python3 comunication/comunication.py& "
    launchMsg += "cd .. && python3 modules/logs.py& "
    launchMsg += "cd .. && modules/controlModeDecider.py& "
    
    if(enableRelay == "True"):
        launchMsg += "cd .. && python3 modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "cd .. && python3 modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableSensor == "True"):
        launchMsg += "cd .. && python3 modules/sensor.py& "

    os.system(launchMsg)

    logPublish = str(serverIp) + "$"
    logPublish += str(enableUart) + "$"
    logPublish += str(enableSensor) + "$"
    logPublish += str(enableRelay) + "$"
    logPublish += str(uartAmount)
    while not rospy.is_shutdown():
        pub.publish(logPublish)

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')