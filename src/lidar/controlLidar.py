#!/usr/bin/env python3

import rospy
import time
from threading import Thread
from std_msgs.msg import String

speed = 100
limit = 40
steer = 0
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
        speed = 100
        return True
    else:
        speed = 0
        return False

def correctHardDirection(arg):
    steer+=arg
    time.sleep(1)
    steer-=arg
    
def correctDirection():

    if(leftPoint <= perto ):
        thread = Thread(target = correctHardDirection,args=(50))
        thread.start()
        thread.join()
    elif(rightPoint <= perto):
        thread = Thread(target = correctHardDirection,args=(-50))
        thread.start()
        thread.join()
    else:
        global lastLeftPoint, lastRightPoint, rightPoint, leftPoint
        if(lastLeftPoint - leftPoint > 0.20 AND rightPoint - lastRightPoint > 0.20)
            steer+=10
        elif(leftPoint - lastLeftPoint > 0.20 AND lastRightPoint - rightPoint > 0.20)
            steer-=10
        lastRightPoint = rightPoint
        lastLeftPoint = leftPoint

def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

def callback(data):
    global pointDirection,frontPoint,backPoint,rightPoint,leftPoint
    commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
    pointDirection = str(data.data).split('$')
    frontPoint = pointDirection[0]
    backPoint = pointDirection[1]
    rightPoint = pointDirection[2]
    leftPoint = pointDirection[3]
    if(move()):
        correctDirection()
    commandToPublish = "5*speed$" + speed + "*steer$" + steer + "*limit$" + limit + "*powerA$0*powerB$0*pulverize$0"
    pubControlCommand(commandToPublish)
    

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)