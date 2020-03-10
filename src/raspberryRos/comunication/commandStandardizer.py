########################################
#----> Command Standardizer class <----#
########################################

class CommandStandardizer():
    def __init__(self):
        self.a = 10

    #Check and correct the speed value if it is needed
    def checkSpeed(self,speed):
        if(speed < -100):
            return -100
        if(speed > 100):
            return 100
        return speed

    #Check and correct the steer value if it is needed
    def checkSteer(self,steer):
        if(steer < -100):
            return -100
        if(steer > 100):
            return 100
        return steer

    #Check and correct the limit value if it is needed
    def checkLimit(self,limit):
        if(limit < 0):
            return 0
        if(limit > 100):
            return 100
        return limit

    #Check and correct the relay value if it is needed
    def checkRelays(self,signal):
        if(signal != 0 and signal != 1):
            return 0
        return signal

    #Check all the variables recieved from the web server
    def webServerMsgCheck(self,speed,steer,limit,powerA,powerB,pulverizer):
        return self.checkSpeed(speed),self.checkSteer(steer),self.checkLimit(limit),self.checkRelays(powerA),self.checkRelays(powerB),self.checkRelays(pulverizer)

    #Split and certify that all the required variables are present
    def webServerMsgSpliter(self,msg):
        index = 1
        while index < len(msg):
            try:
                parameter = msg[index].split("$")[0]
                value = int(msg[index].split("$")[1])

                if(parameter == "speed"):
                    speed = value
                elif(parameter == "steer"):
                    steer = value
                elif(parameter == "limit"):
                    limit = value
                elif(parameter == "powerA"):
                    powerA = value
                elif(parameter == "powerB"):
                    powerB = value
                elif(parameter == "pulverize"):
                    pulverizer = value
            except:
                pass
            index = index + 1
        try:
            return speed,steer,limit,powerA,powerB,pulverizer
        except:
            return 0,0,0,0,0,0

    #Check and correct all recieved variables from the WebServer
    def webServerMsgHandler(self,msg):
        if(msg != None):
            speed,steer,limit,powerA,powerB,pulver = self.webServerMsgSpliter(msg) 
            speed,steer,limit,powerA,powerB,pulver = self.webServerMsgCheck(speed,steer,limit,powerA,powerB,pulver)  
            return str(speed) + "$" + str(steer) + "$" + str(limit) + "$" + str(powerA) + "$" + str(powerB) + "$" + str(pulver)
        else:
            return "None"