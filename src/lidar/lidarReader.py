#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

frange = [0,45,315,359]
brange = [135,225]
lrange = [44,134]
rrange = [224,314]

mb = int((brange[0] + brange[1])/2)
ml = int((lrange[0] + lrange[1])/2)
mr = int((rrange[0] + rrange[1])/2)

def selectPoints(vet,range,centralPoint):
    i = 0
    selectedVet = []
    selectedVet.add(vet[centralPoint])
    while(i < range):
        selectPoints.add(vet[centralPoint+i])
        selectPoints.add(vet[centralPoint-i])
        i = i+1
    return selectedVet

def callback(msg):
    print('Front: ' + str(getClosestObject(selectPoints(msg.ranges,7,0))))
    print('Back: ' + str(getClosestObject(selectPoints(msg.ranges,7,mb))))
    print('Left: ' + str(getClosestObject(selectPoints(msg.ranges,7,ml))))
    print('Right: ' + str(getClosestObject(selectPoints(msg.ranges,7,mr))))

def getClosestObject(Vet):
    lowerValue = 100
    for testValue in Vet:
        if (testValue < lowerValue):
            lowerValue = testValue 
    return lowerValue

rospy.init_node('lidar_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()