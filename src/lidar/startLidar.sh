#!/bin/bash
sleep 60
./lauchLidar.sh& && python3 lidarReader.py& && python3 paramServer.py& && python3 readerParamsControlLidar.py& && python3 controlLidar&