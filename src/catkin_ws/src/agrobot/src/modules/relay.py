#!/usr/bin/env python3

"""
Módulo que gerencia o envio dos comandos para os relés.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,rospy
from agrobot_msgs.msg import Relay as Ros_relay,Log,Control
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)
## Constante que pinta o texto de azul.
const_blue: str = '\033[94m'
## Constante que pinta o texto de verde.
const_green: str = '\033[92m'
## Constante que pinta o texto de vermelho.
const_error: str = '\033[91m'
## Constante finaliza a pintura do texto.
const_end_color: str = '\033[0m'
## Constante que define se a biblioteca do GPIO foi ou não importada com sucesso.
const_gpio_is_enabled: bool = False
## Instância que controla a publicação no tópico control_robot.
const_pub_control_robot: rospy.Publisher = rospy.Publisher('control_robot', Control, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó relay.
rospy.init_node("relay", anonymous=True)

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
def callback_shutdown(msg):
    if(str(msg.data) == "shutdown_relay"):
        log: Log = Log()
        log.type = "error"
        log.severity = "Warning"
        log.msg = "Relay finalized."
        log.file = "relay.py"
        log.where = "function callback_shutdown()"
        rospy.signal_shutdown("Relay finalized")
        exit(0)

## Função que pinta um texto com a cor passada como argumento e retorna o resultado.
def set_color(color: str,text: str):
    return color + text + const_end_color

## Função que recupera uma variável do rosparam.
def get_param(param_name: str):
    if(rospy.has_param(param_name)):
        return rospy.get_param(param_name)
    print(set_color(const_error,"[Error] "), end='')
    print("Error trying to get the parameter: " + param_name)

# -------------------------- #
# -> Imports Condicionais <- #
# -------------------------- #

try: 
    import RPi.GPIO as GPIO
    const_gpio_is_enabled = True
except:
    do_log("error","relay.py","Warning","Could not include RPi.GPIO as GPIO.","'Imports Condionais' area")

try:
    ## Definição do modo do GPIO.
    GPIO.setmode(GPIO.BOARD)
    ## Desabilitando os warnings do GPIO.
    GPIO.setwarnings(False)
except:
    do_log("error","relay.py","Warning","Could not set up GPIO configs.","'Imports Condionais' area")

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerencia os relés.
class Relay():
    ## Método que envia um sinal para o relé da placa A do hover board.
    def send_signal_to_board_one(self,signal: int):
        if(signal == 1):
            control = Control()
            control.power = 1
            control.limit = 0
            control.speed = 0
            control.steer = 0
            const_pub_control_robot.publish(control)
        else:
            control = Control()
            control.power = 0
            control.limit = 0
            control.speed = 0
            control.steer = 0
            const_pub_control_robot.publish(control)

    ## Método que envia um sinal para o relé da placa B do hover board.
    def send_signal_to_board_two(self,signal: int):
        if(signal == 1):
            control = Control()
            control.power = 1
            control.limit = 0
            control.speed = 0
            control.steer = 0
            const_pub_control_robot.publish(control)
        else:
            control = Control()
            control.power = 0
            control.limit = 0
            control.speed = 0
            control.steer = 0
            const_pub_control_robot.publish(control)

    ## Método que envia um sinal para o relé do pulverizador/uv.
    def send_signal_to_pulverizer(self,signal: int):
        if(const_gpio_is_enabled == True):
            if(signal == 1):
                GPIO.setmode(GPIO.BOARD)
                GPIO.setwarnings(False)
                GPIO.setup(35, GPIO.OUT)
                GPIO.output(35, GPIO.HIGH)
                time.sleep(0.2)
            else:
                GPIO.setmode(GPIO.BOARD)
                GPIO.setwarnings(False)
                GPIO.setup(35, GPIO.OUT)
                GPIO.output(35, GPIO.LOW)

    ## Método que trata os comandos recebidos pelo listener.
    def callback(self,relay_command: Ros_relay):
        work_permission: str = str(get_param("/relay_work_permission"))
        if(work_permission == "True"):
            try:
                self.send_signal_to_board_two(int(relay_command.power_b))
            except:
                do_log("error","relay.py","Warning","Could not send signal to board two.","class Relay, method callback()")
            try:
                self.send_signal_to_board_one(int(relay_command.power_a))
            except:
                do_log("error","relay.py","Warning","Could not send signal to board one.","class Relay, method callback()")
            try:
                self.send_signal_to_pulverizer(int(relay_command.power_pulverize))
            except:
                do_log("error","relay.py","Warning","Could not send signal to pulverizer.","class Relay, method callback()")
        else:
            do_log("error","relay.py","Warning","Relay is without permission to work.","class Relay, method callback()")
    
    ## Método que escuta do tópico relay e processa os comandos recebidos.
    def listener(self):
        rospy.Subscriber("relay", Ros_relay, self.callback)   
        rospy.Subscriber("shutdown", String, callback_shutdown)
        rospy.spin()

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == '__main__':
    try: 
        do_log("started_file","[optional] relay.py")
        Relay().listener()
    except:
        do_log("error","[optional] relay.py","Fatal","Could not run relay.py.","main")
        
