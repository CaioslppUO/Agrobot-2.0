###########################
#----> Verifications <----#
###########################

def checkVariables(serverIp,enableUart,enableSensor,enableRelay,uartAmount):
    if(serverIp == None):
        return False,"Invalid ServerIp"
    if(enableUart == None):
        return False,"Invalid EnableUart"
    if(enableSensor == None):
        return False,"Invalid EnableSensor"
    if(enableRelay == None):
        return False,"Invalid EnableRelay"
    if(uartAmount == None):
        return False,"Invalid UartAmount"
    return True,"Launcher variables were initialized correctly"

######################################
#----> Launcher Variables Class <----#
######################################

class LauncherVariables():
    def __init__(self):
        self.serverIp     = None
        self.enableUart   = None
        self.enableSensor = None
        self.enableRelay  = None
        self.uartAmount   = None
        self.numberOfNeededVariables = 5

    def variableSeparator(self,variables):
        i = 1
        while(i < len(variables)):
            variable = variables[i].split(":")
            if(variable[0] == "serverIp"):
                self.serverIp = str(variable[1])
            elif(variable[0] == "enableUart" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enableUart = str(variable[1])
            elif(variable[0] == "enableSensor" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enableSensor = str(variable[1])
            elif(variable[0] == "enableRelay" and (str(variable[1]) == "False" or str(variable[1]) == "True")):
                self.enableRelay = str(variable[1])
            elif(variable[0] == "uartAmount" and (int(variable[1]) == 0 or int(variable[1]) == 1 or int(variable[1]) == 2)):
                self.uartAmount = int(variable[1])
            i = i + 1

        checkResult,checkResultMsg = checkVariables(self.serverIp,self.enableUart,self.enableSensor,self.enableRelay,self.uartAmount)
        if(checkResult == False):
            print(checkResultMsg)
            exit(0)
            
        print(checkResultMsg)
        return self.serverIp,self.enableUart,self.enableSensor,self.enableRelay,self.uartAmount