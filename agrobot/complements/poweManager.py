#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#GPIO.setup(40, GPIO.OUT)
#GPIO.setup(38, GPIO.OUT)


class Power:
    def __init__(self,powerBoardA,powerBoardB):
        self.boardA = 40
        self.boardB = 38
        self.powerBoardA = powerBoardA
        self.powerBoardB = powerBoardB
        