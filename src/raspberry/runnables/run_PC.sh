#!/bin/bash

#Parameters: EnableSensors EnableUart IpToUse EnableRelays UartAmount
cd .. && sudo python3 Controller.py enableUart:False enableRelays:False serverIp:192.168.1.15 enableSensors:False uartAmount:0
