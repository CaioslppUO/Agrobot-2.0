#!/usr/bin/env python3

import time
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
walk = True

def readJson():
    with open('parameters.json','r') as file:
        return json.load(file)

def setSpeed(speednew):
    global speed
    speed = int(speednew)

def setSteer(steernew):
    global steer
    steer = int(steernew)

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
        setSteer(int(dataDefault['steerDefault']) - int(dataDefault['shiftDirection']))
    else:
        setSteer(int(dataDefault['steerDefault']) + int(dataDefault['shiftDirection']))
    tick = int(tick) - 1
    
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
    if(int(dataDefault['limit']) == 0 and int(dataDefault['tickDefault']) == 0 and int(dataDefault['steerDefault']) == 0 and int(dataDefault['speedDefault']) == 0 and int(dataDefault['shiftDirection']) == 0 ):
        return False
    return True

def readFile(data):
    global dataDefault
    dataDefault = readJson()

def setWalk(data):
    global walk
    if(data.data == 'walk'):
        walk = True
    else:
        walk = False

def callback(data):
    global dataDefault,leftArea,rightArea,steer,centerArea,walk
    rospy.Subscriber('/Walk', String, SetWalk)
    if(walk):
        if(checkAuto()):
            pointDirection = str(data.data).split('$')
            leftArea = pointDirection[0]
            centerArea = pointDirection[1]
            rightArea = pointDirection[2]

            checkFoward()
            commandToPublish = "5*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(dataDefault['limit']) + "*powerA$0*powerB$0*pulverize$" + str(dataDefault['uv'])
            pubControlCommand.publish(commandToPublish)
            rospy.Subscriber('/writeFile', String, readFile)
        else:
            commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
            pubControlCommand.publish(commandToPublish)
            rospy.Subscriber('/writeFile', String, readFile)
    else:
        commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$" + str(dataDefault['uv'])
        pubControlCommand.publish(commandToPublish)
        rospy.Subscriber('/writeFile', String, readFile)


            
def main():
    sub = rospy.Subscriber('/Lidar', String, callback)
    rospy.spin()

rospy.init_node('ControlLidar', anonymous=True)
pubControlCommand = rospy.Publisher("ControlLidar", String,queue_size=10)
dataDefault = readJson()
main()
