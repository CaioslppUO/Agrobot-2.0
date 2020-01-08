from threading import Thread
import time

sensor_A_trig = 11
sensor_A_echo = 12

sensor_B_trig = 15
sensor_B_echo = 16

sensor_C_trig = 31
sensor_C_echo = 32

class Sensor:
    def __init__(self, enableSensors):
        self.enableSensors = enableSensors
        self.running = True
        self.distance_A          = 0
        self.distance_B          = 0
        self.distance_C          = 0
        self.distanceLimit       = 65
        self.adjustment          = 15
        self.sensorsCoefficiente = 0
        if(self.enableSensors == True):
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(sensor_A_trig, GPIO.OUT)
            GPIO.setup(sensor_A_echo, GPIO.IN)
            GPIO.setup(sensor_B_trig, GPIO.OUT)
            GPIO.setup(sensor_B_echo, GPIO.IN)
            GPIO.setup(sensor_C_trig, GPIO.OUT)
            GPIO.setup(sensor_C_echo, GPIO.IN)

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            self.read_sensors()

    def get_distance_a(self):
        return self.distance_A

    def get_distance_b(self):
        return self.distance_B

    def get_distance_c(self):
        return self.distance_C

    def read_sensors(self):
        self.read_sensor_a()
        self.read_sensor_b()
        self.read_sensor_c()

    def read_sensor_a(self):
        if(self.enableSensors == True):
            import RPi.GPIO as GPIO
            GPIO.output(sensor_A_trig, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(sensor_A_trig, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(sensor_A_trig, GPIO.LOW)
            while GPIO.input(sensor_A_echo) == 0:
                signaloff = time.time()
            while GPIO.input(sensor_A_echo) == 1:
                signalon = time.time()
            timepassed = signalon - signaloff
            distance = timepassed * 17000
            self.distance_A = distance

    def read_sensor_b(self):
        if(self.enableSensors == True):
            import RPi.GPIO as GPIO
            GPIO.output(sensor_B_trig, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(sensor_B_trig, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(sensor_B_trig, GPIO.LOW)
            while GPIO.input(sensor_B_echo) == 0:
                signaloff = time.time()
            while GPIO.input(sensor_B_echo) == 1:
                signalon = time.time()
            timepassed = signalon - signaloff
            distance = timepassed * 17000
            self.distance_B = distance

    def read_sensor_c(self):
        if(self.enableSensors == True):
            import RPi.GPIO as GPIO
            GPIO.output(sensor_C_trig, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(sensor_C_trig, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(sensor_C_trig, GPIO.LOW)
            while GPIO.input(sensor_C_echo) == 0:
                signaloff = time.time()
            while GPIO.input(sensor_C_echo) == 1:
                signalon = time.time()
            timepassed = signalon - signaloff
            distance = timepassed * 17000
            self.distance_C = distance

    #Detect front collision form distance sensor
    def frontCollision(self):
        if(self.enableSensors == True):
            self.read_sensors()
            global distanceLimit;
            if (self.distance_A <= (self.distanceLimit) * self.sensorsCoefficiente/100 and self.distance_B <= (self.distanceLimit) * self.sensorsCoefficiente/100 and self.distance_C <= (self.distanceLimit) * self.sensorsCoefficiente/100):
                return 1
            return 0
        else:
            return 0

    #Detect left collision form distance sensor
    def leftCollision(self):
        if(self.enableSensors == True):
            self.read_sensor_c()
            global distanceLimit;
            global adjustment;
            if (self.distance_C <= (self.distanceLimit+self.adjustment) * self.sensorsCoefficiente/100):
                return 1
            return 0
        else:
            return 0

    #Detect right collision form distance sensor
    def rightCollision(self):
        if(self.enableSensors == True):
            self.read_sensor_b()
            global distanceLimit;
            global adjustment;
            if (self.distance_B <= (self.distanceLimit+self.adjustment) * self.sensorsCoefficiente/100):
                return 1
            return 0
        else:
            return 0