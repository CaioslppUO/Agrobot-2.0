#!/usr/bin/env python3

import rospy
from threading import Thread
from std_msgs.msg import String

vel = 100
limite = 40
direction = 0
perto = 0.5
medio = 2.0
longe = 7.0

pointDirection = split('$')
def move():
    print("B")

def correctDirection():
    print("c")

def main():
    print('a')

def callback():
    print("ola mundo")

sub = rospy.Subscriber('/Lidar', String, callback)