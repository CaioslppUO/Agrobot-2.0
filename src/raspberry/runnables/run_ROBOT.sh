#!/bin/bash

python3 /home/labiot/Agrobot-2.0/src/raspberryRos/controller.py serverIp:192.168.1.2 enableUart:True enableSensor:False enableRelay:True uartAmount:2 commandObservers:1 enableFaceDetect:False rootPath:/home/labiot/Agrobot-2.0/src/raspberryRos/
