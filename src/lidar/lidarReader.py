#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

frange = [0,45,315,359]
brange = [135,225]
lrange = [44,134]
rrange = [224,314]

mf = 0
mb = int((brange[0] + brange[1])/2)
ml = int((lrange[0] + lrange[1])/2)
mr = int((rrange[0] + rrange[1])/2)
angleRange = 11

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

def callback(msg):
    global mf,angleRange
    RVet = []
    LVet = []
    RVet,LVet = selectPoints(msg.ranges,angleRange,mf)

    pubProcessedData.publish(str( getClosestObject(LVet) + "$" getClosestObject(RVet) )

def getClosestObject(Vet):
    for testValue in Vet:
        if(not isinstance(testValue, str)):
            return "busy" 
        # if(testValue < 1.5):
            # return "busy" 
    return "free"


rospy.init_node('lidar_values', anonymous=True)
pubProcessedData = rospy.Publisher("Lidar", String,queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()