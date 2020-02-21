#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import time
from std_msgs.msg import String

pubWebServer = rospy.Publisher('LogsWebServer', String, queue_size=10)
pubComunication = rospy.Publisher('LogsComunication', String, queue_size=10)

def callbackComunication(data):
    pubComunication.publish("Comunication info: " + str(data.data))

def listenComunication():
    rospy.Subscriber("Comunication", String, callbackComunication) 

def callbackWebServer(data):
    pubWebServer.publish("WebServer info: " + str(data.data))

def listenWebServer():
    rospy.Subscriber("WebServer", String, callbackWebServer)     

#######################
#----> Main Loop <----#
#######################

def main():
    listenComunication()
    listenWebServer()
    rospy.spin()

try:
    rospy.init_node('Logs', anonymous=True)
    main()
except:
    pass