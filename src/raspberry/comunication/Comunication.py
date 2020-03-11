#####################
#----> Imports <----#
#####################

from http.server import BaseHTTPRequestHandler, HTTPServer

from complements.Checks import Checks

##############################
#----> Global Variables <----#
##############################

msg = ''
msgSeparator = '*'
webServerRequest = None
clientAdress = "None"
newClientConnectionAttenpts = 0

################################
#----> Comunication class <----#
################################

class Comunication(BaseHTTPRequestHandler):
    def __init__(self):
        self.msg = ''
        self.speed = "None"
        self.steer = "None"
        self.limit = "None"
        self.powerA = "None"
        self.powerB = "None"
        self.pulverizer = "None"
        self.check = Checks()
    
    def getMsg(self):
        global msg
        self.msg = msg
        msg = ""
        return self.msg
    
    def msgSeparator(self,msg,msgSize,ignoreErrorMessage):
        i = 1
        while(i <= msgSize):
            msgAux = msg[i].split('$')
            if(msgAux[0] == 'speed'):
                self.speed = int(msgAux[1])
            elif(msgAux[0] == 'steer'):
                self.steer = int(msgAux[1])
            elif(msgAux[0] == 'limit'):
                self.limit = int(msgAux[1])
            elif(msgAux[0] == 'powerA'):
                self.powerA = int(msgAux[1])
            elif(msgAux[0] == 'powerB'):
                self.powerB = int(msgAux[1])
            elif(msgAux[0] == 'pulverize'):
                self.pulverizer = int(msgAux[1])
            i = i+1

        if(not self.check.checkAppMsgProtocol(self.speed,self.steer,self.limit,self.powerA,self.powerB,self.pulverizer,ignoreErrorMessage)):
            return 0,0,0,0,0,0

        speed = int(self.speed)
        steer = int(self.steer)
        limit = int(self.limit)
        powerA = int(self.powerA)
        powerB = int(self.powerB)
        pulverizer = int(self.pulverizer)
        self.speed = "None"
        self.steer = "None"
        self.limit = "None"
        self.powerA = "None"
        self.powerB = "None"
        self.pulverizer = "None"
        return speed,steer,limit,powerA,powerB,pulverizer

    class RequestHandler_httpd(BaseHTTPRequestHandler):
        def do_GET(self):
            global msg,msgSeparator,newClientConnectionAttenpts,clientAdress
            webServerRequest = self.requestline
            if(clientAdress == "None" or newClientConnectionAttenpts >= 15):
                clientAdress = self.client_address[0]
            if(clientAdress == self.client_address[0]):
                newClientConnectionAttenpts = 0
                webServerRequest = webServerRequest[5 : int(len(webServerRequest)-9)]
                #Geting speed,steer and limit
                msg = str(webServerRequest).split(msgSeparator) #Message recieved from smartphone app
                return
            else:
                newClientConnectionAttenpts = newClientConnectionAttenpts + 1

    