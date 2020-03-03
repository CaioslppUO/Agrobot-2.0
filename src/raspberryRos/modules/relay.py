#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import time
import rospy
import RPi.GPIO as GPIO

from std_msgs.msg import String

################################
#----> Global Definitions <----#
################################

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#########################
#----> Relay Class <----#
#########################

class Relay():
    #Send the recieved signal to turn on/off to board one
    def sendSignalToBoardOne(self,signal):
        if(signal == 1):
            GPIO.setup(38, GPIO.OUT)
            GPIO.output(38, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(38, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(38, GPIO.OUT)
            GPIO.output(38, GPIO.LOW)

    #Send the recieved signal to turn on/off to board two
    def sendSignalToBoardTwo(self,signal):
        if(signal == 1):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(40, GPIO.OUT)
            GPIO.output(40, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(40, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(40, GPIO.OUT)
            GPIO.output(40, GPIO.LOW)
    
    #Send the recieved signal to turn on/off the pulverizer
    def sendSignalToPulverizer(self,signal):
        if(signal == 1):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(35, GPIO.OUT)
            GPIO.output(35, GPIO.HIGH)
            time.sleep(0.2)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(35, GPIO.OUT)
            GPIO.output(35, GPIO.LOW)

    #Decide wich relay need to be activated
    def callback(self,data):
        cbAux = str(data.data).split(":")
        if(cbAux[0] == "sendSignalToPulverizer"):
            self.sendSignalToPulverizer(int(cbAux[1]))
        elif(cbAux[0] == "sendSignalToBoardTwo"):
            self.sendSignalToBoardTwo(int(cbAux[1]))
        elif(cbAux[0] == "sendSignalToBoardOne"):
            self.sendSignalToBoardOne(int(cbAux[1]))
    
    #Listen to the relay topic
    def listener(self):
        rospy.init_node('Relay', anonymous=True) 
        rospy.Subscriber("Relay", String, self.callback)   
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

if __name__ == '__main__':
    relay = Relay()
    relay.listener()