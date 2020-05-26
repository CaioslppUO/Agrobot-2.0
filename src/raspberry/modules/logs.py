#!/usr/bin/env python3

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_log_folder = '../logs/'

const_started_files_path = const_log_folder + 'startedFiles.log'
const_errors_file_path = const_log_folder + 'errors.log'

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('log', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que limpa os arquivos de log ao rodar o programa.
def clean_log_files(files_path):
    for f in files_path:
        file_ = open(f, 'w')
        file_.close()

## Função que escreve a mensagem de erro no arquivo de log.
def write_error(error_severity,error_msg):
    file_ = open(const_errors_file_path, 'a')
    file_.write('[' + error_severity + '] ' + error_msg + '\n')
    file_.close()

## Função que escreve a mensagem de arquivo aberto no arquivo de log.
def write_started(file_name):
    file_ = open(const_started_files_path, 'a')
    file_.write(file_name + ': Started\n')
    file_.close()

## Função que trata a mensagem recebida pelo tópico de log.
def callback(msg):
    info = (msg.data).split('$')

    if(info[0] == "startedFile"):
        write_started(str(info[1]))
    elif(info[0] == "error"):
        write_error(str(info[1]), str(info[2]))

## Função que escuta o tópico de log
def listen():
    rospy.Subscriber('log', String, callback)
    rospy.spin()

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

#Limpando os arquivos de log
clean_log_files([const_started_files_path,const_errors_file_path])
listen()