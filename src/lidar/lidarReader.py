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
    selectedVet = []
    selectedVet.append(vet[centralPoint])
    while(i < range):
        selectedVet.append(vet[centralPoint+i])
        selectedVet.append(vet[centralPoint-i])
        i = i+1
    return selectedVet

def callback(msg):
    pubProcessedData.publish(str(getClosestObject(selectPoints(msg.ranges,angleRange,mf))) + '$'\
    + str(getClosestObject(selectPoints(msg.ranges,angleRange,mb))) + '$'\
    + str(getClosestObject(selectPoints(msg.ranges,angleRange,ml))) + '$'\
    + str(getClosestObject(selectPoints(msg.ranges,angleRange,mr))))
def getClosestObject(Vet):
    lowerValue = 100
    for testValue in Vet:
        if(not isinstance(testValue, str)):
            if (testValue < lowerValue):
                lowerValue = testValue 
    return lowerValue


rospy.init_node('lidar_values', anonymous=True)
pubProcessedData = rospy.Publisher("Lidar", String,queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()