#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com o app de celular de controle manual.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy
from agrobot_msgs.msg import CompleteControl,Log
from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação no tópico web_server_manual.
const_pub_web_server: rospy.Publisher = rospy.Publisher('web_server_manual', CompleteControl, queue_size=10)
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

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Iniciando o nó web_server_manual.
rospy.init_node('web_server_manual', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que faz logs.
def do_log(log_type: str,source_file: str,severity: str ="",msg: str ="",where: str =""):
    log: Log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que pinta um texto com a cor passada como argumento e retorna o resultado.
def set_color(color: str,text: str):
    return color + text + const_end_color

## Função que recupera uma variável do rosparam.
def get_param(param_name: str):
    if(rospy.has_param(param_name)):
        return rospy.get_param(param_name)

    print(set_color(const_error,"[Error] "), end='')
    print("Error trying to get the parameter: " + param_name)
    print(set_color(const_error,"[Aborting] "), end='')
    print("web_server.py")
    exit(0)

## Função que finaliza o módulo ao receber o comando certo no tópico shutdown.
def callback_shutdown(file_to_shutdown):
    if(str(file_to_shutdown.data) == "shutdown_web_server"):
        do_log("error","web_server.py","Warning","Web server finalized.","function callback_shutdown()")
        rospy.signal_shutdown("Web server finalized")
        exit(0)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerencia os requests feito no servidor http.
class RequestHandler_httpd(BaseHTTPRequestHandler):
    ## Método que sepera a string recebida pelo app de controle manual e retorna um objeto do tipo CompleteControl já preenchido
    def msg_splitter(self,separator: str,parameters: str) -> CompleteControl:
        control_command: CompleteControl = CompleteControl()
        splitted_parameters: list = parameters.split(separator)
        for param in splitted_parameters:
            try:
                complete_param: str = param.split("$")
                param_name: str = str(complete_param[0])
                param_value: str = complete_param[1]
                if(param_name == "speed"):
                    control_command.control.speed = int(param_value)
                elif(param_name == "steer"):
                    control_command.control.steer = int(param_value)
                elif(param_name == "limit"):
                    control_command.control.limit = int(param_value)
                elif(param_name == "powerA"):
                    control_command.relay.power_a = str(param_value)
                elif(param_name == "powerB"):
                    control_command.relay.power_b = str(param_value)
                elif(param_name == "pulverize"):
                    control_command.relay.power_pulverize = str(param_value)
            except:
                do_log("error","web_server.py","Warning","The parameter " + param + " could not be loaded.", "Method msg_splitter()")
        return control_command

    ## Método que trata o GET feito pelo app de controle manual.
    def do_GET(self):
        web_server_request = None
        web_server_request = self.requestline
        web_server_request = web_server_request[5 : int(len(web_server_request)-9)]
        const_pub_web_server.publish(self.msg_splitter("*",str(web_server_request)))
        return

## Classe que gerencia o servidor http.
class Web_server():
    ## Método que inicializa as variáveis e o servidor.
    def __init__(self):
        try:
            ## Ip no qual será aberto o servidor.
            self.server_ip: str = str(get_param("/server_ip"))
            self.server_address_httpd = (self.server_ip,8080)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.server_thread = Thread(target=httpd.serve_forever)
            self.server_thread.daemon = True # O servidor é fechado ao finalizar o programa.
            self.server_thread.start()
            rospy.Subscriber("shutdown", String, callback_shutdown)
        except:
            do_log("error","web_server.py","Fatal","Could not run web_server.py","class Web_server, method __init__()")

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
  
if __name__ == '__main__':
    try:
        do_log("started_file","[optional] web_server.py")
        Web_server()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        do_log("error","web_server.py","Fatal","Module interrupted: web_server.py.","main")
