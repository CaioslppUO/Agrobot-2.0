#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import time
from std_msgs.msg import String

pubisherLog = rospy.Publisher('LogRobot', String, queue_size=10)

ComunicationSpeed = None
CommunicationSteer = None
ComunicationLimit = None
ComunicationPowerA = None
ComunicationPowerB = None
ComunicationPulverizer = None
WebServerStrig = None

def callbackComunication(data):
    SplitComunication = str(data.data).split('$')
    ComunicationSpeed = SplitComunication[0] 
    ComunicationSteer = SplitComunication[1]
    ComunicationLimit = SplitComunication[2]
    ComunicationPowerA = SplitComunication[3]
    ComunicationPowerB = SplitComunication[4]
    ComunicationPulverizer = SplitComunication[5]

def listenComunication():
    rospy.Subscriber("Comunication", String, callbackComunication) 

def callbackWebServer(data):
    WebServerStrig = str(data.data)

def listenWebServer():
    rospy.Subscriber("WebServer", String, callbackWebServer)   

def printLog():
    IndentationLog = "{0:<30}"
    print("\x1b[2J\x1b[1;1H")
    print(IndentationLog.format("Comunication variable"),end='|')
    print(IndentationLog.format("Web Server variable"),end='|\n')

    print(IndentationLog.format("Speed" + ComunicationSpeed),end='|')
    print(IndentationLog.format(""),end='|\n')

    print(IndentationLog.format("Steer" + ComunicationSteer),end='|')
    print(IndentationLog.format(""),end='|\n')

    print(IndentationLog.format("Limit" + ComunicationLimit),end='|')
    print(IndentationLog.format(""),end='|\n')

    print(IndentationLog.format("PowerA" + ComunicationPowerA),end='|')
    print(IndentationLog.format(""),end='|\n')

    print(IndentationLog.format("PowerB" + ComunicationPowerB),end='|')
    print(IndentationLog.format(""),end='|\n')

    print(IndentationLog.format("Pulverizador" + ComunicationPulverizer),end='|')
    print(IndentationLog.format(""),end='|\n')

    

def clearVariable():
    ComunicationSpeed = None
    CommunicationSteer = None
    ComunicationLimit = None
    ComunicationPowerA = None
    ComunicationPowerB = None
    ComunicationPulverizer = None
    WebServerStrig = None


#######################
#----> Main Loop <----#
#######################

def main():
    listenComunication()
    listenWebServer()
    printLog()
    clearVariable()
    rospy.spin()

try:
    rospy.init_node('Logs', anonymous=True)
    main()
except:
    pass