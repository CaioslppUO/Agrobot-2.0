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

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_web_server = rospy.Publisher('param_server', String, queue_size=10)
const_pub_log = rospy.Publisher("log", String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('param_server', anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe Request Handler.
class RequestHandler_httpd(BaseHTTPRequestHandler):
    ## Faz o manejo da mensagem quando existe uma conexão com o app.
    # Caso exista comunicação com app, a mensagem recebida é enviada para o tópico param_server.
    def do_GET(self):
        web_server_request = None
        web_server_request = self.requestline
        web_server_request = web_server_request[5 : int(len(web_server_request)-9)]
        msg = str(web_server_request) # Mensagem que vem do App de celular.
        const_pub_web_server.publish(str(msg))
        msg = None
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
            const_pub_log.publish("error$Fatal$Could not run param_server.py.")

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
##Loop Principal  
if __name__ == '__main__':
    try:
        const_pub_log.publish("startedFile$param_server.py")
        param_server = Param_server()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        const_pub_log.publish("error$Warning$param_server.py finalized.")
