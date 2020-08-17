#!/usr/bin/env python3

"""
Módulo que gerencia a padronização dos comandos recebidos.
"""

# ------------- #
# -> Imports <- #
# ------------- #

from agrobot_msgs.msg import CompleteControl

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência a padronização dos comandos recebidos.
class Command_standardizer():        
    ## Método que corrige o valor da variável speed caso seja necessário.
    def check_speed(self,speed: int) -> int:
        if(speed < -100):
            return -100
        if(speed > 100):
            return 100
        return speed

    ## Método que corrige o valor da variável steer caso seja necessário.
    def check_steer(self,steer: int) -> int:
        if(steer < -100):
            return -100
        if(steer > 100):
            return 100
        return steer

    ## Método que corrige o valor da variável limit caso seja necessário.
    def check_limit(self,limit: int) -> int:
        if(limit < 0):
            return 0
        if(limit > 100):
            return 100
        return limit

    ## Método que corrige o valor da variável signal caso seja necessário.
    def check_relays(self,signal: str) -> str:
        if(signal != "0" and signal != "1"):
            return "0"
        return signal

    ## Método que executa todas as verificações das variáveis de controle do robô e retorna o resultado.
    def msg_check(self,msg: CompleteControl) -> CompleteControl:
        msg_checked: CompleteControl = CompleteControl()
        
        msg_checked.control.speed = self.check_speed(int(msg.control.speed))
        msg_checked.control.steer = self.check_steer(int(msg.control.steer))
        msg_checked.control.limit = self.check_limit(int(msg.control.limit))

        msg_checked.relay.power_a = self.check_relays(str(msg.relay.power_a))
        msg_checked.relay.power_b = self.check_relays(str(msg.relay.power_b))
        msg_checked.relay.power_pulverize = self.check_relays(str(msg.relay.power_pulverize))

        return msg_checked

    ## Método que trata o comando recebido, separando e verificando todas as variáveis.
    def msg_handler(self,msg) -> CompleteControl:
        if(msg != None):
            return self.msg_check(msg)  
        else: ## Retorna um objeto com todos os valores zerados
            return CompleteControl()
