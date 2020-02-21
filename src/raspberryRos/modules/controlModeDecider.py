#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
from std_msgs.msg import String

#######################################
#----> Control Mode Decide Class <----#
#######################################

class ControlMode():
    def __init__(self):
        rospy.init_node('ControlMode', anonymous=True) 
        self.pubRelay = rospy.Publisher('Relay', String, queue_size=10)
        self.pub = rospy.Publisher('ControlRobot', String, queue_size=10)

    def sendComands(self,speed,steer,limit,powerA,powerB):
        self.pub.publish(str(speed) + ":" + str(steer) + ":" + str(limit))
        self.pubRelay.publish("sendSignalToBoardOne:" + str(powerA))
        self.pubRelay.publish("sendSignalToBoardTwo:" + str(powerB))

    def callbackComunication(self,data):
        if(str(data.data) != "No connection established."):
            cbAux = str(data.data).split("$")
            self.sendComands(int(cbAux[0]), int(cbAux[1]), int(cbAux[2]), int(cbAux[3]), int(cbAux[4]))
    
    def listenComunication(self):
        rospy.Subscriber("Comunication", String, self.callbackComunication)   
        rospy.spin()

if __name__ == '__main__':
    control = ControlMode()
    control.listenComunication()