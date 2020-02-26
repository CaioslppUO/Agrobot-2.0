#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
from std_msgs.msg import String

################################
#----> Comunication class <----#
################################

class Comunication():
    def __init__(self):
        self.msg        = None
        self.separator  = "*"
        self.speed      = None
        self.steer      = None
        self.limit      = None
        self.powerA     = None
        self.powerB     = None
        self.pulverizer = None

        #ROS
        self.pub = rospy.Publisher('Comunication', String, queue_size=10)
        self.pub2 = rospy.Publisher('ControlRobot', String, queue_size=10)
        rospy.init_node('Comunication', anonymous=True)
        rospy.Subscriber("WebServer", String, self.callbackWebServer) 

    #Set the msg variable with the message recieved from the webServer
    def callbackWebServer(self,data):
        self.msg = str(data.data).split(self.separator)

    #Separate the message to it's respective variables and publish them in the Comunication ROS Topic
    def msgSeparator(self):
        if(self.msg != None):
            msgSize = int(self.msg[0])
            i = 1
            while(i <= msgSize):
                msgAux = self.msg[i].split('$')
                if(msgAux[0] == 'speed'):
                    self.speed = msgAux[1]
                elif(msgAux[0] == 'steer'):
                    self.steer = msgAux[1]
                elif(msgAux[0] == 'limit'):
                    self.limit = msgAux[1]
                elif(msgAux[0] == 'powerA'):
                    self.powerA = msgAux[1]
                elif(msgAux[0] == 'powerB'):
                    self.powerB = msgAux[1]
                elif(msgAux[0] == 'pulverize'):
                    self.pulverizer = msgAux[1]
                i = i+1

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

            self.pub.publish(speed + "$" + steer + "$" + limit + "$" + powerA + "$" + powerB + "$" + pulverizer)
            self.pub2.publish(speed + ":" + steer + ":" + limit)
        else:
            self.pub.publish("No connection established.")

    #Send commands even when there is no comunication with the webServer
    def sendCommands(self):
        rate = rospy.Rate(5) # 5hz
        while not rospy.is_shutdown():
            self.msg = None
            rate.sleep()
            self.msgSeparator()

try:
    comunication = Comunication()
    comunication.sendCommands()
except:
    pass