#!/usr/bin/env python3

"""
Módulo que gerencia a comunicação com o app de celular de controle manual.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import rospy,sys
from std_msgs.msg import String
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação no tópico web_server_manual.
const_pub_web_server = rospy.Publisher('web_server_manual', String, queue_size=10)
## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Iniciando o nó web_server_manual.
rospy.init_node('web_server_manual', anonymous=True)

# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerencia os requests feito no servidor http.
class RequestHandler_httpd(BaseHTTPRequestHandler):
    ## Método que trata o GET feito pelo app de controle manual.
    def do_GET(self):
        web_server_request = None
        msg = None
        web_server_request = self.requestline
        web_server_request = web_server_request[5 : int(len(web_server_request)-9)]
        msg = str(web_server_request) # Mensagem crua recebida do app.
        const_pub_web_server.publish(msg)
        return

## Classe que gerencia o servidor http.
class Web_server():
    ## Método que inicializa as variáveis e o servidor.
    def __init__(self):
        try:
            ## Ip no qual será aberto o servidor.
            self.server_ip = sys.argv[1]
            self.server_address_httpd = (self.server_ip,8080)
            httpd = HTTPServer(self.server_address_httpd, RequestHandler_httpd)
            self.server_thread = Thread(target=httpd.serve_forever)
            self.server_thread.daemon = True # O servidor é fechado ao finalizar o programa.
            self.server_thread.start()
        except:
            const_pub_log.publish("error$Fatal$web_server.py could not run.")
            pass

# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
  
if __name__ == '__main__':
    try:
        web_server = Web_server()
        const_pub_log.publish('startedFile$web_server.py')
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        const_pub_log.publish("error$Fatal$web_server.py stoped working.")
