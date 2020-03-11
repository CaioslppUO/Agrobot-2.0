#!/usr/bin/env python3

import numpy as np
import cv2
import rospy
from std_msgs.msg import String

msg = None
pub = rospy.Publisher('ComputationalVision', String, queue_size=10)
rospy.init_node('ComputationalVision', anonymous=True)

limit = 50
pulverize = 0
powerB = 0
powerA = 0
priority = 7

speed = 0
steer = 0

#prioridade 7
#priority*speed$val*steer$val*limit$val*powerA$0*powerB$0*pulverize$0
def DirectionValue(value):
	return value < 0
def Velocity(MaxValue,ActualValue):
	return MaxValue/ActualValue
def DeadArea(pt1,safe1,safe2):
	return (pt1[0] > safe1[0] and pt1[0] < safe2[0])

def AjustAngle(pt1,size):
	direction = False
	vel = 0
	direction = DirectionValue(pt1[0] - size)
	if(direction):
		steer = 100
	else:
		steer = -100
	if(direction):
		vel = Velocity(size-pt1[0],size)
	else:
		vel = Velocity(pt1[0]-size,size)
	speed = int((100*vel)/0.5)

#priority*speed$val*steer$val*limit$val*powerA$0*powerB$0*pulverize$0
	msg = "{:0}*speed${:1}*steer${:2}*limit${:4}*powerA${:5}*powerB${:6}*pulverize${:7}".format(priority,speed,steer,limit,powerA,powerB,pulverize)
	pub.Publisher(msg)
	msg = None
	# print(direction)
	# print(vel)


def enableVision():
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	FaceCenterX = 0
	FaceCenterY = 0
	while(True):
		_, frame = cv2.VideoCapture(0).read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		(ScrenCenterX,ScrenCenterY) = ( frame.shape[1] // 2, frame.shape[0] // 2 )#Pega o centro da tela
		# cv2.circle(frame,(ScrenCenterX,ScrenCenterY) , 2 , (0,0,255),2 )#Desenha um circulo no centro da tela
		# cv2.rectangle(frame,(ScrenCenterX-80,ScrenCenterY-80),(ScrenCenterX+80,ScrenCenterY+80),(255,0,0),2)#Desenha um retangulo na area morta
		for (x,y,w,h) in faces:
			(FaceCenterX,FaceCenterY) = (( x+w // 2 ),( y+h // 2)) #Pega o valor do ponto central do rosto
			# cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #Desenha um retangulo no rosto
			# cv2.circle(frame,(FaceCenterX,FaceCenterY),2,(255,255,0),2)#Desenha um circulo no centro do rosto
			# cv2.line(frame,(FaceCenterX,FaceCenterY),(ScrenCenterX,ScrenCenterY), (255,0,0) )#Desenha uma linha do centro do rosto ao centro da tela
		if(not (DeadArea((FaceCenterX,FaceCenterY),(ScrenCenterX-80,ScrenCenterY-80),(ScrenCenterX+80,ScrenCenterY+80)))):
			AjustAngle((FaceCenterX,FaceCenterY),ScrenCenterX)
		# cv2.imshow('frame',frame)
		key = cv2.waitKey(10)
		if key == 27:
			break        
	cap.release()
	cv2.destroyAllWindows()

enableVision()