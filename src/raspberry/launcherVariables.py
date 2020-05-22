""" 
Programa que gerencia as variáveis de inicialização do sistema.
"""

## Função que checa se cada uma das variáveis recebidas é válida.
#  Caso seja inválida, retorna false e uma mensagem de erro. \n
#  Caso seja válida, retorna true e uma mensagem de sucesso.
def checkVariables(serverIp,enableUart,enableRelay,uartAmount,enableFaceDetect,rootPath):
    if(serverIp == None):
        return False,"Invalid ServerIp"
    if(enableUart == None):
        return False,"Invalid EnableUart"
    if(enableRelay == None):
        return False,"Invalid EnableRelay"
    if(uartAmount == None):
        return False,"Invalid UartAmount"
    if(enableFaceDetect == None):
        return False,"Invalid enableFaceDetect"
    if(rootPath == None):
        return False,"Invalid rootPath"
    return True,"Launcher variables were initialized correctly"

## Classe que gerência as variáveis de inicialização do robô.
class LauncherVariables():
    def __init__(self):
        ## Ip do robô que irá rodar o webServer de conexão manual com o app
        self.serverIp         = None
        ## Boolean para definir se a comunicação Uart vai ou não estar habilitada
        self.enableUart       = None
        ## Boolean para definir se os relés vão ou não estar habilitados
        self.enableRelay      = None
        ## Quantidade de Conversores TTL que serão utilizados
        self.uartAmount       = None
        ## Boolean para definir se a classe que gerẽncia a detecção de faces vai ou não estar habilitada
        self.enableFaceDetect = None
        ## Caminho completo para a raiz do código fonte do robô: /home/USER/Agrobot-2.0/raspberry
        self.rootPath         = None

    ## Método que separa as variáveis recebidas no vetor variables.
    # Caso alguma variável esteja errada, finaliza o programa e printa uma mensagem de erro. \n
    # Caso todas as variáveis estejam corretas, printa uma mensagem de sucesso e continua a execução do programa.
    def variableSeparator(self,variables):
        i = 1
        while(i < len(variables)):
            variable = variables[i].split(":")
            if(variable[0] == "serverIp"):
                self.serverIp = str(variable[1])
            elif(variable[0] == "enableUart" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enableUart = str(variable[1])
            elif(variable[0] == "enableRelay" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enableRelay = str(variable[1])
            elif(variable[0] == "uartAmount" and (int(variable[1]) == 0 or int(variable[1]) == 1 or int(variable[1]) == 2)):
                self.uartAmount = int(variable[1])
            elif(variable[0] == "enableFaceDetect"):
                self.enableFaceDetect = str(variable[1])
            elif(variable[0] == "rootPath"):
                self.rootPath = str(variable[1])
            i = i + 1

        checkResult,checkResultMsg = checkVariables(self.serverIp,self.enableUart,self.enableRelay,self.uartAmount,self.enableFaceDetect,self.rootPath)
        
        if(checkResult == False):
            print(checkResultMsg)
            exit(0)
            
        print(checkResultMsg)
        return self.serverIp,self.enableUart,self.enableRelay,self.uartAmount,self.enableFaceDetect,self.rootPath
