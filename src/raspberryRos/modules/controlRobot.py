#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import time
import serial
import sys
import rospy

from std_msgs.msg import String

##############################
#----> Global Variables <----#
##############################

uart0 = None
uart1 = None

#######################
#----> Functions <----#
#######################

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
                uart1 = serial.Serial(
                    port='/dev/ttyUSB_CONVERSOR-0',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                )

###########################
#----> Verifications <----#
###########################

def checkSpeed(speed):
    if(speed < -100):
        return -100,"Speed is below -100. Automatically capped at -100."
    if(speed < 100):
        return 100,"Speed is over 100. Automatically capped at 100."
    return speed,None

def checkSteer(steer):
    if(steer < -100):
        return -100,"Steer is below -100. Automatically capped at -100."
    if(steer > 100):
        return 100,"Speed is over 100. Automatically capped at 100."
    return steer,None

def checkLimit(limit):
    if(limit < 0):
        return 0,"Limit is below 0. Automatically capped at 0."
    if(limit > 100):
        return 100,"Limit is over 100. Automatically capped at 100."
    return limit,None

#################################
#----> Control Robot Class <----#
#################################

class ControlRobot():
    def __init__(self):
        self.speed = "0000"
        self.steer = "0000"
        self.limit = "0000"
        self.uartAmount = sys.argv[1]
        self.pub = rospy.Publisher('LogControlRobot', String, queue_size=10)
        
        try:
            setUart(int(self.uartAmount))
        except:
            self.pub.publish("[ERROR] Cant Set Uarts.")

    #Recieve a numeric value and change it to String
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
        spdCk,spdCkMsg = checkSpeed(speed)
        strCk,strCkMsg = checkSteer(steer)
        lmtCk,lmtCkMsg = checkLimit(limit)
    
        if(spdCkMsg != None):
            self.pub.publish(str(spdCkMsg))

        if(strCkMsg != None):
            self.pub.publish(str(strCkMsg))

        if(lmtCkMsg != None):
            self.pub.publish(str(lmtCkMsg))

        self.speed = self.getValue(spdCk)
        self.steer = self.getValue(strCk)
        self.limit = self.getValue(lmtCk)

    #Send the values from speed,steer and limit to the arduino
    def callbackSetValues(self,data):
        cbAux = str(data.data).split(":")
        self.setValues(int(cbAux[0]),int(cbAux[1]),int(cbAux[2]))
        global uart0,uart1
        text = self.speed
        text += ','
        text += self.steer
        text += ','
        text += self.limit
        text += ';'
        try:
            if(int(self.uartAmount) == 1):  
                uart0.write(str.encode(text))
            elif(int(self.uartAmount) == 2):
                uart0.write(str.encode(text))
                uart1.write(str.encode(text))
            time.sleep(0.02)
            self.pub.publish("Command send to arduino: " + str(text) + " Using " + str(self.uartAmount) + " Uarts")
        except:
            self.pub.publish("[ERROR] Cant send commands via UART. Uart Amount: " + str(self.uartAmount))

    #Listen the ControlRobot topic
    def listenValues(self):
        rospy.init_node('ControlRobot', anonymous=True) 
        rospy.Subscriber("ControlRobot", String, self.callbackSetValues)   
        rospy.spin()

#######################
#----> Main Loop <----#
#######################

if __name__ == '__main__':
    control = ControlRobot()
    control.listenValues()