#!/usr/bin/python

from complements.Sensors import Sensor
import serial
import time

UART0 = 0
UART1 = 0

def setUarts(amount):
    if(amount == 1): 
        #Setting UART 0
        global UART0;
        global UART1;
        UART0 = serial.Serial(
            port='/dev/ttyUSB_CONVERSOR-0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
    elif(amount == 2):
        #Setting UART 0
        global UART0;
        global UART1;
        UART0 = serial.Serial(
            port='/dev/ttyUSB_CONVERSOR-0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        #Setting UART 1
        UART1 = serial.Serial(
            port='/dev/ttyUSB_CONVERSOR-1',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

class Movement:
    def __init__(self, enableSensors, enableUart):
        self.speed = '0000'
        self.steer = '0000'
        self.limit = '0000'
        self.enableSensors = enableSensors #Change to enable or disable the sensors
        self.enableUart = enableUart #Change to enable or disable uart communication
        if(self.enableUart == True):
            setUarts(2)
        self.sensor = Sensor(enableSensors)
        
    #Recieve a numeric value and change it to Integer
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
        
    def setValues(self, speed, steer, limit):
        self.speed = self.getValue(speed)
        self.steer = self.getValue(steer)
        self.limit = self.getValue(limit)

    #Send the commands to the arduino, using UART protocol
    def move(self):
        if(self.enableSensors == True and self.sensor.frontCollision() or self.sensor.leftCollision() or self.sensor.rightCollision()):
            texto = '0000,0000,0000;'
            if(self.enableUart == True):
                UART0.write(str.encode(texto))
                UART1.write(str.encode(texto))
            time.sleep(0.02)
        else:
            texto = self.speed
            texto += ','
            texto += self.steer
            texto += ','
            texto += self.limit
            texto += ';'
            if(self.enableUart == True):
                UART0.write(str.encode(texto))
                UART1.write(str.encode(texto))
            time.sleep(0.02)
    
    