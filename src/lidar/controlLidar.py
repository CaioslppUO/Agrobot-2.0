#!/usr/bin/env python3

import rospy
import time
from threading import Thread
from std_msgs.msg import String

speed = 0
limit = 50
steer = 0
tick = 0

tickDefault = 3
steerDefault = -3
speedDefault = -26
shiftDirection = 5
correctdir = "None"
leftArea = "None"
rightArea = "None"

def move():
    global speedDefault,leftArea,rightArea
    if( rightArea == "free" or leftArea == "free"):
        speed = speedDefault
        return True
    else:
        speed = 0
        return False

def correctDirA():
    global correctdir,tick,steer,shiftDirection
    if(tick == 1):
        steer = steerDefault
    elif(correctdir == "right"):
        steer = steerDefault + shiftDirection
    else:
        steer = steerDefault - shiftDirection
    tick = tick - 1
    
def correctDirection():
    global leftArea,rightArea,tick,tickDefault,correctdir
    if(leftArea == "busy"):
        tick = tickDefault
        correctdir = "right"
    if(rightPoint < perto):
        tick = tickDefault
        correctdir = "left"

def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

def callback(data):
    global tick
    commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
    pointDirection = str(data.data).split('$')

    leftArea = float(pointDirection[0])
    rightArea = float(pointDirection[1])

    if(move()):
        if(tick == 0):
            correctDirection()
        else:
            correctDirA()

    commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(limit) + "*powerA$0*powerB$0*pulverize$0"
    pubControlCommand.publish(commandToPublish)
    

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
main()