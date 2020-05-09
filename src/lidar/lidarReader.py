#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

frange = [0,45,315,360]
brange = [135,225]
lrange = [44,134]
rrange = [224,314]

mb = int((brange[0] + brange[1])/2)
ml = int((lrange[0] + lrange[1])/2)
mr = int((rrange[0] + rrange[1])/2)

def callback(msg):
    print('Front: ' + str(msg.ranges[0]))
    print('Back: ' + str(msg.ranges[mb]))
    print('Left: ' + str(msg.ranges[ml]))
    print('Right: ' + str(msg.ranges[mr]))

rospy.init_node('lidar_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()