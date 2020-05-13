#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import sys

from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

###############################
#----> Variáveis Globais <----#
###############################

msg = None
pubWebServer = rospy.Publisher('ParamServer', String, queue_size=10)
rospy.init_node('ParamServer', anonymous=True)

####################################
#----> Classe Request Handler <----#
####################################

class RequestHandler_httpd(BaseHTTPRequestHandler):
    #Faz o manejo da mensagem quando existe uma conexão com o app
    #Entrada: Nenhuma
    #Retorno: Nenhum
    #Pré-condição: Nenhuma
    #Pós-condição: Caso exista comunicação com app, a mensagem recebida é enviada para o tópico ROS
    def do_GET(self):
        global msg,pubWebServer
        webServerRequest = None
        webServerRequest = self.requestline
        webServerRequest = webServerRequest[5 : int(len(webServerRequest)-9)]
        msg = str(webServerRequest) #Raw message recieved from smartphone app
        pubWebServer.publish(str(msg))
        msg = None
        return

##############################
#----> Classe Web Server <----#
##############################

class ParamServer():
    def __init__(self):
        try:
            self.serverIp = sys.argv[1]
            self.server_address_httpd = (self.serverIp,8082)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.serverThread = Thread(target=httpd.serve_forever)
            self.serverThread.daemon = True #O servidor é fechado ao fechar o programa
            self.serverThread.start()
        except:
            pass

#######################
#----> Loop Principal <----#
#######################
  
if __name__ == '__main__':
    try:
        paramServer = ParamServer()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        pass