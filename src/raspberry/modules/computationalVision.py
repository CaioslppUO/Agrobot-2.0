#!/usr/bin/env python3

import numpy as np
import cv2
import rospy
from std_msgs.msg import String

##Declaração do nó ComputationalVision
pub = rospy.Publisher('ComputationalVision', String, queue_size=10)
pubLog = rospy.Publisher('Log', String, queue_size=10)
rospy.init_node('ComputationalVision', anonymous=True)


##Variavel que armazena o limite do robô
limit = 50
##Variavel que armazena a velocidade do robô
speed = 0
##Variavel que armazena a direção do robô
steer = 0


##Função que verifica o valor da direção
#Retorna verdadeiro caso for esquerda, e falso caso for direita
def DirectionValue(value):
	return value < 0

##Função que retorna a velocidade que o robô deve ter com base no que tem na tela
def Velocity(MaxValue,ActualValue):
	return MaxValue/ActualValue

##Função que verifica se o rosto ja esta na area central
#Retorana verdadeiro se estiver, e false caso contrario
def DeadArea(pt1,safe1,safe2):
	return (pt1[0] > safe1[0] and pt1[0] < safe2[0])

##Função que manipula a direção do robô com base no rosto da pessoa
def AjustAngle(pt1,size):
	global speed,steer, limit
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

	msg = "5*speed$"+str(speed)+"*steer$"+str(steer)+"*limit$"+str(limit)+"*powerA$0*powerB$0*pulverize$0"
	pub.Publisher(msg)
	msg = None

##Função que detecta o rosto da pessoa, e o centro da tela
def enableVision():
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	FaceCenterX = 0
	FaceCenterY = 0
	while(True):
		_, frame = cv2.VideoCapture(0).read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		#Pega o centro da tela
		(ScrenCenterX,ScrenCenterY) = ( frame.shape[1] // 2, frame.shape[0] // 2 )
		# cv2.circle(frame,(ScrenCenterX,ScrenCenterY) , 2 , (0,0,255),2 )#Desenha um circulo no centro da tela
		# cv2.rectangle(frame,(ScrenCenterX-80,ScrenCenterY-80),(ScrenCenterX+80,ScrenCenterY+80),(255,0,0),2)#Desenha um retangulo na area morta
		for (x,y,w,h) in faces:
			#Pega o valor do ponto central do rosto
			(FaceCenterX,FaceCenterY) = (( x+w // 2 ),( y+h // 2)) 
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

pubLog('startedFile$ComputationalVision')
enableVision()