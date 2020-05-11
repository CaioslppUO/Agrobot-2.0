#!/usr/bin/env python3

import rospy
from threading import Thread
from std_msgs.msg import String

vel = 100
limite = 40
direction = 0
perto = 0.5
medio = 2.0
longe = 7.0

frontPoint = 0
backPoint = 0
rightPoint = 0
leftPoint = 0
pointDirection = 0

lastRightPoint = 0
lastLeftPoint = 0
def move():
    global frontPoint,backPoint,rightPoint,leftPoint
    if( rightPoint < longe AND leftPoint < longe AND frontPoint < medio )
        vel = 100
        return True
    else:
        vel = 0
        return False

def correctDirection():
    global lastLeftPoint, lastRightPoint, rightPoint, leftPoint
    if(lastLeftPoint - leftPoint > 0.20 AND rightPoint - lastRightPoint > 0.20)
        direction+=10
    elif(leftPoint - lastLeftPoint > 0.20 AND lastRightPoint - rightPoint > 0.20)
        direction-=10
    lastRightPoint = rightPoint
    lastLeftPoint = leftPoint

def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

def callback(data):
    global pointDirection,frontPoint,backPoint,rightPoint,leftPoint
    pointDirection = str(data.data).split('$')
    frontPoint = pointDirection[0]
    backPoint = pointDirection[1]
    rightPoint = pointDirection[2]
    leftPoint = pointDirection[3]
    if(move()):
        correctDirection()
    

