#!/bin/bash
sleep 30
caminho="/home/labiot/Agrobot-2.0/src/lidar/"

source /opt/ros/melodic/setup.bash
source /home/labiot/catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://192.168.1.2:11311
export ROS_IP=192.168.1.121

${caminho}./launchLidar.sh &
sleep 10
python3 ${caminho}lidarReader.py &
sleep 7
python3 ${caminho}paramServer.py &
sleep 7
python3 ${caminho}walkAndStop.py &
sleep 7
python3 ${caminho}controlLidar.py &

#/etc/init.d/script