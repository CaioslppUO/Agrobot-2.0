#!/usr/bin/env python3

#####################
#----> Imports <----#
#####################

import rospy
import sys

from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

##############################
#----> Global Variables <----#
##############################

msg = None
pubWebServer = rospy.Publisher('WebServerManual', String, queue_size=10)
rospy.init_node('WebServerManual', anonymous=True)

###################################
#----> Request Handler Class <----#
###################################

class RequestHandler_httpd(BaseHTTPRequestHandler):
    #Handle the message when there is a connection with the app
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
#----> Web Server Class <----#
##############################

class WebServer():
    def __init__(self):
        try:
            self.serverIp = sys.argv[1]
            self.server_address_httpd = (self.serverIp,8080)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.serverThread = Thread(target=httpd.serve_forever)
            self.serverThread.daemon = True #The server is closed when the program is closed
            self.serverThread.start()
        except:
            pass

#######################
#----> Main Loop <----#
#######################
  
if __name__ == '__main__':
    try:
        webServer = WebServer()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        pass