#!/usr/bin/env python

"""
Modulo que pega os valores do sensor e publica
"""

# ------------- #
# -> Imports <- #
# ------------- #

from __future__ import print_function
import time, sys, signal, atexit, math
from upm import pyupm_bmm150 as sensorObj

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_angle = rospy.Publisher("angle", String, queue_size=10)
const_pub_log = rospy.Publisher("log", String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('angle', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que executa as rotinas de pegar os valores do acelerômetro e publicar no tópico angle.
def main():
  sensor = sensorObj.BMM150(0, 0x13)

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

    heading_degrees = heading * 180/(math.pi);
    const_pub_angle.publish(heading_degrees)
    time.sleep(.250)


# ------------------------ #
# -> Execução de código <- #
# ------------------------ #

if __name__ == '__main__':
  try:
    const_pub_log.publish("startedFile$take_angle.py")
    main()
  except KeyboardInterrupt:
    const_pub_log.publish("error$Warning$take_angle.py finalized.")
