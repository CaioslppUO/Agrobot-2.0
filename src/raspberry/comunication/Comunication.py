from http.server import BaseHTTPRequestHandler, HTTPServer

msg = ''
msgSeparator = '*'

#Web server
request = None

class Comunication(BaseHTTPRequestHandler):
    def __init__(self):
        self.msg = ''
    
    def getMsg(self):
        global msg;
        self.msg = msg;
        return msg
    
    def msgSeparator(self,msg,msgSize):
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
        return int(self.speed),int(self.steer),int(self.limit),int(self.powerA),int(self.powerB),int(self.pulverizer)

    class RequestHandler_httpd(BaseHTTPRequestHandler):
        def do_GET(self):
            global msg,msgSeparator;
            request = self.requestline
            request = request[5 : int(len(request)-9)]
            #Geting speed,steer and limit
            msg = str(request).split(msgSeparator) #Message recieved from smartphone app
            return

    