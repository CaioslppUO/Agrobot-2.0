#!/usr/bin/env python3

""" 
Programa que gerencia as variáveis de inicialização do sistema.
"""

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Constante que pinta o texto de azul.
const_blue = '\033[94m'
## Constante que pinta o texto de verde.
const_green = '\033[92m'
## Constante que pinta o texto de vermelho.
const_error = '\033[91m'
## Constante finaliza a pintura do texto.
const_end_color = '\033[0m'

# ------------- #
# -> Funções <- #
# ------------- #

## Função que pinta um texto com a cor passada como argumento e retorna o resultado.
def set_color(color,text):
    return color + text + const_end_color

## Função que checa se cada uma das variáveis recebidas é válida.
def check_variables(server_ip,enable_uart,enable_relay,uart_amount,enable_face_detect,root_path):
    if(server_ip == None):
        return False,set_color(const_error,"[Error] ") + "Invalid server_ip."
    if(enable_uart == None):
        return False,set_color(const_error,"[Error] ") + "Invalid enable_uart."
    if(enable_relay == None):
        return False,set_color(const_error,"[Error] ") + "Invalid enable_relay."
    if(uart_amount == None):
        return False,set_color(const_error,"[Error] ") + "Invalid uart_amount."
    if(enable_face_detect == None):
        return False,set_color(const_error,"[Error] ") + "Invalid enable_face_detect."
    if(root_path == None):
        return False,set_color(const_error,"[Error] ") + "Invalid root_path."
    return True,set_color(const_green,"[OK] ") + "Launcher variables were correctly initialized."

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerência as variáveis de inicialização do robô.
class Launcher_variables():
    def __init__(self):
        ## Ip do robô que irá rodar o webServer de conexão manual com o app
        self.server_ip = None
        ## Boolean para definir se a comunicação Uart vai ou não estar habilitada
        self.enable_uart = None
        ## Boolean para definir se os relés vão ou não estar habilitados
        self.enable_relay = None
        ## Quantidade de Conversores TTL que serão utilizados
        self.uart_amount = None
        ## Boolean para definir se a classe que gerẽncia a detecção de faces vai ou não estar habilitada
        self.enable_face_detect = None
        ## Caminho completo para a raiz do código fonte do robô: /home/USER/Agrobot-2.0/raspberry
        self.root_path = None

    ## Método que separa as variáveis recebidas no vetor variables.
    # Caso alguma variável esteja errada, finaliza o programa e printa uma mensagem de erro. \n
    # Caso todas as variáveis estejam corretas, printa uma mensagem de sucesso e continua a execução do programa.
    def variable_separator(self,variables):
        i = 1
        while(i < len(variables)):
            variable = variables[i].split(":")
            if(variable[0] == "server_ip"):
                self.server_ip = str(variable[1])
            elif(variable[0] == "enable_uart" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enable_uart = str(variable[1])
            elif(variable[0] == "enable_relay" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enable_relay = str(variable[1])
            elif(variable[0] == "uart_amount" and (int(variable[1]) == 0 or int(variable[1]) == 1 or int(variable[1]) == 2)):
                self.uart_amount = int(variable[1])
            elif(variable[0] == "enable_face_detect"):
                self.enable_face_detect = str(variable[1])
            elif(variable[0] == "root_path"):
                self.root_path = str(variable[1])
            i = i + 1

        check_result,check_result_msg = check_variables(self.server_ip,self.enable_uart,self.enable_relay,self.uart_amount,self.enable_face_detect,self.root_path)
        
        print(check_result_msg)
        if(check_result == False):
            exit(0)
            
        return self.server_ip,self.enable_uart,self.enable_relay,self.uart_amount,self.enable_face_detect,self.root_path