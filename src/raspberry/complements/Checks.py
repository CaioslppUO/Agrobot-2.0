##########################
#----> Checks class <----#
##########################

class Checks:
    #Check if the input variables from command line are correct
    def checkInputVariables(self,enableSensors,enableUart,serverIp,enableRelays,uartAmount):
        if(enableSensors == "None" or (enableSensors != True and enableSensors != False)):
            self.criticalError("One or more input variables are missing or are incorrect.","enableSensors")

        if(enableUart == "None" or (enableUart != True and enableUart != False)):
            self.criticalError("One or more input variables are missing or are incorrect.","enableUart")

        if(enableRelays == "None" or (enableRelays != True and enableRelays != False)):
            self.criticalError("One or more input variables are missing or are incorrect.","enableRelays")
        
        if(serverIp == "None" or len(serverIp.split(".")) != 4):
            self.criticalError("One or more input variables are missing or are incorrect.","serverIp")

        if(uartAmount < 0 or uartAmount > 2):
            self.criticalError("One or more input variables are missing or are incorrect.","uartAmount")

    def checkSpeed(self,speed):
        if(speed < -100):
            self.remediableError("Speed variable is below -100. Making the correction.")
            return -100
        elif(speed > 100):
            self.remediableError("Speed variable is over 100. Making the correction.")
            return 100
        return speed

    def checkSteer(self,steer):
        if(steer < -100):
            self.remediableError("Steer variable is below -100. Making the correction.")
            return -100
        elif(steer > 100):
            self.remediableError("Steer variable is over 100. Making the correction.")
            return 100
        return steer

    def checkLimit(self,limit):
        if(limit < 0):
            self.remediableError("Limit variable is below 0. Making the correction.")
            return 0
        elif(limit > 100):
            self.remediableError("Limit variable is over 100. Making the correction.")
            return 100
        return limit

    def checkAppMsgProtocol(self,speed,steer,limit,powerA,powerB,pulverizer,ignoreErrorMessage):
        if(speed == "None" or steer == "None" or limit == "None" or powerA == "None" or powerB == "None" or pulverizer == "None"):
            self.remediableError("One or more control variables recieved from protocol are missing or are incorrect. Making the robot stop.",ignoreErrorMessage)
            return False
        return True

    def remediableError(self,msg,ignoreErrorMessage):
        if(ignoreErrorMessage == False):
            print("[Remediable Error] " + msg)

    #End the program in case of critical error
    def criticalError(self,msg,especification):
        print("[Critical Error] " + msg)
        print("[Error] Incorrect/missing variable(s): " + especification)
        print("Aborting...")
        exit(1)