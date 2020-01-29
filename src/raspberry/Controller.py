"""
    Version: 1.7.0
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

##############################
#----> Global Variables <----#
##############################

msgRecievedFromApp   = "None"
speed                = "None"
steer                = "None"
limit                = "None"
powerBoardA          = "None"
powerBoardB          = "None"
pulverizer           = "None"
uartAmount           = "None"
serverIp             = "None"
enableSensors        = "None"
enableUart           = "None"
enableRelays         = "None"

####################################
#----> Initialization options <----#
####################################

def getInputVariables():
    global enableSensors,enableRelays,enableUart,serverIp,uartAmount
    aux = 1
    while(aux < len(sys.argv)):
        indicator = sys.argv[aux].split(":")
        if(indicator[0] == "enableSensors"):
            if(indicator[1] == "True"):
                enableSensors = True
            else:
                enableSensors = False
        elif(indicator[0] == "enableUart"):
            if(indicator[1] == "True"):
                enableUart = True
            else:
                enableUart = False
        elif(indicator[0] == "serverIp"):
            serverIp = str(indicator[1])
        elif(indicator[0] == "enableRelays"):
            if(indicator[1] == "True"):
                enableRelays = True
            else:
                enableRelays = False
        elif(indicator[0] == "uartAmount"):
            uartAmount = int(indicator[1])
        aux = aux+1
    if(enableSensors == "None" or enableUart == "None" or serverIp == "None" or enableRelays == "None" or uartAmount == "None"):
        print("[Error] The input variables are not correct")
        print("Aborting...")
        exit(1)

getInputVariables()

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
    global msgRecievedFromApp,comunication,serverIp 
    print('Server Ip:' + serverIp)
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