import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time
import subprocess

from comunication.Comunication import Comunication
from complements.Sensors import Sensor
from movement.Movement import Movement
from complements.OutputMsgs import OutMsg
from movement.Controls import Controls

#Communication class
cm = Comunication()

#Options to enable sensors and UART communication
if(sys.argv[1] == 'True'):
    enableSensors = True
else:
    enableSensors = False
    
if(sys.argv[2] == 'True'):
    enableUart = True
else:
    enableUart = False

#0: Use PC ip, 1: Use robot ip
ipToUse = sys.argv[3]

#Movement class
mv = Movement(enableSensors, enableUart)

#Controls class
ctr = Controls(enableSensors,enableUart)

#OutMessages class
ot = OutMsg()

#Message recieved from server
msg = ''

#Web server ip get from computer
if(ipToUse == '0'):
    serverIp = str(str(str(str(str(str(subprocess.check_output(['ifconfig'])).split('UP,BROADCAST,RUNNING,MULTICAST')[1]).split('inet')[1])).split('netmask')[0]).split(' ')[1])
else:
    serverIp = '192.168.1.2'

#Manual control
speed                = 0
steer                = 0
limit                = 0
powerBoardA          = 0
powerBoardB          = 0

#Control mode
controlMode          = 'none'

#Mission control
compass              = 0
missionAngle         = 0
distanceBetwenPoints = 0

#distanceSensors
sensorsCoefficiente  = 0 #Falta definir onde receber da msg

#Web Server
server_address_httpd = (serverIp,8080)
httpd = HTTPServer(server_address_httpd, cm.RequestHandler_httpd)
serverThread = Thread(target=httpd.serve_forever)
serverThread.daemon = True
serverThread.start()
print('Server started')

#Set variables to use on manual control
def setManualControl():
    global msg,speed,steer,limit,powerBoardA,powerBoardB,ss,ot,flagBoardA,flagBoardB;
    #print('Manual control')
    speed       = int(msg[0])
    steer       = int(msg[1])
    limit       = int(msg[2])
    powerBoardA = int(msg[3])
    powerBoardB = int(msg[4])
    ot.printManualOutput(str(speed),str(steer),str(limit))
    mv.setValues(speed,steer,limit)
    mv.move()

#Set variables to use on mission control
def setMissionControl():
    global msg,compass,missionAngle,distanceBetwenPoints;
    print('Mision control')
    #compass              = float(msg[6])
    #missionAngle         = float(msg[7])
    #distanceBetwenPoints = float(msg[8])

#Set the control mode for the robot
def setControl(value):
    global speed;
    if(value == 'manual'):
        #setManualControl()
        ctr.testInterface()
    elif(value == 'mission'):
        setMissionControl()
    else:
        print('Control mode not defined: ' + str(value))

#Main loop
def mainLoop():
    attempts = 0
    global msg,cm;
    while True:
        msg = cm.getMsg()
        if(msg):
            controlMode = msg[5]
            setControl(controlMode)
            time.sleep(0.02)
        else:
            print('No message recieved. Attempt: ' + str(attempts))
            attempts = attempts + 1
            time.sleep(1.5)
if __name__ == "__main__":
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('Program finalized')