"""
Módulo que gerência a padronização dos comandos recebidos.
"""

#########################################
#----> Classe Command Standardizer <----#
#########################################

## Classe que gerência a padronização dos comandos recebidos
class CommandStandardizer():        
    ## Método que checa se o valor da variável speed está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def checkSpeed(self,speed):
        if(speed < -100):
            return -100
        if(speed > 100):
            return 100
        return speed

    ## Método que checa se o valor da variável steer está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def checkSteer(self,steer):
        if(steer < -100):
            return -100
        if(steer > 100):
            return 100
        return steer

    ## Método que checa se o valor da variável limit está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def checkLimit(self,limit):
        if(limit < 0):
            return 0
        if(limit > 100):
            return 100
        return limit

    ## Método que checa se o valor da signal speed está dentro dos limites aceitáveis.
    # Caso não esteja, corrige o valor e o retorna. \n
    # Caso esteja, somente retorna o valor recebido.
    def checkRelays(self,signal):
        if(signal != 0 and signal != 1):
            return 0
        return signal

    ## Método que executa todas as verificações das variáveis de controle do robô e retorna o resultado.
    def webServerMsgCheck(self,speed,steer,limit,powerA,powerB,pulverizer):
        return self.checkSpeed(speed),self.checkSteer(steer),self.checkLimit(limit),self.checkRelays(powerA),self.checkRelays(powerB),self.checkRelays(pulverizer)

    ## Método que recebe o comando em um vetor e separa as variáveis que serão checadas.
    def webServerMsgSpliter(self,msg):
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
                    powerA = value
                elif(parameter == "powerB"):
                    powerB = value
                elif(parameter == "pulverize"):
                    pulverizer = value
            except:
                pass
            index = index + 1
        try:
            return speed,steer,limit,powerA,powerB,pulverizer
        except:
            return 0,0,0,0,0,0

    ## Método que trata o comando recebido, separando e verificando todas as variáveis.
    # Retorna None caso algum erro ocorra. \n
    # Retorna um vetor com as variáveis separadas pelo símbolo $. Já corrigidas e verificadas.
    def webServerMsgHandler(self,msg):
        if(msg != None):
            speed,steer,limit,powerA,powerB,pulver = self.webServerMsgSpliter(msg) 
            speed,steer,limit,powerA,powerB,pulver = self.webServerMsgCheck(speed,steer,limit,powerA,powerB,pulver)  
            return str(speed) + "$" + str(steer) + "$" + str(limit) + "$" + str(powerA) + "$" + str(powerB) + "$" + str(pulver)
        else:
            return "None"