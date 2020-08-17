#!/usr/bin/env python3

"""
Módulo que controla o movimento do robô.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,rospy
from agrobot_msgs.msg import Lidar,CommandWebServer,CompleteControl,Automatic,Log

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Constante que define o que significa 'andar reto' para o robô.
const_default_foward = 0

## Constante que serve como 'folga' para o processamento de andar reto.
const_ignore_range = (5/100) * 360

## Variável que controla a publicação no tópico da control_lidar.
const_pub_control_command = rospy.Publisher("control_lidar", CompleteControl,queue_size=10)
## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', Log, queue_size=10)


# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('control_lidar', anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #


class Control_lidar():
    ## Função que faz logs.
    def do_log(self,log_type,source_file,severity="",msg="",where=""):
        log = Log()
        log.type = log_type
        log.file = source_file
        log.severity = severity
        log.msg = msg
        log.where = where
        const_pub_log.publish(log)

    def __init__(self):
        ## Variável boolean que diz se o robô pode ou não nadar.
        # É utilizada para controlar a funcionalidade de andar por 'x' segundos e parar por 'y' segundos.
        self.walk = True
        ## Variável que controla a velocidade que será enviada para o robô.
        self.speed = 0
        ## Variável que controla a direção que será enviada para o robô.
        self.steer = 0
        ## Variável que controla o relé da lâmpada uv que será enviado para o robô.
        self.uv = 0
        ## Variáveç que contém a direção para a qual é necessário corrigir o movimento do robô.
        self.correction_dir = None
        ## Variável que contém a informação se existe algum 'objeto' próximo ao sensor da esquerda.
        self.left_sensor = None
        ## Variável que contém a informação se existe algum 'objeto' próximo ao sensor da direita.
        self.right_sensor = None
        ## Variável que contém a informação se existe algum 'objeto' próximo ao sensor do meio.
        self.center_sensor = None
        ## Variável que controla a quantidade de movimentos de correção que serão aplicados.
        self.tick = 0

        ## Variável que controla os valores recebidos pelo app.
        self.standart_data = {}
        ## Variável que recebe o valor do app para o limite.
        self.standart_data['limit'] = 0
        ## Variável que recebe o valor do app para o número de correções de movimentos.
        self.standart_data['tick_default'] = 0
        ## Variável que recebe o valor do app para a direção padrão que faz o robô 'andar reto'.
        self.standart_data['steer_default'] = 0
        ## Variável que recebe o valor do app para a velocidade padrão.
        self.standart_data['speed_default'] = 0
        ## Variável que recebe o valor do app para a intensidade da correção do movimento.
        self.standart_data['correction_magnitude'] = 0
        ## Variável que recebe o valor do app para o estado da lâmpada UV.
        self.standart_data['uv'] = 0

    ## Método seta o movimento necessário para corrigir o robô(se for necessário).
    def define_correction_movement(self):
        if(self.left_sensor == "busy"):
            self.tick = self.standart_data['tick_default']
            self.correction_dir = "right"
        elif(self.right_sensor == "busy"):
            self.tick = self.standart_data['tick_default']
            self.correction_dir = "left"

    ## Método que avalia os valores lidos pelos sensores e decide se precisa corrigir ou não o movimento, alterando o valor da direção.
    # Também altera a variável 'tick', indicando que um movimento de correção foi efetuado.
    def set_steer(self):
        if(self.tick == 1):
            self.steer = self.standart_data['steer_default']
        elif(self.correction_dir == "right"):
            self.steer = int(self.standart_data['steer_default']) - int(self.standart_data['correction_magnitude'])
        else:
            self.steer = int(self.standart_data['steer_default']) + int(self.standart_data['correction_magnitude'])
        self.tick = int(self.tick) - 1

    ## Método que verifica o valor do tick e decide se é ou não necessário realizar a leitura dos sensores e alterar o valor da direção.
    def check_tick(self):
        if(int(self.tick) == 0):
            self.define_correction_movement()
        else:
            self.set_steer()

    ## Método que checa se o modo automático está ativo ou não, liberando ou bloqueando a movimentação automática.
    def check_move_permission(self):
        if( self.standart_data['limit'] == 0 and 
            self.standart_data['tick_default'] == 0 and
            self.standart_data['steer_default'] == 0 and
            self.standart_data['speed_default'] == 0 and
            self.standart_data['correction_magnitude'] == 0 ):
            return False
        return True

    ## Método callback para a classe que controla o tempo de movimento e parada do robô.
    # Define a variável walk, que diz para o robô quando ele pode andar e quando deve ficar parado.
    def callback_walk(self,msg):
        if(msg != None):
            if(msg.walk_permission == "walk"):
                self.walk = True
            else:
                self.walk = False

    ## Método callback para as mensagens recebidas pelo app, no modo de controle automático.
    # Recebe e separa as variáveis passadas pelo app.
    def callback_app_msg(self,msg):
        if(msg != None):
            self.standart_data['limit'] = int(msg.limitDefault)
            self.standart_data['tick_default'] = int(msg.tickDefault)
            self.standart_data['steer_default'] = int(msg.steerDefault)
            self.standart_data['speed_default'] = int(msg.speedDefault)
            self.standart_data['correction_magnitude'] = int(msg.detectDistance)
            self.standart_data['uv'] = int(msg.uv)

    ## Método que verifica se existe algum objeto 'próximo' ao sensor central do robô. Caso exista para o robô e desliga a lâmpada UV.
    def check_foward(self):
        if(self.center_sensor == 'free'):
            self.speed = self.standart_data['speed_default']
            self.uv = self.standart_data['uv']
            self.check_tick()
        else:
            self.steer = 0
            self.speed = 0
            self.uv = 0

    ## Método que recebe o valor lido no acelerômetro e decide se tem que corrigir o movimento ou não.
    def check_accelerometer(self,msg):
       value = msg.correction_magnitude
       if(value >= const_default_foward - const_ignore_range and value <= const_default_foward + const_ignore_range):
           self.steer = self.standart_data['steer_default']
       elif(value < const_default_foward - const_ignore_range):
           self.steer = int(self.standart_data['steer_default']) - int(self.standart_data['correction_magnitude'])
       self.steer = int(self.standart_data['steer_default']) + int(self.standart_data['correction_magnitude'])

    ## Método que controla o movimento do robô.
    def move(self):
        command_to_publish = CompleteControl()
        command_to_publish.relay.power_a = 0
        command_to_publish.relay.power_b = 0
        command_to_publish.relay.power_pulverize = 0
        if(self.check_move_permission()):
            if(self.walk):
                self.check_foward()
                rospy.Subscriber('angle', Automatic, self.check_accelerometer) # verifica e ajusta a direção com base na leitura do acelerômetro.
                command_to_publish.relay.power_uv = self.uv
                command_to_publish.control.speed = self.speed
                command_to_publish.control.steer = self.steer
                command_to_publish.control.limit = int(self.standart_data['limit'])
                const_pub_control_command.publish(command_to_publish)
            else:
                command_to_publish.relay.power_uv = int(self.standart_data['uv'])
                command_to_publish.control.speed = 0
                command_to_publish.control.steer = 0
                command_to_publish.control.limit = 0
                const_pub_control_command.publish(command_to_publish)
        else:
            command_to_publish.relay.power_uv = 0
            command_to_publish.control.speed = 0
            command_to_publish.control.steer = 0
            command_to_publish.control.limit = 0
            const_pub_control_command.publish(command_to_publish)

    ## Método callback para a leitura do lidar.
    # O envio de comandos ao robô é baseado na velocidade de leitura do lidar.
    def callback_lidar(self,msg):
        rospy.Subscriber('walk', Automatic, self.callback_walk) # Atualiza o valor da variável 'walk'.
        self.left_sensor = msg.left_pos
        self.center_sensor = msg.middle_pos
        self.right_sensor = msg.right_pos
        self.move() # Chama o método que controla o robô.
        rospy.Subscriber('param_server', CommandWebServer, self.callback_app_msg) # Verifica se houveram ou não mudanças nas configurações do modo automático.

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == "__main__":
    try:
        do_log("started_file","[essential] control_lidar.py")
        control_lidar = Control_lidar()
        rospy.Subscriber('lidar', Lidar, control_lidar.callback_lidar)
        rospy.Subscriber('param_server', CommandWebServer, control_lidar.callback_app_msg)
        rospy.spin()
    except KeyboardInterrupt:
        do_log("KeyBoard Interrupt","control_lidar.py","Fatal","Module interrupted: control_lidar.py","main")
