#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com os arduinos, enviando os comandos que serão enviados para o hover board.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,serial,rospy
from agrobot_msgs.msg import Control,Log
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)
## Constante utilizada para acessar o conversor TTL 0.
const_uart_0 = None
## Constante utilizada para acessar o conversor TTL 1.
const_uart_1 = None
## Constante que pinta o texto de azul.
const_blue: str = '\033[94m'
## Constante que pinta o texto de verde.
const_green: str = '\033[92m'
## Constante que pinta o texto de vermelho.
const_error: str = '\033[91m'
## Constante finaliza a pintura do texto.
const_end_color: str = '\033[0m'

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó control_robot.
rospy.init_node('control_robot', anonymous=True) 

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
    if(str(file_to_shutdown.data) == "shutdown_control_robot"):
        do_log("error","control_robot.py","Warning","Control robot finalized.","function callback_shutdown()")
        rospy.signal_shutdown("Control_robot finalized")
        exit(0)

## Função que pinta um texto com a cor passada como argumento e retorna o std_valueado.
def set_color(color: str,text: str):
    return color + text + const_end_color

## Função que define e instancia a comunicação com os conversores TTL baseando-se na variável uart_amount.
def set_uart(uart_amount: int):
    global const_uart_0,const_uart_1
    if(uart_amount == 1):
        try:
            const_uart_0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            try:
                const_uart_0 = serial.Serial(
                    port='/dev/ttyUSB_CONVERSOR-1',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                )
            except:
                do_log("error","control_robot.py","Warning","Error trying to set 1 Uart.","function set_uart")
    elif(uart_amount == 2):
        try:
            const_uart_0 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-0',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

            const_uart_1 = serial.Serial(
                port='/dev/ttyUSB_CONVERSOR-1',
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )
        except:
            do_log("error","control_robot.py","Warning","Error trying to set 2 Uarts.","function set_uart")

## Função que recupera uma variável do rosparam.
def get_param(param_name: str):
    if(rospy.has_param(param_name)):
        return rospy.get_param(param_name)

    print(set_color(const_error,"[Error] "), end='')
    print("Error trying to get the parameter: " + param_name)
    print(set_color(const_error,"[Aborting] "), end='')
    print("web_server.py")
    exit(0)


# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência a comunicação com os arduinos.
class Control_robot():
    def __init__(self):
        ## Variável utilizada para enviar a velocidade. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.speed: str = "0000"
        ## Variável utilizada para enviar a direção. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.steer: str = "0000"
        ## Variável utilizada para enviar o limite. O primeiro valor é o sinal do número: 0 Negativo e 1 Positivo.
        self.limit: str = "0000"
        ## Variável utilizada para controlar o relé que liga ou desliga a placa do hoverboard.
        self.power: int = 0

        try:
            self.uart_amount: int = int(get_param("/uart_amount"))
        except:
            self.uart_amount: int = 0

        try:
            set_uart(self.uart_amount)
            # Tempo para garantir que a comunicação está estabelecida com os conversores TTL.
            self.store_param("/relay_work_permission","True")
        except:
            do_log("error","control_robot.py","Warning","Could not set UART(s).","class Control_robot, method __init__()")

    ## Método que guarda um novo parâmetro.
    # Caso o parâmetro já exista, ele é substituído.
    def store_param(self,param_name: str,param_value):
        if(rospy.has_param(param_name)):
            rospy.delete_param(param_name)
        rospy.set_param(param_name,param_value)

    ## Método que transforma um valor inteiro para o protocolo utilizado para enviar comandos ao arduino.
    # Padrão: SINAL_NÙMERO: o Sinal ocupa 1 posição, o número ocupa 3 posições.
    def get_stand_value(self, value: int) -> str:
        if(value >= 0):
            std_value: str = '1'
        else:
            std_value: str = '0'
        if(value < 10 and value > -10):
            std_value += '00'
        elif(value < 100 and value > -100):
            std_value += '0'
        std_value += str(abs(value))
        return std_value

    ## Método que seta os valores das variáveis recebidas.
    def set_values(self,control_command: Control):
        self.speed = self.get_stand_value(int(control_command.speed))
        self.steer = self.get_stand_value(int(control_command.steer))
        self.limit = self.get_stand_value(int(control_command.limit))
        self.power = int(control_command.power)

    ## Método que responde ao recebimento de comandos que serão enviados aos arduinos.
    # Envia os comandos para os arduinos. \n
    def callback_set_values(self,control_command: Control):
        try:
            self.set_values(control_command)
        except:
            self.speed = self.get_stand_value(0)
            self.steer = self.get_stand_value(0)
            self.limit = self.get_stand_value(0)
            self.power = 0

        command: str = self.speed + ',' + self.steer + ',' + self.limit + ',' + str(self.power) + ";"

        try:
            if(self.uart_amount == 1):  
                const_uart_0.write(str.encode(command))
            elif(self.uart_amount == 2):
                const_uart_0.write(str.encode(command))
                const_uart_1.write(str.encode(command))
            else:
                time.sleep(0.02) # Sleep para não sobrecarregar a comunicação com o arduino.
        except:
            do_log("error","control_robot.py","Fatal","Could not write through UART communication.","class Control_robot, method callback_set_values()")

    ## Método que escuta do tópico control_robot para tratar os comandos recebidos.
    def listen_values(self):
        rospy.Subscriber("control_robot", Control, self.callback_set_values)  

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == '__main__':
    try: 
        do_log("started_file","[optional] control_robot.py")
        Control_robot().listen_values()
        rospy.Subscriber("shutdown", String, callback_shutdown)
        rospy.spin()
    except:
        do_log("error","control_robot.py","Fatal","Could not run control_robot.py.","main")