#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com os arduinos, enviando os comandos que serão enviados para o hover board.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,serial,rospy,RPi.GPIO as gpio
from agrobot_msgs.msg import Control,Log
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)
## Constante utilizada para acessar o conversor TTL 0.
## Constante que pinta o texto de azul.
const_blue: str = '\033[94m'
## Constante que pinta o texto de verde.
const_green: str = '\033[92m'
## Constante que pinta o texto de vermelho.
const_error: str = '\033[91m'
## Constante finaliza a pintura do texto.
const_end_color: str = '\033[0m'
## Constante do pino no qual a primeira roda da frente está ligada.
const_front_wheel_1 = 16
## Constante do pino no qual a segunda roda da frente está ligada.
const_front_wheel_2 = 13
## Constante do pino no qual a primeira roda de trás está ligada.
const_back_wheel_1 = 18
## Constante do pino no qual a segunda roda de trás está ligada.
const_back_wheel_2 = 15

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó control_robot.
rospy.init_node('control_mini_robot', anonymous=True) 

## Configurando o GPIO
gpio.setmode(gpio.BOARD)
gpio.setup(const_front_wheel_1, gpio.OUT)
gpio.setup(const_front_wheel_2, gpio.OUT)
gpio.setup(const_back_wheel_1, gpio.OUT)
gpio.setup(const_back_wheel_2, gpio.OUT)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que faz logs.
def do_log(log_type: str,source_file: str,severity: str ="",msg: str ="",where: str =""):
    log: Log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que finaliza o módulo ao receber o comando certo no tópico shutdown.
def callback_shutdown(file_to_shutdown):
    if(str(file_to_shutdown.data) == "shutdown_control_mini_robot"):
        do_log("error","control_mini_robot.py","Warning","Control mini robot finalized.","function callback_shutdown()")
        rospy.signal_shutdown("Control_mini_robot finalized")
        exit(0)

## Função que pinta um texto com a cor passada como argumento e retorna o std_valueado.
def set_color(color: str,text: str):
    return color + text + const_end_color

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência a comunicação com os arduinos.
class Control_mini_robot():
    def __init__(self):
        ## Variável utilizada para enviar a velocidade. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.direction: str = "forward"

    ## Seta o valor de GPIO para as rodas da frente.
    def set_value_to_front_wheels(self,value):
        gpio.output(const_front_wheel_1, value)
        gpio.output(const_front_wheel_2, value)

    ## Seta o valor de GPIO para as rodas de trás.
    def set_value_to_back_wheels(self,value):
        gpio.output(const_back_wheel_1, value)
        gpio.output(const_back_wheel_2, value)
    
    ## Movimenta o robô baseado no valor da variável direction.
    def move(self):
        if(self.direction == "stop"):
            self.set_value_to_front_wheels(gpio.LOW)
            self.set_value_to_back_wheels(gpio.LOW)
        elif(self.direction == "forward"):
            self.set_value_to_front_wheels(gpio.HIGH)
            self.set_value_to_back_wheels(gpio.LOW)
        else:
            self.set_value_to_front_wheels(gpio.LOW)
            self.set_value_to_back_wheels(gpio.HIGH)

    ## Método que seta o valor da variável recebida.
    def set_direction(self,control_command: Control):
        if(int(control_command.speed > 0)):
            self.direction = "forward"
        elif(int(control_command.speed < 0)):
            self.direction = "reverse"
        else:
            self.direction = "stop"

    ## Método que responde ao recebimento de comandos que serão enviados aos arduinos.
    def callback_set_values(self,control_command: Control):
        try:
            self.set_direction(control_command)
        except:
            self.direction = "stop"

    ## Método que escuta do tópico control_robot para tratar os comandos recebidos.
    # Também cuida de chamar a função que movimenta o robô.
    def listen_values(self):
        rospy.Subscriber("control_robot", Control, self.callback_set_values)
        self.move()

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == '__main__':
    try: 
        do_log("started_file","[optional] control_mini_robot.py")
        Control_mini_robot().listen_values()
        rospy.Subscriber("shutdown", String, callback_shutdown)
        rospy.spin()
    except:
        do_log("error","control_mini_robot.py","Fatal","Could not run control_mini_robot.py.","main")