#!/bin/bash
sleep 60
caminho="/home/labiot/Agrobot-2.0/src/lidar/"
source /opt/ros/melodic/setup.bash && ${caminho}./launchLidar.sh & python3 ${caminho}lidarReader.py& python3 ${caminho}paramServer.py& python3 ${caminho}readerParamsControlLidar.py&

