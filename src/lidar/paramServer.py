#!/usr/bin/env python3

"""
Modulo que recebe os dados do App.
"""

#####################
#----> Imports <----#
#####################

import rospy
import sys

from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

# ---------------- #
# -> Constantes <- #
# ---------------- #

##Declaração do nó
pubWebServer = rospy.Publisher('ParamServer', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('ParamServer', anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #


##Classe Request Handler
class RequestHandler_httpd(BaseHTTPRequestHandler):
    ##Faz o manejo da mensagem quando existe uma conexão com o app
    #Caso exista comunicação com app, a mensagem recebida é enviada para o tópico ROS
    def do_GET(self):
        global pubWebServer
        webServerRequest = None
        webServerRequest = self.requestline
        webServerRequest = webServerRequest[5 : int(len(webServerRequest)-9)]
        #Mensagem que vem do App de celular.
        msg = str(webServerRequest) 
        pubWebServer.publish(str(msg))
        msg = None
        return


##Classe Web Server
class ParamServer():
    def __init__(self):
        try:
            self.serverIp = "192.168.1.121"
            self.server_address_httpd = (self.serverIp,8082)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.serverThread = Thread(target=httpd.serve_forever)
            self.serverThread.daemon = True #O servidor é fechado ao fechar o programa
            self.serverThread.start()
        except:
            pass

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
##Loop Principal  
if __name__ == '__main__':
    try:
        rospy.Publisher("Log",Strin,queue_size=10).publish("startedFile$paramServer")
        paramServer = ParamServer()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        pass
