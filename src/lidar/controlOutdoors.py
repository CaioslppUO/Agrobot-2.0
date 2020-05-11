#!/usr/bin/env python3

import rospy
from threading import Thread
from std_msgs.msg import String

#Variáveis de controle do robô
speed = "50"
limit = "100"
steer = "0"

#Distancias em metro
close = 0.5
medium = 1.5
far = 7.0

def moveFowardRule(frontDist):
    global medium
    return frontDist > medium and frontDist < far

def turnRightRule(frontDist,rightDist):
    global medium,far
    return frontDist <= medium and rightDist > medium and rightDist < far

def turnLeftRule(frontDist,leftDist):
    global medium,far
    return frontDist <= medium and leftDist > medium and leftDist < far

def move(frontDist,backDist,leftDist,rightDist):
    global close,medium,far,speed,steer,limit,pubControlCommand
    commandToPublish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
    stringToPublish = ""
    if(moveFowardRule(frontDist)):
        speed = "50"
        steer = "0"
        commandToPublish = "5*speed$" + speed + "*steer$" + steer + "*limit$" + limit + "*powerA$0*powerB$0*pulverize$0"
        stringToPublish = "Go Foward"
    elif(turnLeftRule(frontDist,leftDist)):
        speed = "0"
        steer = "-25"
        commandToPublish = "5*speed$" + speed + "*steer$" + steer + "*limit$" + limit + "*powerA$0*powerB$0*pulverize$0"
        stringToPublish = "Turn Left"
    elif(turnRightRule(frontDist,rightDist)):
        speed = "0"
        steer = "25"
        commandToPublish = "5*speed$" + speed + "*steer$" + steer + "*limit$" + limit + "*powerA$0*powerB$0*pulverize$0"
        stringToPublish = "Turn Right"
    else:
        speed = "0"
        steer = "0"
        commandToPublish = "5*speed$" + speed + "*steer$" + steer + "*limit$" + limit + "*powerA$0*powerB$0*pulverize$0"
        stringToPublish = "Stop"

    pubControlCommand.publish(commandToPublish)
    pubHumanReadableString.publish(stringToPublish)

def callback(msg):
    distances = str(msg.data).split("$")
    frontDist = float(distances[0])
    backDist = float(distances[1])
    leftDist = float(distances[2])
    rightDist = float(distances[3])
    move(frontDist,backDist,leftDist,rightDist)

rospy.init_node('controlOutdoors', anonymous=True)
pubControlCommand = rospy.Publisher("ControlOutdoors", String,queue_size=10)
pubHumanReadableString = rospy.Publisher("ControlOutdoorHumanReadable", String, queue_size=10)
sub = rospy.Subscriber('/Lidar', String, callback)
rospy.spin()