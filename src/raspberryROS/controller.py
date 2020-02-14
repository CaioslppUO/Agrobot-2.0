#!/usr/bin/env python

"""
    Version: ROS 1.0.0
    Date: 11/02/2020, 20:52
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
    os.system("python webServer.py " + serverIp + "& " + "python comunication.py& python logs.py")
    
if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')