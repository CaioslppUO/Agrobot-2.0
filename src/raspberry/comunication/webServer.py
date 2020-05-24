#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com o app de celular de controle manual.
"""

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
pubWebServer = rospy.Publisher('WebServerManual', String, queue_size=10)
pubLog = rospy.Publisher('Log', String, queue_size=10)
rospy.init_node('WebServerManual', anonymous=True)

####################################
#----> Classe Request Handler <----#
####################################

## Classe que gerencia os requests feito no servidor http.
class RequestHandler_httpd(BaseHTTPRequestHandler):
    ## Método que trata o GET feito pelo app de controle manual.
    def do_GET(self):
        newClientConnectionAttenpts = 0
        clientAdress = None
        webServerRequest = None
        global msg,pubWebServer
        webServerRequest = self.requestline
        if(clientAdress == None or newClientConnectionAttenpts >= 15):
            clientAdress = self.client_address[0]
        if(clientAdress == self.client_address[0]):
            newClientConnectionAttenpts = 0
            webServerRequest = webServerRequest[5 : int(len(webServerRequest)-9)]
            msg = str(webServerRequest) #Raw message recieved from smartphone app
            pubWebServer.publish(str(msg))
            msg = None
            return
        else:
            newClientConnectionAttenpts = newClientConnectionAttenpts + 1

##############################
#----> Classe Web Server <----#
##############################

## Classe que gerencia o servidor http
class WebServer():
    ## Método que inicializa as variáveis e o servidor
    def __init__(self):
        try:
            ## Ip no qual será aberto o servidor.
            self.serverIp = sys.argv[1]
            self.server_address_httpd = (self.serverIp,8080)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.serverThread = Thread(target=httpd.serve_forever)
            self.serverThread.daemon = True #O servidor é fechado ao fechar o programa
            self.serverThread.start()
        except:
            pass

############################
#----> Loop Principal <----#
############################
  
if __name__ == '__main__':
    try:
        webServer = WebServer()
        pubLog.publish('startedFile$WebServer')
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        pass