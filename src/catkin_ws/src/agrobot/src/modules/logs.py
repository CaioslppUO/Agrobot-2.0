#!/usr/bin/env python3

# ------------- #
# -> Imports <- #
# ------------- #

import rospy,pathlib
from agrobot_msgs.msg import Log
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_log_folder: str = str(pathlib.Path(__file__).parent.absolute()) + "/../logs/"
const_started_files_path: str = const_log_folder + 'started_files.log'
const_errors_file_path: str = const_log_folder + 'errors.log'

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Iniciando o nó log.
rospy.init_node('log', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que finaliza o módulo ao receber o comando certo no tópico shutdown.
def callback_shutdown(file_to_shutdown):
    if(str(file_to_shutdown.data) == "shutdown_logs"):
        log: Log = Log()
        log.type = "error"
        log.severity = "Warning"
        log.msg = "Logs finalized."
        log.file = "logs.py"
        log.where = "function callback_shutdown()"
        rospy.signal_shutdown("Logs finalized")
        exit(0)

## Função que limpa os arquivos de log ao rodar o programa.
def clean_log_files(files_path: list):
    for f in files_path:
        file_ = open(f, 'w')
        file_.close()

## Função que escreve a mensagem de erro no arquivo de log.
def write_error(error_severity: str,error_msg: str,file_name: str,where: str):
    errors_file = open(const_errors_file_path, 'a')
    errors_file.write('[' + error_severity + '] ' + error_msg + " File: '" + file_name + "', in '" + where + "'" + "\n\n")
    errors_file.close()

## Função que escreve a mensagem de arquivo aberto no arquivo de log.
def write_started(file_name: str):
    started_files_file = open(const_started_files_path, 'a')
    started_files_file.write(" * " + file_name + '\n')
    started_files_file.close()

## Função que trata a mensagem recebida pelo tópico de log.
def callback(log_msg: Log):
    if(log_msg.type == "started_file"):
        write_started(str(log_msg.file))
    elif(log_msg.type == "error"):
        write_error(str(log_msg.severity), str(log_msg.msg), str(log_msg.file), str(log_msg.where))

## Função que escuta o tópico de log.
def listen():
    rospy.Subscriber('log', Log, callback)
    rospy.Subscriber("shutdown", String, callback_shutdown)
    rospy.spin()

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__ == "__main__":
    clean_log_files([const_started_files_path,const_errors_file_path])
    # Escutando os nós que fizerem log.
    listen()