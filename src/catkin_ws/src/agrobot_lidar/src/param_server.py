#!/usr/bin/env python3

"""
Modulo que recebe os dados do App.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy,sys
from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from agrobot_msgs.msg import CommandWebServer,Log


# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação dos commandos que vem do webServer
const_pub_web_server = rospy.Publisher('param_server', CommandWebServer, queue_size=10)
## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', Log, queue_size=10)
# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('param_server', anonymous=True)

## Função que faz logs.
def do_log(log_type,source_file,severity="",msg="",where=""):
    log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe Request Handler.
class RequestHandler_httpd(BaseHTTPRequestHandler):
    def mount_command(self,web_server_command):
        command_web_server = CommandWebServer()
        msg = web_server_command.split('*')
        for variable in msg:
            new_variable = variable.split('$')
            if(new_variable[0] == "limit"):
                command_web_server.limitDefault = int(new_variable[1])
            if(new_variable[0] == "tick"):
                command_web_server.tickDefault = int(new_variable[1])
            if(new_variable[0] == "steer"):
                command_web_server.steerDefault = int(new_variable[1])
            if(new_variable[0] == "speed"):
                command_web_server.speedDefault = int(new_variable[1])
            if(new_variable[0] == "shift"):
                command_web_server.shiftDirection = int(new_variable[1])
            if(new_variable[0] == "uv"):
                command_web_server.uv = int(new_variable[1])
            if(new_variable[0] == "detect"):
                command_web_server.detectDistance = float(new_variable[1])
            if(new_variable[0] == "move"):
                command_web_server.walkTime = int(new_variable[1])
            if(new_variable[0] == "stop"):
                command_web_server.stopTime = int(new_variable[1])
        return command_web_server
    ## Faz o manejo da mensagem quando existe uma conexão com o app.
    # Caso exista comunicação com app, a mensagem recebida é enviada para o tópico param_server.
    def do_GET(self):
        web_server_request = None
        web_server_request = self.requestline
        if(web_server_request != None):
            web_server_request = web_server_request[5 : int(len(web_server_request)-9)]
            const_pub_web_server.publish(self.mount_command(web_server_request))
        return

## Classe Web Server.
class Param_server():
    def __init__(self):
        try:
            self.server_ip = "192.168.1.121"
            self.server_address_httpd = (self.server_ip,8082)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.server_thread = Thread(target=httpd.serve_forever)
            self.server_thread.daemon = True # O servidor é fechado ao fechar o programa.
            self.server_thread.start()
        except:
            do_log("error","param_server.py","Fatal","Could not run param_server.py","class Param_server, method __init__()")

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
##Loop Principal  
if __name__ == '__main__':
    try:
        do_log("started_file","[optional] param_server.py")
        param_server = Param_server()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        do_log("error","param_server.py","Fatal","Module interrupted: param_server.py.","main")
