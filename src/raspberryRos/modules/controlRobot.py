#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import time
import serial
import sys
import rospy

from std_msgs.msg import String

################################
#----> Global Definitions <----#
################################

rospy.init_node('ControlRobot', anonymous=True) 

##############################
#----> Global Variables <----#
##############################

uart0 = None
uart1 = None

#######################
#----> Functions <----#
#######################

#Define the amount of uarts that will be used and reserve the USB port for them
def setUart(uartAmount):
    global uart0,uart1
    if(uartAmount == 1):
        try:
            uart0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            uart0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-1',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
    elif(uartAmount == 2):
        try:
            uart0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

            uart1 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-1',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            pass

#Check and correct the speed value if it is needed
def checkSpeed(speed):
    if(speed < -100):
        return -100
    if(speed > 100):
        return 100
    return speed

#Check and correct the steer value if it is needed
def checkSteer(steer):
    if(steer < -100):
        return -100
    if(steer > 100):
        return 100
    return steer

#Check and correct the limit value if it is needed
def checkLimit(limit):
    if(limit < 0):
        return 0
    if(limit > 100):
        return 100
    return limit

#################################
#----> Control Robot Class <----#
#################################

class ControlRobot():
    def __init__(self):
        self.speed = "0000"
        self.steer = "0000"
        self.limit = "0000"

        try:
            self.uartAmount = sys.argv[1]
        except:
            self.uartAmount = 0
        try:
            setUart(int(self.uartAmount))
        except:
            pass

    #Recieve a numeric value and change it to String to the format: signal (value value value)
    def getValue(self, v):
        if(v >= 0):
            r = '1'
        else:
            r = '0'
        if(v < 10 and v > -10):
            r += '00'
        elif(v < 100 and v > -100):
            r += '0'
        r += str(abs(v))
        return r

    #Define the values needed to control the robot
    def setValues(self,speed,steer,limit):
        spdCk = checkSpeed(speed)
        strCk = checkSteer(steer)
        lmtCk = checkLimit(limit)

        self.speed = self.getValue(spdCk)
        self.steer = self.getValue(strCk)
        self.limit = self.getValue(lmtCk)

    #Send the values from speed,steer and limit to the arduino
    def callbackSetValues(self,data):
        global uart0,uart1
        cbAux = str(data.data).split(":")
        
        try:
            self.setValues(int(cbAux[0]),int(cbAux[1]),int(cbAux[2]))
        except:
            self.speed = 0
            self.steer = 0
            self.limit = 0

        text = self.speed
        text += ','
        text += self.steer
        text += ','
        text += self.limit
        text += ';'

        try:
            if(int(self.uartAmount) == 1):  
                uart0.write(str.encode(text))
                self.pub.publish("Command send to arduino: " + str(text) + " Using " + str(self.uartAmount) + " Uarts")
            elif(int(self.uartAmount) == 2):
                uart0.write(str.encode(text))
                uart1.write(str.encode(text))
            else:
                self.pub.publish("Command send to arduino: None, Using " + str(self.uartAmount) + " Uarts")
            time.sleep(0.02)
        except:
            pass
        
    #Listen the ControlRobot topic
    def listenValues(self):
        rospy.Subscriber("ControlRobot", String, self.callbackSetValues)   
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

if __name__ == '__main__':
    control = ControlRobot()
    control.listenValues()
