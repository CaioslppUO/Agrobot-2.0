from http.server import BaseHTTPRequestHandler, HTTPServer

msg = ''
msgSeparator = '.'

#Web server
request = None

class Comunication(BaseHTTPRequestHandler):
    def __init__(self):
        self.msg = ''
    
    def getMsg(self):
        global msg;
        self.msg = msg;
        return msg

    class RequestHandler_httpd(BaseHTTPRequestHandler):
        def do_GET(self):
            global msg,msgSeparator;
            request = self.requestline
            request = request[5 : int(len(request)-9)]
            #Geting speed,steer and limit
            msg = str(request).split(msgSeparator) #Message recieved from smartphone app
            return

    