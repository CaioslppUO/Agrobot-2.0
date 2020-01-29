"""
    Version: 1.6.3
    Date: 28/01/2020 , 22:51
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

####################################
#----> Initialization options <----#
####################################

#Option to enable sensors
if(sys.argv[1] == 'True'):
    enableSensors = True
else:
    enableSensors = False

#Option to enable UART communication
    
if(sys.argv[2] == 'True'):
    enableUart = True
else:
    enableUart = False

#Option to decide wich ip use
# 0: Use PC ip, 1: Use robot ip
ipToUse = sys.argv[3]

#Option to enable relays
if(sys.argv[4] == 'True'):
    enableRelays = True
else:
    enableRelays = False

#Ip definer
if(ipToUse == '0'):
    serverIp = '192.168.1.15' ##->Edit this line to run on computer<-##
else: #Default robot ip
    serverIp = '192.168.1.2'
    
print('Server Ip:' + serverIp)

##############################
#----> Global Variables <----#
##############################

msgRecievedFromApp = ''
speed                = 0
steer                = 0
limit                = 0
powerBoardA          = 0
powerBoardB          = 0
pulverizer           = 0
uartAmount           = sys.argv[5]

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
lastPulverizeSignal = 0

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

def controlRobot(msg):
    global speed,steer,limit,powerBoardA,powerBoardB,relays,pulverizer,lastPulverizeSignal
    speed,steer,limit,powerBoardA,powerBoardB,pulverizer = comunication.msgSeparator(msg,int(msg[0]))
    #Sending power signal to boards
    relays.sendSignalToBoardOne(powerBoardA)
    relays.sendSignalToBoardTwo(powerBoardB)
    #Sending power signal to relay
    relays.sendSignalToPulverizer(pulverizer)
    #Writing in the screen the actual values
    outputMsg.printManualOutput(str(speed),str(steer),str(limit),str(powerBoardA),str(powerBoardB),str(pulverizer))
    #Moving the robot
    movement.setValues(speed,steer,limit)
    movement.move()

#######################
#----> Main loop <----#
#######################

def mainLoop():
    comunicationAttempts = 0
    global msgRecievedFromApp,comunication
    while True:
        msgRecievedFromApp = comunication.getMsg()
        if(msgRecievedFromApp):
            controlRobot(msgRecievedFromApp)
            time.sleep(0.1)
        else:
            print('No message recieved. Attempt: ' + str(comunicationAttempts))
            comunicationAttempts = comunicationAttempts + 1
            time.sleep(1.5)
            
if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')