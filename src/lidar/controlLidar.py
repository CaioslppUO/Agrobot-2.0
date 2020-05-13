#!/usr/bin/env python3

import rospy
import time
from threading import Thread
from std_msgs.msg import String
import json

speed = 0
steer = 0
tick = 0

correctdir = "None"
leftArea = "None"
rightArea = "None"

def read_json():
    with open('params.json','r') as file:
        return json.load(file)


def move():
    global leftArea,rightArea,dataDefault
    if( rightArea == "free" or leftArea == "free"):
        speed = dataDefault['speedDefault']
        return True
    else:
        speed = 0
        return False

def correctDirA():
    global correctdir,tick,steer,dataDefault
    if(tick == 1):
        steer = dataDefault['steerDefault']
    elif(correctdir == "right"):
        steer = dataDefault['steerDefault'] + dataDefault['shiftDirection']
    else:
        steer = dataDefault['steerDefault'] - dataDefault['shiftDirection']
    tick = tick - 1
    
def correctDirection():
    global leftArea,rightArea,tick,correctdir,dataDefault
    if(leftArea == "busy"):
        tick = dataDefault['tickDefault']
        correctdir = "right"
    if(rightArea == "busy"):
        tick = dataDefault['tickDefault']
        correctdir = "left"

def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

def callback(data):
    global tick
    commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
    pointDirection = str(data.data).split('$')

    leftArea = pointDirection[0]
    rightArea = pointDirection[1]

    if(move()):
        if(tick == 0):
            correctDirection()
        else:
            correctDirA()

    commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(dataDefault['limit']) + "*powerA$0*powerB$0*pulverize$0"
    pubControlCommand.publish(commandToPublish)
    

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
dataDefault = read_json()
main()