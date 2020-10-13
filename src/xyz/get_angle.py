#!/usr/bin/env python


from __future__ import print_function
import time, sys, signal, atexit, math
from upm import pyupm_bmm150 as sensor_obj

def main():
  sensor = sensor_obj.BMM150(0, 0x13)

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
    print(heading_degrees)
    time.sleep(.250)

main()
