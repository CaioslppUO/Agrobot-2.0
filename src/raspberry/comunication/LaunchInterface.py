#####################
#----> Imports <----#
#####################

import sys
from complements.Checks import Checks

#####################################
#----> LauncherInterface Class <----#
#####################################

class LauncherInterface:
    def __init__(self,enableSensors,enableUart,enableRelays,serverIp,uartAmount):
        self.check = Checks()
        self.enableSensors = enableSensors
        self.enableUart = enableUart
        self.enableRelays = enableRelays
        self.serverIp = serverIp
        self.uartAmount = uartAmount
    
    #Get the variables from command line arguments
    def getInputVariables(self):
        aux = 1
        while(aux < len(sys.argv)):
            indicator = sys.argv[aux].split(":")
            if(indicator[0] == "enableSensors"):
                if(indicator[1] == "True"):
                    self.enableSensors = True
                else:
                    self.enableSensors = False

            elif(indicator[0] == "enableUart"):
                if(indicator[1] == "True"):
                    self.enableUart = True
                else:
                    self.enableUart = False

            elif(indicator[0] == "serverIp"):
                self.serverIp = str(indicator[1])
            elif(indicator[0] == "enableRelays"):
                if(indicator[1] == "True"):
                    self.enableRelays = True
                else:
                    self.enableRelays = False

            elif(indicator[0] == "uartAmount"):
                self.uartAmount = int(indicator[1])

            else:
                print("[Warning] Incorrect parameter: " + indicator[0])
            aux = aux+1

        self.check.checkInputVariables(self.enableSensors,self.enableUart,self.serverIp,self.enableRelays,self.uartAmount)
        return self.enableSensors,self.enableUart,self.enableRelays,self.serverIp,self.uartAmount
