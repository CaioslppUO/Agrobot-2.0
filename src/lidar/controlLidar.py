#!/usr/bin/env python3

import time
from threading import Thread
import rospy
from std_msgs.msg import String
import json

speed = 0
steer = 0
tick = 0

correctdir = "None"
leftArea = "None"
rightArea = "None"

def readJson():
    with open('parameters.json','r') as file:
        return json.load(file)


def move():
    global leftArea,rightArea,dataDefault,speed    
    if( rightArea == "free" or leftArea == "free"):
        speed = dataDefault['speedDefault']
        print(speed) 
        return True
    else:
        speed = 0
        return False

def correctDirA():
    global correctdir,tick,steer,dataDefault
    if(tick == 1):
        steer = dataDefault['steerDefault']
    elif(correctdir == "right"):
        steer = int(dataDefault['steerDefault']) - int(dataDefault['shiftDirection'])
    else:
        steer = int(dataDefault['steerDefault']) + int(dataDefault['shiftDirection'])
    tick = int(tick) - 1
    
def correctDirection():
    global leftArea,rightArea,tick,correctdir,dataDefault
    if(leftArea == "busy"):
        tick = int(dataDefault['tickDefault'])
        correctdir = "right"
    if(rightArea == "busy"):
        tick = (dataDefault['tickDefault'])
        correctdir = "left"


def checkAuto():
    global dataDefault
    if(dataDefault['limit'] == 0 and dataDefault['tickDefault'] == 0 and dataDefault['steerDefault'] == 0 and dataDefault['speedDefault'] == 0 and dataDefault['shiftDirection'] == 0 ):
        return False
    return True


def readFile(data):
    global dataDefault
    dataDefault = readJson()


def callback(data):
    global tick,dataDefault,leftArea,rightArea
    if(checkAuto()):
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

        subb = rospy.Subscriber('/writeFile', String, readFile)
            


def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
dataDefault = readJson()
main()
