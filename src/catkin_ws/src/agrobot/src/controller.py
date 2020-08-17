#!/usr/bin/env python3

""" 
Programa que gerencia quais e como serão executados todos os módulos do sistema.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import os,rospy,time,pathlib
from agrobot_msgs.msg import Log
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)
## Constante que pinta o texto de azul.
const_blue: str = '\033[94m'
## Constante que pinta o texto de verde.
const_green: str = '\033[92m'
## Constante que pinta o texto de vermelho.
const_error: str = '\033[91m'
## Constante finaliza a pintura do texto.
const_end_color: str = '\033[0m'
## Constante que guarda a localização na qual este arquivo se encontra.
const_folder_location: str = str(pathlib.Path(__file__).parent.absolute()) + "/"

# ------------------- #
# -> Configurações <- #
# ------------------- #

# Limpa a tela inicial do ROS.
os.system("clear& ")

## Iniciando o nó controller.
rospy.init_node('controller', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que pinta um texto com a cor passada como argumento e retorna o resultado.
def set_color(color: str,text: str):
    return color + text + const_end_color

## Função que faz logs.
def do_log(log_type: str,source_file: str,severity: str ="",msg: str ="",where: str =""):
    log: Log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que recupera uma variável do rosparam.
def get_param(param_name: str):
    if(rospy.has_param(param_name)):
        return rospy.get_param(param_name)
    
    print(set_color(const_error,"[Error] "), end='')
    print("Error trying to get the parameter: " + param_name)
    print(set_color(const_error,"[Aborting] "), end='')
    print("controller.py")
    exit(0)

## Função que inicia os módulos requeridos pelas variáveis de configuração de launch.
def launch_modules(root_path: str,enable_uart: str,enable_relay: str,enable_face_detect: str):
    # Commando para executar um arquivo do projeto em python3.
    run_py3: str = "python3 " + root_path

    # Define quais módulos base serão inicializados.
    os.system(run_py3 + "modules/logs.py& ") # Inicia primeiramente o módulo de logs, para registrar possíveis bugs de execução.

    print(set_color(const_blue,"-> Starting modules ..."))
    time.sleep(10)

    # Módulos principais(essênciais).
    launch_msg: str = run_py3 + "comunication/web_server.py& "
    launch_msg += run_py3 + "comunication/command_priority_decider.py& "
    launch_msg += run_py3 + "modules/command_assembler.py& "
    
    # Módulos opcionais.
    if(enable_relay == "True"):
        launch_msg += run_py3 + "modules/relay.py& "
    if(enable_uart == "True"):
        launch_msg += run_py3 + "modules/control_robot.py& "
    if(enable_face_detect == "True"):
        launch_msg += run_py3 + "modules/computational_vision.py& "

    # Inicializa os módulos que foram requeridos.
    os.system(launch_msg)

## Função que finaliza o módulo ao receber o comando certo no tópico shutdown.
def callback_shutdown(file_to_shutdown):
    if(str(file_to_shutdown.data) == "shutdown"):
        do_log("error","controller.py","Warning","ROS finalized","function callback_shutdown()")
        os.system("pkill ros")
        rospy.signal_shutdown("ROS finalized")
        exit(0)

## Função que carrega as variáveis de inicialização e inicia os módulos que foram requeridos.
def main_loop():
    print(set_color(const_green,"[OK] "), end='')
    print("Roscore has been successfully initialized.")

    # Carregando as variáveis de launch.
    os.system("python3 " + const_folder_location + "config_launcher.py")
    time.sleep(5)

    # Definindo as variáveis de launch.
    root_path: str = const_folder_location
    enable_uart: str = str(get_param("/enable_uart"))
    enable_relay: str = str(get_param("/enable_relay"))
    enable_face_detect: str = str(get_param("/enable_face_detect"))

    print(set_color(const_green,"[OK] "), end='')
    print("Config file read successfully.")

    # Inicializando os módulos que foram requeridos.
    launch_modules(root_path,enable_uart,enable_relay,enable_face_detect)
    
    # Publica no tópico de logs que o arquivo controller.py foi inicializado.
    do_log("started_file","[essential] controller.py")
    time.sleep(5)
    
    # Mostra na tela quais módulos foram abertos.
    print(set_color(const_blue,"\n-> Open modules: \n"))
    os.system('cat ' + root_path + "logs/started_files.log")

    # Mostra na tela os erros que ocorreram.
    print(set_color(const_blue,"\n\n-> Errors: \n"))
    os.system('cat ' + root_path + "logs/errors.log")

    # Indica a situação atual do sistema.
    print("\n-> Status: " + set_color(const_green,"Running"))
    
    # Impede o terminal de finalizar.
    while not rospy.is_shutdown():
        rospy.Subscriber("shutdown", String, callback_shutdown)
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        do_log("error","controller.py","Warning","Program finalized","main")
        print('Program finalized')

