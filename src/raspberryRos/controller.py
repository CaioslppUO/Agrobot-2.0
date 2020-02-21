#!/usr/bin/env python3

"""
    Version: ROS 1.0.0
    Date: 11/02/2020, 22:40
    Devs: Caio, Lucas, Levi

"""

#####################
#----> Imports <----#
#####################

import os
import sys
from launcherVariables import LauncherVariables

#######################
#----> Main Loop <----#
#######################

def mainLoop():
    launcher = LauncherVariables()
    serverIp,enableUart,enableSensor,enableRelay,uartAmount = launcher.variableSeparator(sys.argv)

    launchMsg = "roscore& python3 /home/labiot/ros/src/agroBot/src/comunication/webServer.py " + serverIp + "& " + "python3 /home/labiot/ros/src/agroBot/src/comunication/comunication.py& python3 /home/labiot/ros/src/agroBot/src/modules/logs.py& python3 /home/labiot/ros/src/agroBot/src/modules/controlModeDecider.py& "
    if(enableRelay == "True"):
        launchMsg += "python3 /home/labiot/ros/src/agroBot/src/modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "python3 /home/labiot/ros/src/agroBot/src/modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableSensor == "True"):
        launchMsg += "python3 /home/labiot/ros/src/agroBot/src/modules/sensor.py& "

    os.system(launchMsg)

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')