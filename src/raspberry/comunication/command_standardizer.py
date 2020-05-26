#!/usr/bin/env python3

"""
Módulo que gerencia a padronização dos comandos recebidos.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_log = rospy.Publisher("log", String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node("command_standardizer", anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência a padronização dos comandos recebidos.
class Command_standardizer():        
    ## Método que checa se o valor da variável speed está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def check_speed(self,speed):
        if(speed < -100):
            return -100
        if(speed > 100):
            return 100
        return speed

    ## Método que checa se o valor da variável steer está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def check_steer(self,steer):
        if(steer < -100):
            return -100
        if(steer > 100):
            return 100
        return steer

    ## Método que checa se o valor da variável limit está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def check_limit(self,limit):
        if(limit < 0):
            return 0
        if(limit > 100):
            return 100
        return limit

    ## Método que checa se o valor da signal speed está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def check_relays(self,signal):
        if(signal != 0 and signal != 1):
            return 0
        return signal

    ## Método que executa todas as verificações das variáveis de controle do robô e retorna o resultado.
    def msg_check(self,speed,steer,limit,power_a,power_b,pulverizer):
        return self.check_speed(speed),self.check_steer(steer),self.check_limit(limit),self.check_relays(power_a),self.check_relays(power_b),self.check_relays(pulverizer)

    ## Método que recebe o comando em um vetor e separa as variáveis que serão checadas.
    def msg_spliter(self,msg):
        index = 1
        while index < len(msg):
            try:
                parameter = msg[index].split("$")[0]
                value = int(msg[index].split("$")[1])
                if(parameter == "speed"):
                    speed = value
                elif(parameter == "steer"):
                    steer = value
                elif(parameter == "limit"):
                    limit = value
                elif(parameter == "powerA"):
                    power_a = value
                elif(parameter == "powerB"):
                    power_b = value
                elif(parameter == "pulverize"):
                    pulverizer = value
            except:
                const_pub_log.publish("error$Warning$Error while trying to split the msg from command priority decider.")
            index = index + 1
        try:
            return speed,steer,limit,power_a,power_b,pulverizer
        except:
            return 0,0,0,0,0,0

    ## Método que trata o comando recebido, separando e verificando todas as variáveis.
    # Retorna None caso algum erro ocorra. \n
    # Retorna um vetor com as variáveis separadas pelo símbolo $. Já corrigidas e verificadas.
    def msg_handler(self,msg):
        if(msg != None):
            speed,steer,limit,power_a,power_b,pulver = self.msg_spliter(msg) 
            speed,steer,limit,power_a,power_b,pulver = self.msg_check(speed,steer,limit,power_a,power_b,pulver)  
            return str(speed) + "$" + str(steer) + "$" + str(limit) + "$" + str(power_a) + "$" + str(power_b) + "$" + str(pulver)
        else:
            return "None"