import time
class Relay:
    
    def __init__(self,enableRelays):
        self.relayOne = 38
        self.relayTwo = 40
        self.relayThree = 35
        self.relayFour = 37
        self.enableRelays = enableRelays
        
    def sendSignalToBoardOne(self,signal):
        if(self.enableRelays == True and signal == 1):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(38, GPIO.OUT)
            GPIO.output(38, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(38, GPIO.LOW)
            time.sleep(0.2)
        elif(self.enableRelays == True):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(38, GPIO.OUT)
            GPIO.output(38, GPIO.LOW)
    
    def sendSignalToBoardTwo(self,signal):
        if(self.enableRelays == True and signal == 1):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(40, GPIO.OUT)
            GPIO.output(40, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(40, GPIO.LOW)
            time.sleep(0.2)
        elif(self.enableRelays == True):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(40, GPIO.OUT)
            GPIO.output(40, GPIO.LOW)
    
    def sendSignalToPulverizer(self,signal):
        if(self.enableRelays == True and signal == 1):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(35, GPIO.OUT)
            GPIO.output(35, GPIO.HIGH)
            time.sleep(0.2)
        elif(self.enableRelays == True):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(35, GPIO.OUT)
            GPIO.output(35, GPIO.LOW)