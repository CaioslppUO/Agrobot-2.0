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

    def variableSeparator(self,variables):
        i = 1
        while(i < len(variables)):
            variable = variables[i].split(":")
            if(variable[0] == "serverIp"):
                self.serverIp = str(variable[1])
            elif(variable[0] == "enableUart"):
                self.enableUart = str(variable[1])
            elif(variable[0] == "enableSensor"):
                self.enableSensor = str(variable[1])
            elif(variable[0] == "enableRelay"):
                self.enableRelay = str(variable[1])
            elif(variable[0] == "uartAmount"):
                self.uartAmount = int(variable[1])
            i = i + 1

        checkResult,checkResultMsg = checkVariables(self.serverIp,self.enableUart,self.enableSensor,self.enableRelay,self.uartAmount)
        if(checkResult == False):
            print(checkResultMsg)
            exit(0)
            
        print(checkResultMsg)
        return self.serverIp,self.enableUart,self.enableSensor,self.enableRelay,self.uartAmount