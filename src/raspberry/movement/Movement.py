#####################
#----> Imports <----#
#####################

import time

from complements.Sensors import Sensor
from complements.Checks import Checks

##############################
#----> Global Variables <----#
##############################

UART0 = 0
UART1 = 0

#######################
#----> Functions <----#
#######################

#Define the amount the wich uarts connections will be used
def setUarts(amount):
    global UART0
    global UART1
    if(amount == 1): 
        import serial
        #Setting UART 0
        try:
            UART0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            UART0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-1',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

    elif(amount == 2):
        import serial
        try:
            #Setting UART 0
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
        except:
            try:
                #Setting UART 0
                UART0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
            except:
                try:
                    #Setting UART 1
                    UART1 = serial.Serial(
                    port='/dev/ttyUSB_CONVERSOR-1',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )
                except:
                    print("Unable to set uart comunication")

############################
#----> Movement Class <----#
############################

class Movement:
    def __init__(self, enableSensors, enableUart, uartAmount):
        self.speed = '0000'
        self.steer = '0000'
        self.limit = '0000'
        self.enableSensors = enableSensors
        self.enableUart = enableUart
        self.uartAmount = uartAmount
        if(self.enableUart == True):
            try:
                setUarts(self.uartAmount)
            except:
                print("Unable to set uarts. Running the program without uart comunication.")
                self.enableUart = False
                self.uartAmount = 0
                time.sleep(3)
        self.sensor = Sensor(enableSensors)
        self.check = Checks()
        
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
        
    #Define the values of speed, steer and limit in the board
    def setValues(self, speed, steer, limit):
        speed = self.check.checkSpeed(speed)
        steer = self.check.checkSteer(steer)
        limit = self.check.checkLimit(limit)

        self.speed = self.getValue(speed)
        self.steer = self.getValue(steer)
        self.limit = self.getValue(limit)

    #Send the commands to the arduino, using UART protocol
    def move(self):
        if(self.enableSensors == True and self.sensor.frontCollision() or self.sensor.leftCollision() or self.sensor.rightCollision()):
            texto = '0000,0000,0000;'
            if(self.enableUart == True):
                import serial
                if(self.uartAmount == 1):  
                    UART0.write(str.encode(texto))
                elif(self.uartAmount == 2):
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
                import serial
                if(self.uartAmount == 1):  
                    UART0.write(str.encode(texto))
                elif(self.uartAmount == 2):
                    UART0.write(str.encode(texto))
                    UART1.write(str.encode(texto))
            time.sleep(0.02)
    
    