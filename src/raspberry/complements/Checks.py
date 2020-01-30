##########################
#----> Checks class <----#
##########################

class Checks:
    #Check if the input variables from command line are correct
    def checkInputVariables(self,enableSensors,enableUart,serverIp,enableRelays,uartAmount):
        if(enableSensors == "None" or (enableSensors != True and enableSensors != False)):
            self.criticalError("enableSensors")

        if(enableUart == "None" or (enableUart != True and enableUart != False)):
            self.criticalError("enableUart")

        if(enableRelays == "None" or (enableRelays != True and enableRelays != False)):
            self.criticalError("enableRelays")
        
        if(serverIp == "None" or len(serverIp.split(".")) != 4):
            self.criticalError("serverIp")

        if(uartAmount < 0 or uartAmount > 2):
            self.criticalError("uartAmount")

    #End the program in case of critical error
    def criticalError(self,msg):
        print("[Critical Error] One or more input variables are missing or are incorrect.")
        print("[Error] Incorrect/missing variable(s): " + msg)
        print("Aborting...")
        exit(1)