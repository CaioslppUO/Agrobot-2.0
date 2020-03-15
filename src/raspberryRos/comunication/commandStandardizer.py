#########################################
#----> Classe Command Standardizer <----#
#########################################

class CommandStandardizer():
    def __init__(self):
        self.a = 10

    #Checa se a velocidade está correta e a corrige caso seja necessário
    #Entrada: Velocidade
    #Retorno: Velocidade recebida caso esteja correta ou a velocidade corrigida
    #Pré-condição: Nenhuma
    #Pós-condição: Caso a velocidade esteja errada, ela é corrigida
    def checkSpeed(self,speed):
        if(speed < -100):
            return -100
        if(speed > 100):
            return 100
        return speed

    #Checa se a direção está correta e a corrige caso seja necessário
    #Entrada: Direção
    #Retorno: Direção recebida caso esteja correta ou a direção corrigida
    #Pré-condição: Nenhuma
    #Pós-condição: Caso a direção esteja errada, ela é corrigida
    def checkSteer(self,steer):
        if(steer < -100):
            return -100
        if(steer > 100):
            return 100
        return steer

    #Checa se o limite está correta e a corrige caso seja necessário
    #Entrada: Limite
    #Retorno: Limite recebida caso esteja correta ou o limite corrigida
    #Pré-condição: Nenhuma
    #Pós-condição: Caso o limite esteja errada, ela é corrigida
    def checkLimit(self,limit):
        if(limit < 0):
            return 0
        if(limit > 100):
            return 100
        return limit

    #Checa se o relé está correto e o corrige caso seja necessário
    #Entrada: Relé
    #Retorno: Relé recebido caso esteja correto ou o relé corrigido
    #Pré-condição: Nenhuma
    #Pós-condição: Caso o relé esteja errado, ele é corrigido
    def checkRelays(self,signal):
        if(signal != 0 and signal != 1):
            return 0
        return signal

    #Checa todas as variáveis recebidas pelo web server
    #Entrada: Velocidade, direção, limite, powerA, powerB e pulverizador
    #Retorno: Retorna as variáveis recebidas já corrigidas caso necessário
    #Pré-condição: Nenhuma
    #Pós-condição: As variáveis recebidas são retornadas já corrigidas caso necessário
    def webServerMsgCheck(self,speed,steer,limit,powerA,powerB,pulverizer):
        return self.checkSpeed(speed),self.checkSteer(steer),self.checkLimit(limit),self.checkRelays(powerA),self.checkRelays(powerB),self.checkRelays(pulverizer)

    #Separa e garante que todas as variáveis necessárias para a execução estão presentes
    #Entrada: Mensagem recebida pelo web server
    #Retorno: Variáveis separadas e corrigidas
    #Pré-condição: Nenhuma
    #Pós-condição: As variáveis são retiradas da mensagem e retornadas, já separadas e tratadas
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

    #Checa e corrige todas as variáveis recbidas pelo web server
    #Entrada: Mensagem recebida pelo web server
    #Retorno: Variáveis recebidas já tratadas ou None caso a mensagem seja nula
    #Pré-condição: Nenhuma
    #Pós-condição: Retorna as variáveis corretamente, já dentro do protoloc interno de comunicação do ROS ou None caso a mensagem seja inválida
    def webServerMsgHandler(self,msg):
        if(msg != None):
            speed,steer,limit,powerA,powerB,pulver = self.webServerMsgSpliter(msg) 
            speed,steer,limit,powerA,powerB,pulver = self.webServerMsgCheck(speed,steer,limit,powerA,powerB,pulver)  
            return str(speed) + "$" + str(steer) + "$" + str(limit) + "$" + str(powerA) + "$" + str(powerB) + "$" + str(pulver)
        else:
            return "None"