#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

frange = [0,45,315,359]
brange = [135,225]
lrange = [44,134]
rrange = [224,314]

collisionDistance = 1.5
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


def callback(data):
  global collisionDistance
  dadosNo = str(data.data).split('$')
  collisionDistance = dadosNo[5]


def callback(msg):
    global mf,angleRange
    RVet = []
    LVet = []
    RVet,LVet = selectPoints(msg.ranges,angleRange,mf)
    sub = rospy.Subscriber('/ParamServer', String, callBack)
    pubProcessedData.publish(str( getClosestObject(LVet) + "$" + getClosestObject(RVet) )

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