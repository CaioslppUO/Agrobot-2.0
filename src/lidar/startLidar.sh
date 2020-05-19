#!/bin/bash
# sleep 60
caminho="/home/labiot/Agrobot-2.0/src/lidar/"

echo "executando lidar" 
${caminho}./launchLidar.sh &
sleep 6
echo "executando lidarReader" 
python3 ${caminho}lidarReader.py &
sleep 3
echo "executando paramServer" 
python3 ${caminho}paramServer.py &
sleep 3
echo "executando readerParamsControllLidar" 
python3 ${caminho}readerParamsControlLidar.py &
sleep 3
echo "executando controlLidar" 
python3 ${caminho}controlLidar.py &