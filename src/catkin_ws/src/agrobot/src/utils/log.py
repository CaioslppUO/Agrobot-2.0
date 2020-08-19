#!/usr/bin/env python3

"""
Módulo que gerencia a montagem e distribuição dos comandos para os devidos gerênciadores de dispositivos(hardware).
"""

# ------------- #
# -> Imports <- #
# ------------- #

from agrobot_msgs.msg import Log

# ---------------- #
# -> Constantes <- #
# ---------------- #

## Instância que controla a publicação de logs.
const_pub_log: rospy.Publisher = rospy.Publisher('log', Log, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

## Inicializando o nó command_decider.
rospy.init_node('do_log', anonymous=True) 

# ------------- #
# -> Classes <- #
# ------------- #

## Gerencia a publicação de logs
class Log:
    def __init__(self,source_file: str) -> None:
        self.source_file = file

    def do_log(log_type: str,severity: str ="",msg: str ="",where: str =""):
        log: Log = Log()
        log.type = log_type
        log.file = this.source_file
        log.severity = severity
        log.msg = msg
        log.where = where
        const_pub_log.publish(log)