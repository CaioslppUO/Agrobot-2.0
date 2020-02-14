#!/usr/bin/env python

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

    launchMsg = "roscore& python comunication/webServer.py " + serverIp + "& " + "python comunication/comunication.py& python modules/logs.py& "
    if(enableRelay == "True"):
        launchMsg += "python modules/relay.py& "
    if(enableUart == "True"):
        launchMsg += "python modules/controlRobot.py " + str(uartAmount) + "& "
    if(enableSensor == "True"):
        launchMsg += "python modules/sensor.py& "

    os.system(launchMsg)

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')