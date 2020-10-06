#!/usr/bin/env python3

"""
Módulo que gerencia o reconhecimento facial.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação no tópico computational_vision.
const_pub_computational_vision = rospy.Publisher('computational_vision', String, queue_size=10)
## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)
## Constante que define o limite de velocidade para no robô.
const_limit = 50

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó computational_vision.
rospy.init_node('computational_vision', anonymous=True)

# -------------------------- #
# -> Imports Condicionais <- #
# -------------------------- #

try:
	import numpy as np
except:
	const_pub_log.publish("error$Warning$Could not import numpy as np in raspberry/modules/computationalVision.py")
try: 
	import cv2
except:
	const_pub_log.publish("error$Warning$Could not import cv2 in raspberry/modules/computationalVision.py")

# ------------- #
# -> Funções <- #
# ------------- #

## Função que verifica o valor da direção.
def check_direction_value(value):
	return value < 0

## Função que retorna a velocidade que o robô deve ter com base na tela.
def calc_velocity(max_value,actual_value):
	return max_value/actual_value

## Função que verifica se o rosto ja esta na area central da tela.
def check_dead_area(pt1,safe1,safe2):
	return (pt1[0] > safe1[0] and pt1[0] < safe2[0])

## Função que manipula a direção do robô com base no rosto da pessoa.
def ajust_angle(pt1,size,limit):
	direction = False
	vel = 0
	direction = check_direction_value(pt1[0] - size)
	if(direction):
		steer = 100
	else:
		steer = -100
	if(direction):
		vel = calc_velocity(size-pt1[0],size)
	else:
		vel = calc_velocity(pt1[0]-size,size)
	speed = int((100*vel)/0.5)

	msg = "5*speed$"+str(speed)+"*steer$"+str(steer)+"*limit$"+str(limit)+"*powerA$0*powerB$0*pulverize$0"
	try:
		const_pub_computational_vision.publish(msg)
	except:
		const_pub_log.publish("error$Warning$Could not publish ajust_angle msg in raspberry/modules/computationalVision.py")
	msg = None

## Função que detecta o rosto da pessoa e o centro da tela.
def enable_vision():
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	face_center_x = 0
	face_center_y = 0
	while(True):
		_, frame = cv2.VideoCapture(0).read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		# Pega o centro da tela.
		(scren_center_x,scren_center_y) = ( frame.shape[1] // 2, frame.shape[0] // 2 )
		# cv2.circle(frame,(scren_center_x,scren_center_y) , 2 , (0,0,255),2 ) #Desenha um circulo no centro da tela .
		# cv2.rectangle(frame,(scren_center_x-80,scren_center_y-80),(scren_center_x+80,scren_center_y+80),(255,0,0),2) #Desenha um retangulo na area morta.
		for (x,y,w,h) in faces:
			#Pega o valor do ponto central do rosto.
			(face_center_x,face_center_y) = (( x+w // 2 ),( y+h // 2)) 
			# cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #Desenha um retangulo no rosto.
			# cv2.circle(frame,(face_center_x,face_center_y),2,(255,255,0),2) #Desenha um circulo no centro do rosto.
			# cv2.line(frame,(face_center_x,face_center_y),(scren_center_x,scren_center_y), (255,0,0) ) #Desenha uma linha do centro do rosto ao centro da tela.
		if(not (check_dead_area((face_center_x,face_center_y),(scren_center_x-80,scren_center_y-80),(scren_center_x+80,scren_center_y+80)))):
			ajust_angle((face_center_x,face_center_y),scren_center_x,const_limit)
		# cv2.imshow('frame',frame)
		key = cv2.waitKey(10)
		if key == 27:
			break    
	try:
		cap.release()
	except:
		const_pub_log.publish("error$Warning$cap variable doesn't exist in raspberry/modules/computationalVision.py")
	cv2.destroyAllWindows()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

try:
	const_pub_log.publish('startedFile$ComputationalVision.py')
	enable_vision()
except:
	const_pub_log.publish('error$Fatal$Could not run computationalVision.py')