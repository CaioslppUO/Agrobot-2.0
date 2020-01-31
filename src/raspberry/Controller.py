"""
    Version: 2.0.0
    Date: 31/01/2020 , 10:46
    Developers: Caio, Lucas, Levi
"""

#####################
#----> Imports <----#
#####################

#Main imports
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time

#Libs imports
from comunication.Comunication import Comunication
from movement.Movement import Movement
from complements.OutputMsgs import OutMsg
from complements.Relay import Relay
from comunication.LaunchInterface import LauncherInterface

##############################
#----> Global Variables <----#
##############################

uartAmount           = "None"
serverIp             = "None"
enableSensors        = "None"
enableUart           = "None"
enableRelays         = "None"

##################################
#----> Classes Declarations <----#
##################################

#LauncherInterface class
launcher = LauncherInterface()

###########################################
#----> Launcher variables definition <----#
###########################################

enableSensors,enableUart,enableRelays,serverIp,uartAmount = launcher.getInputVariables()

##################################
#----> Classes Declarations <----#
##################################

#Communication class
comunication = Comunication()

#Movement class
movement = Movement(enableSensors, enableUart, uartAmount)

#OutMessages class
outputMsg = OutMsg()

#Relay class
relays = Relay(enableRelays)

########################
#----> Web Server <----#
########################

server_address_httpd = (serverIp,8080)
httpd = HTTPServer(server_address_httpd, comunication.RequestHandler_httpd)
serverThread = Thread(target=httpd.serve_forever)
serverThread.daemon = True #The server is closed when the program is closed
serverThread.start()
print('Server started')

##############################
#----> Robot management <----#
##############################

def controlRobot(msg,enableOutPutMessage):
    global relays,comunication
    speed                = "None"
    steer                = "None"
    limit                = "None"
    powerBoardA          = "None"
    powerBoardB          = "None"
    pulverizer           = "None"
    speed,steer,limit,powerBoardA,powerBoardB,pulverizer = comunication.msgSeparator(msg,int(msg[0]))

    #Sending power signal to boards
    relays.sendSignalToBoardOne(powerBoardA)
    relays.sendSignalToBoardTwo(powerBoardB)

    #Sending power signal to relay
    relays.sendSignalToPulverizer(pulverizer)

    if(enableOutPutMessage == True):
        #Writing in the screen the actual values 
        outputMsg.printManualOutput(str(speed),str(steer),str(limit),str(powerBoardA),str(powerBoardB),str(pulverizer))

    #Moving the robot
    movement.setValues(speed,steer,limit)
    movement.move()

#######################
#----> Main loop <----#
#######################

def mainLoop():
    msgRecievedFromApp   = "None"
    comunicationAttempts = 0
    global comunication,serverIp
    print('Server Ip:' + serverIp)
    while True:
        msgRecievedFromApp = comunication.getMsg()
        if(msgRecievedFromApp):
            controlRobot(msgRecievedFromApp,True)
            time.sleep(0.1)
            comunicationAttempts = 0
        else:
            controlRobot("0",False)
            print('No message recieved. Attempt: ' + str(comunicationAttempts))
            comunicationAttempts = comunicationAttempts + 1
            time.sleep(1.5)
            
if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')