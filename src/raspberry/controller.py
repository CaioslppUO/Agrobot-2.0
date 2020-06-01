#!/usr/bin/env python3

""" 
Programa que gerencia quais e como serão executados todos os módulos do sistema.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import os,sys,rospy,time
from std_msgs.msg import String
from launcher_variables import Launcher_variables

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

# Inicialização do ROS.
os.system("roscore& ")
time.sleep(8)
os.system("clear && echo '-> Roscore has been successfully initialized.'& ")

## Iniciando o nó controller.
rospy.init_node('controller', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que processa as variáveis de inicialização e inicia os módulos que foram requeridos.
def main_loop():
    # Classe que gerência as variáveis de inicialização.
    launcher = Launcher_variables()
    # Variáveis de inicialização.
    server_ip,enable_uart,enable_relay,uart_amount,enable_faceDetect,root_path = launcher.variable_separator(sys.argv)

    # Commando para executar um arquivo do projeto em python3.
    run_py3 = "python3 " + root_path

    # Define quais módulos base serão inicializados.
    os.system("python3 " + root_path + "modules/logs.py& ")
    print('Startind modules ...')
    time.sleep(10)

    # Módulos principais(essênciais).
    launch_msg = run_py3 + "comunication/web_server.py " + server_ip + "& "
    launch_msg += run_py3 + "comunication/command_priority_decider.py& "
    launch_msg += run_py3 + "modules/command_assembler.py& "
    
    # Módulos opcionais.
    if(enable_relay == "True"):
        launch_msg += run_py3 + "modules/relay.py& "
    if(enable_uart == "True"):
        launch_msg += run_py3 + "modules/control_robot.py " + str(uart_amount) + "& "
    if(enable_faceDetect == "True"):
        launch_msg += run_py3 + "modules/computational_vision.py& "

    # Inicializa os módulos que foram requeridos.
    os.system(launch_msg)
    
    # Publica no tópico de logs que o arquivo controller.py foi inicializado.
    const_pub_log.publish("startedFile$controller.py")
    time.sleep(5)
    
    # Mostra na tela quais módulos foram abertos.
    print('\n-> Open modules: \n')
    os.system('cat ' + root_path + "logs/startedFiles.log")

    # Mostra na tela os erros que ocorreram.
    print('\n\n-> Errors: \n')
    os.system('cat ' + root_path + "logs/errors.log")

    # Indica a situação atual do sistema.
    print('\n-> Status: Running')
    
    # Impede o terminal de finalizar.
    while not rospy.is_shutdown():
        rospy.spin()

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        const_pub_log.publish("error$Warning$Program finalized")
        print('Program finalized')
