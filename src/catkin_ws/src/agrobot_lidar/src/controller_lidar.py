#!/usr/bin/env python3

""" 
Programa que gerencia a execução do lidar.
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
const_pub_log = rospy.Publisher('log', Log, queue_size=10)
## Constante que guarda a localização na qual este arquivo se encontra.
const_folder_location = str(pathlib.Path(__file__).parent.absolute()) + "/"

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Iniciando o nó controller.
rospy.init_node('controller', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que faz logs.
def do_log(log_type,source_file,severity="",msg="",where=""):
    log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que inicia os módulos requeridos pelas variáveis de configuração de launch.
def launch_modules(root_path):
    # Commando para executar um arquivo do projeto em python3.
    run_py3 = "python3 " + root_path

    # Módulos principais(essênciais).
    os.system(root_path + "./launchLidar.sh& ")
    time.sleep(10)
    os.system(run_py3 + "lidarReacer.py& ")
    time.sleep(7)
    os.system(run_py3 + "paramServer.py& ")
    time.sleep(7)
    os.system(run_py3 + "walkAndStop.py& ")
    time.sleep(7)
    os.system(run_py3 + "controlLidar.py& ")

    # Inicializa os módulos que foram requeridos.
    os.system(


## Função que carrega as variáveis de inicialização e inicia os módulos que foram requeridos.
def main_loop():
    # Inicializando os módulos que foram requeridos.
    launch_modules(const_folder_location)
    
    # Publica no tópico de logs que o arquivo controller.py foi inicializado.
    do_log("started_file","[optional] controller_lidar.py")
    time.sleep(5)

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
        do_log("error","controller_lidar.py","Warning","Program finalized","main")

