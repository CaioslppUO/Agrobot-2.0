#!/usr/bin/env python3

"""
    Version: ROS 1.0.1
    Date: 26/02/2020, 13:41
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

    launchMsg = "roscore& "
    launchMsg += "cd .. && python3 comunication/webServer.py " + serverIp + "& "
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

if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')