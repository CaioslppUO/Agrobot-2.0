#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import sys
from std_msgs.msg import String

################################
#----> Global Definitions <----#
################################

rospy.init_node('CommandPriorityDecider', anonymous=True)

##############################
#----> Global Variables <----#
##############################

webServersReaded = 0
commandObservers = int(sys.argv[1])

#######################
#----> Functions <----#
#######################

#Check and correct the speed value if it is needed
def checkSpeed(speed):
    if(speed < -100):
        return -100
    if(speed > 100):
        return 100
    return speed

#Check and correct the steer value if it is needed
def checkSteer(steer):
    if(steer < -100):
        return -100
    if(steer > 100):
        return 100
    return steer

#Check and correct the limit value if it is needed
def checkLimit(limit):
    if(limit < 0):
        return 0
    if(limit > 100):
        return 100
    return limit

#Check and correct the relay value if it is needed
def checkRelays(signal):
    if(signal != 0 and signal != 1):
        return 0
    return signal

#Check and correct all recieved variables from the WebServer
def checkMessageRecieved(msg):
    if(msg != None):
        try:
            speed  = int(str(msg[1]).split("$")[1])
            steer  = int(str(msg[2]).split("$")[1])
            limit  = int(str(msg[3]).split("$")[1])
            powerA = int(str(msg[4]).split("$")[1])
            powerB = int(str(msg[5]).split("$")[1])
            pulver = int(str(msg[6]).split("$")[1])
            
            speed  = int(checkSpeed(speed)) 
            steer  = int(checkSteer(steer))
            limit  = int(checkLimit(limit))
            powerA = int(checkRelays(powerA))
            powerB = int(checkRelays(powerB))
            pulver = int(checkRelays(pulver))
            
            return speed,steer,limit,powerA,powerB,pulver
        except:
            return None,None,None,None,None,None
    else:
        return None,None,None,None,None,None

################################
#----> Comunication class <----#
################################

class Comunication():
    def __init__(self):
        self.msg        = None
        self.speed      = None
        self.steer      = None
        self.limit      = None
        self.powerA     = None
        self.powerB     = None
        self.pulverizer = None
        self.priority   = None
        self.separator  = "*" #Symbol used to separate the message recieved from the app

        #ROS
        self.pubComunication = rospy.Publisher('CommandPriorityDecider', String, queue_size=10)

    def execute(self):
        global webServersReaded,commandObservers
        if(webServersReaded == commandObservers):
            self.msgSeparator()
            self.msg = None
            self.priority = None
            webServersReaded = 0

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

    #Separate the message to it's respective variables and publish them in the Comunication ROS Topic
    def msgSeparator(self):
        self.speed,self.steer,self.limit,self.powerA,self.powerB,self.pulverizer = checkMessageRecieved(self.msg)
        if(self.msg != None):
            speed = self.speed
            steer = self.steer
            limit = self.limit
            powerA = self.powerA
            powerB = self.powerB
            pulverizer = self.pulverizer

            self.speed = None
            self.steer = None
            self.limit = None
            self.powerA = None
            self.powerB = None
            self.pulverizer = None
            
            self.pubComunication.publish(str(speed) + "$" + str(steer) + "$" + str(limit) + "$" + str(powerA) + "$" + str(powerB) + "$" + str(pulverizer))
        else:
            self.pubComunication.publish("No connection established.")

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