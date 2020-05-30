#!/usr/bin/env python3

"""
Módulo que controla o movimento do robô.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import time,rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Constante que define o que significa 'andar reto' para o robô.
const_default_foward = 0

## Constante que serve como 'folga' para o processamento de andar reto.
const_ignore_range = (5/100) * 360

## Variável que controla a publicação de textos no tópico da control_lidar.
const_pub_control_command = rospy.Publisher("control_lidar", String,queue_size=10)

## Variável que controla a publicação de textos no tópico de logs.
const_pub_log = rospy.Publisher("log", String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('control_lidar', anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #

class Control_lidar():
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
        self.ticks = 0

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
        elif(correct_for == "right"):
            self.steer = int(self.standart_data['steer_default'] - int(self.standart_data['correction_magnitude'])
        else:
            self.steer = int(self.standart_data['steer_default'] + int(self.standart_data['correction_magnitude'])
        self.tick = int(self.tick) - 1

    ## Método que verifica o valor do tick e decide se é ou não necessário realizar a leitura dos sensores e alterar o valor da direção.
    def check_tick(self):
        if(self.tick == 0):
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
        info = str(msg.data)
        if(info == 'walk'):
            self.walk = True
        else:
            self.walk = False

    ## Método callback para as mensagens recebidas pelo app, no modo de controle automático.
    # Recebe e separa as variáveis passadas pelo app.
    def callback_app_msg(self,msg):
        info = str(msg.data)
        if(info != ''):
            vet = info.split('*')
            for variable in vet :
                new_variable = variable.split('$')
                if(new_variable[0] == 'limit'):
                    self.standart_data['limit'] = int(new_variable[1])
                elif(new_variable[0] == 'tick'):
                    self.standart_data['tick_default'] = int(new_variable[1])
                elif(new_variable[0] == 'steer'):
                    self.standart_data['steer_default'] = int(new_variable[1])
                elif(new_variable[0] == 'speed'):
                    self.standart_data['speed_default'] = int(new_variable[1])
                elif(new_variable[0] == 'shift'):
                    self.standart_data['correction_magnitude'] = int(new_variable[1])
                elif(new_variable[0] == 'uv'):
                    self.standart_data['uv'] = int(new_variable[1])

    ## Método que verifica se existe algum objeto 'próximo' ao sensor central do robô. Caso exista para o robô e desliga a lâmpada UV.
    def check_foward(self):
        if(self.center_sensor == 'free')
            self.speed = standart_data['speed_default']
            self.uv = standart_data['uv']
            self.check_tick()
        else:
            self.steer = 0
            self.speed = 0
            self.uv = 0

    ## Método que recebe o valor lido no acelerômetro e decide se tem que corrigir o movimento ou não.
    def check_accelerometer(self,msg):
       value = int(msg.data)
       if(value >= const_default_foward - const_ignore_range and value <= const_default_foward + const_ignore_range):
           self.steer = dataDefault['steer_default']
       elif(value < const_default_foward - const_ignore_range):
           self.steer = int(dataDefault['steer_default']) - int(dataDefault['correction_magnitude'])
       self.steer = int(dataDefault['steer_default']) + int(dataDefault['correction_magnitude'])

    ## Método que controla o movimento do robô.
    def move(self):
        if(self.check_move_permission()):
            if(self.walk):
                self.check_foward(speed,steer,uv,tick)
                rospy.Subscriber('angulo', String, self.check_accelerometer) # verifica e ajusta a direção com base na leitura do acelerômetro.
                command_to_publish = "5*speed$" + str(self.speed) + "*steer$" + str(self.steer) + "*limit$" + str(self.standart_data['limit']) + "*powerA$0*powerB$0*pulverize$" + str(self.uv)
                const_pub_control_command.publish(command_to_publish)
            else:
                command_to_publish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$" + str(standart_data['uv'])
                const_pub_control_command.publish(command_to_publish)
        else:
            command_to_publish = "5*speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
            const_pub_control_command.publish(command_to_publish)

    ## Método callback para a leitura do lidar.
    # O envio de comandos ao robô é baseado na velocidade de leitura do lidar.
    def callback_lidar(self,msg):
        info = str(msg.data)
        rospy.Subscriber('walk', String, self.callback_walk) # Atualiza o valor da variável 'walk'.
        sensors_value = info.split('$')
        self.left_sensor = point_direction[0]
        self.center_sensor = point_direction[1]
        self.right_sensor = point_direction[2]
        self.move() # Chama o método que controla o robô.
        rospy.Subscriber('param_server', String, self.callback_app_msg) # Verifica se houveram ou não mudanças nas configurações do modo automático.

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == "__main__":
    try:
        const_pub_log.publish("startedFile$control_lidar.py")
        control_lidar = Control_lidar()
        rospy.Subscriber('lidar', String, control_lidar.callback_lidar)
        rospy.Subscriber('param_server', String, control_lidar.callback_app_msg)
        rospy.spin()
    except KeyboardInterrupt:
        const_pub_log.publish("error$Warning$control_lidar.py finalized.")
