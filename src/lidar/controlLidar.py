121#!/usr/bin/env python3

import rospy
import time
from threading import Thread
from std_msgs.msg import String

speed = 100
limit = 40
steer = 0
perto = 0.3
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
    global frontPoint,backPoint,rightPoint,leftPoint,longe,medio,speed
    if( rightPoint < longe and leftPoint < longe and frontPoint > medio ):
        speed = 100
        return True
    else:
        speed = 0
        return False
    
def correctDirection():
    global rightPoint, leftPoint,steer
    if(leftPoint < perto):
        steer+=1
    if(rightPoint < perto):
        steer-=1

def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

def callback(data):
    global pointDirection,frontPoint,backPoint,rightPoint,leftPoint
    commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
    pointDirection = str(data.data).split('$')
    frontPoint = float(pointDirection[0])
    backPoint = float(pointDirection[1])
    leftPoint = float(pointDirection[2])
    rightPoint = float(pointDirection[3])
    if(move()):
        correctDirection()
    commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(limit) + "*powerA$0*powerB$0*pulverize$0"
    pubControlCommand.publish(commandToPublish)
    

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
main()
