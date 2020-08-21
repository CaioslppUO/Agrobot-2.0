#!/usr/bin/env python3

"""
Módulo que gerência o carregamento das variáveis de configuração de launcher do sistema.
"""

# ------------- #
# -> Imports <- #
# ------------- #

from io import TextIOWrapper
import rospy,pathlib

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Constante que pinta o texto de azul.
const_blue: str = '\033[94m'
## Constante que pinta o texto de verde.
const_green: str = '\033[92m'
## Constante que pinta o texto de vermelho.
const_error: str = '\033[91m'
## Constante finaliza a pintura do texto.
const_end_color: str = '\033[0m'
## Constante que guarda a localização na qual este arquivo se encontra.
const_current_folder_location: str = str(pathlib.Path(__file__).parent.absolute()) + "/"

# ------------- #
# -> Funções <- #
# ------------- #

## Função que pinta um texto com a cor passada como argumento e retorna o resultado.
def set_color(color: str,text: str):
    return color + text + const_end_color

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerencia o carregamento e distribuição das variáveis de launch pelo rosparam.
class Config_launcher:
    ## Método que inicializa com None todas as variáveis que serão carregadas dos arquivos de configuração.
    def __init__(self):
        self.server_ip: str = ""
        self.enable_uart: str = ""
        self.enable_relay: str = ""
        self.uart_amount: str = ""
        self.enable_face_detect: str = ""
        self.root_path: str = ""
        self.launch_mode: str = ""

    ## Método que guarda um novo parâmetro de launch lido.
    # Caso o parâmetro já exista, ele é substituído.
    def store_param(self,param_name: str,param_value):
        if(rospy.has_param(param_name)):
            rospy.delete_param(param_name)
        rospy.set_param(param_name,param_value)

    ## Método que lê o arquivo de configuração e extraí os parâmetros.
    def process_config_file(self,config_file: TextIOWrapper):
        content: list = config_file.read().splitlines()
        for param in content:
            # Separando nome e valor do parâmetro.
            splitted_param: list = param.split(":") 
            param_name: str = "/" + str(splitted_param[0])
            param_value = splitted_param[1]

            if(param_name != "/uart_amount"):
                self.store_param(param_name,str(param_value))
            else:
                self.store_param(param_name,int(param_value))

    ## Método que carrega o arquivo de configuração correto.
    def load_config_file(self,launch_mode: str):
        if(launch_mode == "pc"):
            config_file: TextIOWrapper = open(const_current_folder_location + "config/launch_pc.cfg", 'r')
            self.process_config_file(config_file)
            config_file.close()
            print(set_color(const_blue,"-> Running in PC mode."))
        elif(launch_mode == "robot"):
            config_file: TextIOWrapper = open(const_current_folder_location + "config/launch.cfg", 'r')
            self.process_config_file(config_file)
            config_file.close()
            print(set_color(const_blue,"-> Running in ROBOT mode."))
        else:
            print(set_color(const_error,"Invalid launch mode."))
            print(set_color(const_error,"Aborting config_launcher.py ..."))
            exit(0)

    ## Método que verifica qual é o modo de launch em que será rodado o sistema e chama a função para carregar as variáveis de launcher adequadas.
    def read_launch_mode(self):
        launch_mode_file: TextIOWrapper = open(const_current_folder_location + "config/mode.cfg", 'r')
        launch_mode = str(launch_mode_file.readline()).splitlines()[0].split(":")[1] # Separação do nome do parâmetro do valor do parâmetro.
        launch_mode_file.close()
        self.load_config_file(launch_mode)

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == "__main__":
    try:
        Config_launcher().read_launch_mode()
    except:
        print(set_color(const_error,"Error on trying to read launcher config files."))