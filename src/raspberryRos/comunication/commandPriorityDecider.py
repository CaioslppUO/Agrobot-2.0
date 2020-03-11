#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import sys
from std_msgs.msg import String
from commandStandardizer import CommandStandardizer

################################
#----> Global Definitions <----#
################################

rospy.init_node('CommandPriorityDecider', anonymous=True)

##############################
#----> Global Variables <----#
##############################

webServersReaded = 0
commandObservers = int(sys.argv[1])

################################
#----> Comunication class <----#
################################

class Comunication():
    def __init__(self):
        self.msg        = None
        self.priority   = None
        self.separator  = "*" #Symbol used to separate the message recieved from the app
        self.commandStandardizer = CommandStandardizer()

        #ROS
        self.pubComunication = rospy.Publisher('CommandPriorityDecider', String, queue_size=10)

    #Publish the command trough ROS
    def execute(self):
        global webServersReaded,commandObservers
        if(webServersReaded == commandObservers):
            self.pubComunication.publish(self.commandStandardizer.webServerMsgHandler(self.msg))
            self.msg = None
            self.priority = None
            webServersReaded = 0
        else:
            self.pubComunication.publish("No connection established.")

    #Set the msg variable with the message recieved from the webServer
    def callbackWebServerManual(self,data):
        global webServersReaded
        msg = str(data.data).split(self.separator)
        if(self.priority == None or int(msg[0]) < self.priority):
            self.priority = int(msg[0])
            self.msg = msg

        webServersReaded = webServersReaded + 1
        self.execute()

    def callbackComputationalVision(self,data):
        global webServersReaded
        msg = str(data.data).split(self.separator)
        if(self.priority == None or int(msg[0]) < self.priority):
            self.priority = int(msg[0])
            self.msg = msg

        webServersReaded = webServersReaded + 1
        self.execute()

    def listenWebServerManual(self):
        rospy.Subscriber("WebServerManual", String, self.callbackWebServerManual) 
        
    def listenComputationalVision(self):
        rospy.Subscriber("ComputationalVision",String,self.callbackComputationalVision)

    #Send commands even when there is no comunication with the webServer
    def sendCommands(self):
        self.msg = None
        self.listenWebServerManual()
        self.listenComputationalVision()
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

try:
    comunication = Comunication()
    comunication.sendCommands()
except:
    pass