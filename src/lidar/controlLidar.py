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
centerArea = "None"

def readJson():
    with open('parameters.json','r') as file:
        return json.load(file)

def setSpeed(speednew):
    global speed
    speed = speednew

def setSteer(steernew):
    global steer
    steer = steernew

def checkTick():
    global tick
    if(tick == 0):
        setCorrection()
    else:
        correctDirection()
    

def checkFoward():
    global dataDefault,speed,centerArea 
    if( centerArea == "free"):
        setSpeed(dataDefault['speedDefault'])
        checkTick()
    else:
        setSteer(0)
        setSpeed(0)


def correctDirection():
    global correctdir,tick,steer,dataDefault
    if(tick == 1):
        setSteer(dataDefault['steerDefault'])
    elif(correctdir == "right"):
        setSteer(dataDefault['steerDefault'] - dataDefault['shiftDirection'])
    else:
        setSteer(dataDefault['steerDefault'] + dataDefault['shiftDirection'])
    tick = tick - 1
    
def setCorrection():
    global leftArea,rightArea,tick,correctdir,dataDefault
    if(leftArea == "busy"):
        tick = dataDefault['tickDefault']
        correctdir = "right"
    if(rightArea == "busy"):
        tick = dataDefault['tickDefault']
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
    global dataDefault,leftArea,rightArea,steer,centerArea
    if(checkAuto()):
        pointDirection = str(data.data).split('$')
        leftArea = pointDirection[0]
        centerArea = pointDirection[1]
        rightArea = pointDirection[2]

        checkFoward()
        commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(dataDefault['limit']) + "*powerA$0*powerB$0*pulverize$" + str(dataDefault['uv'])
        pubControlCommand.publish(commandToPublish)
        rospy.Subscriber('/writeFile', String, readFile)
            
def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
dataDefault = readJson()
main()
