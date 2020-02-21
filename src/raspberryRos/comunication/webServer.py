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
pub = rospy.Publisher('WebServer', String, queue_size=10)
rospy.init_node('WebServer', anonymous=True)

###################################
#----> Request Handler Class <----#
###################################

class RequestHandler_httpd(BaseHTTPRequestHandler):
    def do_GET(self):
        newClientConnectionAttenpts = 0
        clientAdress = None
        webServerRequest = None
        global msg,pub
        webServerRequest = self.requestline
        if(clientAdress == None or newClientConnectionAttenpts >= 15):
            clientAdress = self.client_address[0]
        if(clientAdress == self.client_address[0]):
            newClientConnectionAttenpts = 0
            webServerRequest = webServerRequest[5 : int(len(webServerRequest)-9)]
            #Geting speed,steer and limit
            msg = str(webServerRequest) #Message recieved from smartphone app
            pub.publish(str(msg))
            msg = None
            return
        else:
            newClientConnectionAttenpts = newClientConnectionAttenpts + 1


##############################
#----> Web Server Class <----#
##############################
class WebServer():
    def __init__(self):
        self.serverIp = sys.argv[1]
        self.server_address_httpd = (self.serverIp,8080)
        httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
        self.serverThread = Thread(target=httpd.serve_forever)
        self.serverThread.daemon = True #The server is closed when the program is closed
        self.serverThread.start()
            
if __name__ == '__main__':
    try:
        webServer = WebServer()
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        pass