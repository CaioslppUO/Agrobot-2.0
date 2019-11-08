#!/usr/bin/python

import time
import serial
from complements.Sensors import Sensor

#Setting UART 0
#UART0 = serial.Serial(
#     port='/dev/ttyUSB0',
#     baudrate = 9600,
#     parity=serial.PARITY_NONE,
#        stopbits=serial.STOPBITS_ONE,
#        bytesize=serial.EIGHTBITS,
#        timeout=1
#)

#Setting UART 1
#UART1 = serial.Serial(
#     port='/dev/ttyUSB1',
#     baudrate = 9600,
#     parity=serial.PARITY_NONE,
#        stopbits=serial.STOPBITS_ONE,
#        bytesize=serial.EIGHTBITS,
#        timeout=1
#)

class Movement:
    def __init(self):
        self.speed = '0000'
        self.steer = '0000'
        self.limit = '0000'
        self.sensor = Sensor()
        
    #Recieve a numeric value and change it to Integer
    def getValue(self,v):
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
        
    def setValues(self,speed,steer,limit):
        self.speed = self.getValue(speed)
        self.steer = self.getValue(steer)
        self.limit = self.getValue(limit)

    #Send the commands to the arduino, using UART protocol
    def move(self):
        #if(self.sensor.frontCollision() or self.sensor.leftCollision() or self.sensor.rightCollision()):
        if (False):
            texto = '0000,0000,0000;'
            #UART0.write(str.encode(texto))
            #UART1.write(str.encode(texto))
            time.sleep(0.02)
        else:
            texto = self.speed
            texto += ','
            texto += self.steer
            texto += ','
            texto += self.limit
            texto += ';'
            #UART0.write(str.encode(texto))
            #UART1.write(str.encode(texto))
            time.sleep(0.02)
    
    