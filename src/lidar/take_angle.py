#!/usr/bin/env python
"""
Modulo que pega os valores do sensor e publica
"""
#####################
#----> Imports <----#
#####################
from __future__ import print_function
import time, sys, signal, atexit, math
from upm import pyupm_bmm150 as sensorObj

# ---------------- #
# -> Constantes <- #
# ---------------- #
pub_angle = rospy.Publisher("angle", String,queue_size=10)


# ------------------- #
# -> Configurações <- #
# ------------------- #
rospy.init_node('angle', anonymous=True)
rospy.Publisher("Log",Strin,queue_size=10).publish("startedFile$take_angle")


# ------------- #
# -> Funções <- #
# ------------- #
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
    xyHeading = math.atan2(data[0], data[1])
    zxHeading = math.atan2(data[2], data[0])
    heading = xyHeading
    if heading < 0:
      heading += 2*math.pi
    if heading > 2*math.pi:
      heading -= 2*math.pi
    headingDegrees = heading * 180/(math.pi);
    pub_angle.publish(headingDegrees)
    # print('heading(axis_Y point to): {0:.2f} degree'.format(headingDegrees))
    time.sleep(.250)


# ------------------------ #
# -> Execução de código <- #
# ------------------------ #
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    rospy.Publisher("Log",String,queue_size=10).publish("error$Warning$Program finalized")
    print('Program finalized')
