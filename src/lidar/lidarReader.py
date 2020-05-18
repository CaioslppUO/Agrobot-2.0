#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String


collisionDistance = 1.5
mf = 0
angleRange = 16

def selectPoints(vet,range,centralPoint):
    i = 0
    RightVet = []
    LeftVet = []
    RightVet.append(vet[centralPoint])
    LeftVet.append(vet[centralPoint])
    while(i < range):
        RightVet.append(vet[centralPoint+i])
        LeftVet.append(vet[centralPoint-i])
        i = i+1
    return RightVet,LeftVet


def callBack(data):
  global collisionDistance
  dadosNo = str(data.data).split('$')
  collisionDistance = float(dadosNo[5])


def callback(msg):
    global mf,angleRange
    RVet = []
    LVet = []
    RVet,LVet = selectPoints(msg.ranges,angleRange,mf)
    sub = rospy.Subscriber('/ParamServer', String, callBack)
    pubProcessedData.publish(str( getClosestObject(LVet) + "$" + getClosestObject(RVet) ))


def getClosestObject(Vet):
    global collisionDistance
    for testValue in Vet:
        if(not isinstance(testValue, str)):
            if(testValue <= collisionDistance):
                return "busy" 
    return "free"


rospy.init_node('lidar_values', anonymous=True)
pubProcessedData = rospy.Publisher("Lidar", String,queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
