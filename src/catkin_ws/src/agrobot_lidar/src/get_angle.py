#!/usr/bin/env python

"""
Modulo que pega os valores do sensor e publica
"""

# ------------- #
# -> Imports <- #
# ------------- #

from __future__ import print_function
import time, sys, signal, atexit, math, rospy
from agrobot_msgs.msg import Automatic,Log
from upm import pyupm_bmm150 as sensor_obj


# ---------------- #
# -> Constantes <- #
# ---------------- #

## Variável que controla a publicação no tópico da angle.
const_pub_angle = rospy.Publisher("angle", Automatic, queue_size=10)
## Instância que controla a publicação de logs.
const_pub_log = rospy.Publisher('log', Log, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('angle', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que faz logs.
  def do_log(log_type,source_file,severity="",msg="",where=""):
    log = Log()
    log.type = log_type
    log.file = source_file
    log.severity = severity
    log.msg = msg
    log.where = where
    const_pub_log.publish(log)

## Função que executa as rotinas de pegar os valores do acelerômetro e publicar no tópico angle.
def main():
  sensor = sensor_obj.BMM150(0, 0x13)
  heading_degrees = Automatic()

  def SIGINTHandler(signum, frame):
    raise SystemExit

  def exitHandler():
    print("Exiting")
    sys.exit(0)
  
  atexit.register(exitHandler)
  signal.signal(signal.SIGINT, SIGINTHandler)
  
  while (1):
    sensor.update()
    data = sensor.getMagnetometer()
    xy_heading = math.atan2(data[0], data[1])
    zx_heading = math.atan2(data[2], data[0])
    heading = xy_heading

    if heading < 0:
      heading += 2*math.pi
    if heading > 2*math.pi:
      heading -= 2*math.pi


    heading_degrees.correction_magnitude = heading * 180/(math.pi);
    const_pub_angle.publish(heading_degrees)
    time.sleep(.250)


# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
try:
  do_log("started_file","[optional] get_angle.py")
  main()
except KeyboardInterrupt:
  do_log("KeyBoard Interrupt","get_angle.py","Fatal","Module interrupted: get_angle.py","main")