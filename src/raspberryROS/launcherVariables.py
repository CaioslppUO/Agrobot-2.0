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
                self.enableUart = bool(variable[1])
            elif(variable[0] == "enableSensor"):
                self.enableSensor = bool(variable[1])
            elif(variable[0] == "enableRelay"):
                self.enableRelay = bool(variable[1])
            elif(variable[0] == "uartAmount"):
                self.uartAmount = int(variable[1])
            i = i + 1

        if(self.serverIp == None or self.enableUart == None or self.enableSensor == None
         or self.enableRelay == None or self.uartAmount == None):
            print("Launcher invariables are incomplete or worng. Aborting...")
            exit(0)

        return self.serverIp,self.enableUart,self.enableSensor,self.enableRelay,self.uartAmount