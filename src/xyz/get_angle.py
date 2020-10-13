#!/usr/bin/env python

from __future__ import print_function
import time, sys, signal, atexit, math
from upm import pyupm_bmm150 as sensor_obj
import rospy
from std_msgs.msg import String

## Instância que controla a publicação de logs.
const_pub_control = rospy.Publisher('control_robot', String, queue_size=10)

## Inicializando o nó xyz.
rospy.init_node('xyz', anonymous=True) 

vel = "50"

def direita():
  print("Direita")
  return vel+"$5$100$0"

def esquerda():
  print("Esquerda")
  return vel+"$-5$100$0"

def reto():
  print("Reto")
  return vel+"$0$100$0"

def main():
  sensor = sensor_obj.BMM150(0, 0x13)

  def SIGINTHandler(signum, frame):
    raise SystemExit

  def exitHandler():
    print("Exiting")
    sys.exit(0)
  
  atexit.register(exitHandler)
  signal.signal(signal.SIGINT, SIGINTHandler)

  sensor.update()
  data = sensor.getMagnetometer()
  xy_heading = math.atan2(data[0], data[1])
  xy_heading = int(xy_heading * 180 / (math.pi))
  if(xy_heading < 0):
    xy_heading = abs(xy_heading+360)
  b = xy_heading
  
  while (1):
    sensor.update()
    data = sensor.getMagnetometer()
    xy_heading = math.atan2(data[0], data[1])
    xy_heading = int(xy_heading * 180 / (math.pi))
    if(xy_heading < 0):
      xy_heading = abs(xy_heading+360)
    print(xy_heading)
    a = xy_heading 
    time.sleep(.250)

    if(a <= b-3 or a >= b+3):
      if(b >= 0 and b <= 90):
        if(a <= 180 and a > b):
          dir = esquerda()
          print("1")
        else:
          dir = direita()
          print("2")
      elif(b > 90 and b <= 270):
        if(a > b):
          dir = esquerda()
          print("3")
        else:
          print("4")
          dir = direita()
      else:
        if(a >= 180 and a < b):
          dir = direita()
          print("5")
        else:
          print("6")
          dir = direita()
    else:
      dir = reto()
    const_pub_control.publish(dir)

main()
