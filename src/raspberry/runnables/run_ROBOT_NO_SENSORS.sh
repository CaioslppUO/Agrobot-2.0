#!/bin/bash

#Parameters: EnableSensors EnableUart IpToUse EnableRelays UartAmount
cd .. && sudo python3 Controller.py enableSensors:False enableRelays:True serverIp:192.168.1.2 enableUart:True uartAmount:2
