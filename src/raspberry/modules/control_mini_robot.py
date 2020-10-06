#!/usr/bin/env python3

"""
Módulo que gerencia o controle do robô de testes.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,sys,rospy,RPi.GPIO as gpio
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)
## Constante do pino no qual a primeira roda da frente está ligada.
const_left_wheel_1 = 16
## Constante do pino no qual a segunda roda da frente está ligada.
const_left_wheel_2 = 13
## Constante do pino no qual a primeira roda de trás está ligada.
const_right_wheel_1 = 18
## Constante do pino no qual a segunda roda de trás está ligada.
const_right_wheel_2 = 15

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó control_robot.
rospy.init_node('control_mini_robot', anonymous=True) 

# Configurando o GPIO
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(const_left_wheel_1, gpio.OUT)
gpio.setup(const_left_wheel_2, gpio.OUT)
gpio.setup(const_right_wheel_1, gpio.OUT)
gpio.setup(const_right_wheel_2, gpio.OUT)

# Configurando o PWM
const_left_wheel_1_pwm = gpio.PWM(const_left_wheel_1, 100)
const_left_wheel_2_pwm = gpio.PWM(const_left_wheel_2, 100)
const_right_wheel_1_pwm = gpio.PWM(const_right_wheel_1, 100)
const_right_wheel_2_pwm = gpio.PWM(const_right_wheel_2, 100)

const_left_wheel_1_pwm.start(0)
const_left_wheel_2_pwm.start(0)
const_right_wheel_1_pwm.start(0)
const_right_wheel_2_pwm.start(0)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência a comunicação com os arduinos.
class Control_mini_robot():
    def __init__(self):
        ## Variável utilizada controlar o movimento para frente e para trás.
        self.movement = "forward"
        ## Variável utilizada controlar o movimento para esquerda e para direita.
        self.direction = "none"
        ## Variável utilizada controlar o limite de velocidade.
        self.limit = 100

    ## Movimenta o robô para frente.
    def go_forward(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(0)
        const_left_wheel_2_pwm.ChangeDutyCycle(0)
        const_right_wheel_1_pwm.ChangeDutyCycle(self.limit)
        const_right_wheel_2_pwm.ChangeDutyCycle(self.limit)

    ## Movimenta o robô para trás.
    def go_back(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(self.limit)
        const_left_wheel_2_pwm.ChangeDutyCycle(self.limit)
        const_right_wheel_1_pwm.ChangeDutyCycle(0)
        const_right_wheel_2_pwm.ChangeDutyCycle(0)
    
    ## Movimenta o robô para frente e esquerda.
    def turn_left_forward(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(0)
        const_left_wheel_2_pwm.ChangeDutyCycle(0)
        const_right_wheel_1_pwm.ChangeDutyCycle(self.limit)
        const_right_wheel_2_pwm.ChangeDutyCycle(0)

    ## Movimenta o robô para frente e direita.
    def turn_right_forward(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(0)
        const_left_wheel_2_pwm.ChangeDutyCycle(0)
        const_right_wheel_1_pwm.ChangeDutyCycle(0)
        const_right_wheel_2_pwm.ChangeDutyCycle(self.limit)

    ## Movimenta o robô para trás e esquerda.
    def turn_left_back(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(self.limit)
        const_left_wheel_2_pwm.ChangeDutyCycle(0)
        const_right_wheel_1_pwm.ChangeDutyCycle(0)
        const_right_wheel_2_pwm.ChangeDutyCycle(0)

    ## Movimenta o robô para trás e direita.
    def turn_right_back(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(0)
        const_left_wheel_2_pwm.ChangeDutyCycle(self.limit)
        const_right_wheel_1_pwm.ChangeDutyCycle(0)
        const_right_wheel_2_pwm.ChangeDutyCycle(0)

    ## Para o robô.
    def stop(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(0)
        const_left_wheel_2_pwm.ChangeDutyCycle(0)
        const_right_wheel_1_pwm.ChangeDutyCycle(0)
        const_right_wheel_2_pwm.ChangeDutyCycle(0)

    ## Movimenta o robô para a esquerda.
    def turn_all_left(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(0)
        const_left_wheel_2_pwm.ChangeDutyCycle(self.limit)
        const_right_wheel_1_pwm.ChangeDutyCycle(self.limit)
        const_right_wheel_2_pwm.ChangeDutyCycle(0)

    ## Movimenta o robô para a direita.
    def turn_all_right(self):
        const_left_wheel_1_pwm.ChangeDutyCycle(self.limit)
        const_left_wheel_2_pwm.ChangeDutyCycle(0)
        const_right_wheel_1_pwm.ChangeDutyCycle(0)
        const_right_wheel_2_pwm.ChangeDutyCycle(self.limit)

    ## Método que seta os valores das variáveis recebidas.
    def set_values(self,speed,steer,limit):
        if(speed < -35):
            self.movement = "reverse"
        elif(speed > 35):
            self.movement = "forward"
        else:
            self.movement = "none"

        if(steer < -35):
            self.direction = "left"
        elif(steer > 35):
            self.direction = "right"
        else:
            self.direction = "none"
        
        self.limit = limit
        print("--------")
        print("Movement: " + self.movement)
        print("Direction: " + self.direction)
        print("--------")

    ## Movimenta o robô baseado no valor da variável direction.
    def move(self):
        if(self.movement == "forward" and self.direction == "none"):
            self.go_forward()
        elif(self.movement == "forward" and self.direction == "left"):
            self.turn_left_forward()
        elif(self.movement == "forward" and self.direction == "right"):
            self.turn_right_forward()
        elif(self.movement == "none" and self.direction == "left"):
            self.turn_all_left()
        elif(self.movement == "none" and self.direction == "right"):
            self.turn_all_right()
        elif(self.movement == "reverse" and self.direction == "none"):
            self.go_back()
        elif(self.movement == "reverse" and self.direction == "left"):
            self.turn_left_back()
        elif(self.movement == "reverse" and self.direction == "right"):
            self.turn_right_back()
        else:
            self.stop()

    ## Método que responde ao recebimento de comandos que serão enviados aos arduinos.
    # Envia os comandos para os arduinos. \n
    def callback_set_values(self,msg):
        info = str(msg.data).split("$")
        try:
            self.set_values(int(info[0]),int(info[1]),int(info[2]))
        except:
            self.movement = "none"
            self.direction = "none"
            self.limit = 100
        
        self.move()

    ## Método que escuta do tópico control_robot para tratar os comandos recebidos.
    def listen_values(self):
        rospy.Subscriber("control_robot", String, self.callback_set_values)  

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == '__main__':
    control = Control_mini_robot()
    const_pub_log.publish('startedFile$control_mini_robot.py')
    control.listen_values()
    rospy.spin()
