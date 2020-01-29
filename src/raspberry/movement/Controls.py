#!/usr/bin/python

#####################
#----> Imports <----#
#####################

import time
from movement.Movement import Movement

############################
#----> Controls Class <----#
############################

class Controls:
    def __init__(self, enableSensors, enableUart):
        self.mv = Movement(enableSensors, enableUart)
        self.delay = 0.5
    
    def goFoward(self, speed):
        self.mv.setValues(speed,0,100)
        self.mv.move()
        time.sleep(self.delay)
    
    def goFoward(self):
        self.mv.setValues(25,0,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goBack(self, speed):
        self.mv.setValues(-speed,0,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goBack(self):
        self.mv.setValues(-25,0,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goRight(self, speed, rotationSpeed):
        self.mv.setValues(speed,rotationSpeed,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goRight(self):
        self.mv.setValues(0,25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goLeft(self, speed, rotationSpeed):
        self.mv.setValues(speed,-rotationSpeed,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goLeft(self):
        self.mv.setValues(0,-25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goFowardLeft(self, speed):
        self.mv.setValues(speed,-25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goFowardLeft(self):
        self.mv.setValues(25,-25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goFowardRight(self, speed):
        self.mv.setValues(speed,25,100)
        self.mv.move()
        time.sleep(self.delay)
    
    def goFowardRight(self):
        self.mv.setValues(25,25,100)
        self.mv.move()
        time.sleep(self.delay)
    
    def goBackLeft(self, speed):
        self.mv.setValues(-speed,-25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goBackLeft(self):
        self.mv.setValues(-25,-25,100)
        self.mv.move()
        time.sleep(self.delay)
    
    def goBackRight(self, speed):
        self.mv.setValues(-speed,25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def goBackRight(self):
        self.mv.setValues(-25,25,100)
        self.mv.move()
        time.sleep(self.delay)
        
    def stop(self):
        self.mv.setValues(0,0,0)
        self.mv.move()
        
    def rotate180Right(self):
        self.mv.setValues(0,53,100)
        self.mv.move()
        time.sleep(0.85)
        
    def rotate180Left(self):
        self.mv.setValues(0,-50,100)
        self.mv.move()
        time.sleep(1.1)
        
    def rotate360(self):
        self.mv.setValues(0,53,100)
        self.mv.move()
        time.sleep(1.7)
    
    def rotate(self, angle):
        self.mv.setValues(0,53,100)
        self.mv.move()
        if(angle < 15):
            time.sleep((angle/180)*3)
        elif(angle < 30):
            time.sleep((angle/180)*1.2)
        elif(angle < 120):
            time.sleep((angle/180)*0.87)
        else:
            time.sleep((angle/180)*0.85)
        
    def testInterface(self):
        while(True):
            self.stop()
            print('goFoward')
            print('goBack')
            print('goLeft')
            print('goRight')
            print('goFowardLeft')
            print('goFowardRight')
            print('goBackLeft')
            print('goBackRight')
            print('stop')
            print('rotate180Right')
            print('rotate180Left')
            print('rotate360')
            print('rotate')
            option = input('Digite o que quer fazer: ')
            
            if(option == 'goFoward'):
                self.goFoward()
            elif(option == 'goBack'):
                self.goBack()
            elif(option == 'goLeft'):
                self.goLeft()
            elif(option == 'goRight'):
                self.goRight()
            elif(option == 'goFowardLeft'):
                self.goFowardLeft()
            elif(option == 'goFowardRight'):
                self.goFowardRight()
            elif(option == 'goBackLeft'):
                self.goBackLeft()
            elif(option == 'goBackRight'):
                self.goBackRight()
            elif(option == 'stop'):
                self.stop()
            elif(option == 'rotate180Right'):
                self.rotate180Right()
            elif(option == 'rotate180Left'):
                self.rotate180Left()
            elif(option == 'rotate360'):
                self.rotate360()
            elif(option == 'rotate'):
                ang = int(input('Digite o angulo: '))
                self.rotate(ang)
            else:
                self.stop()