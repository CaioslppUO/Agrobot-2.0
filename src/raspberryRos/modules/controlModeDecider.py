#!/usr/bin/env python

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
        self.pub = rospy.Publisher('ControlRobot', String, queue_size=10)

    def sendComands(self,speed,steer,limit):
        self.pub.publish(str(speed) + ":" + str(steer) + ":" + str(limit))


    def callbackComunication(self,data):
        if(str(data.data) != "No connection established."):
            cbAux = str(data.data).split("$")
            self.sendComands(int(cbAux[0]), int(cbAux[1]), int(cbAux[2]))
    
    def listenComunication(self):
        rospy.Subscriber("Comunication", String, self.callbackComunication)   
        rospy.spin()

if __name__ == '__main__':
    control = ControlMode()
    control.listenComunication()