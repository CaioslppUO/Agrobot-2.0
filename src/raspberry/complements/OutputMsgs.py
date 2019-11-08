import os

class OutMsg:
    
    def printManualOutput(self,speed,steer,limit,powerA,powerB):
        os.system("clear")
        print('\t\t\t       * Manual Mode *\n')
        print('\t\t\t\t-> Speed: ' + speed)
        print('\t\t\t\t-> Steer: ' + steer)
        print('\t\t\t\t-> Limit: ' + limit + '\n')
        print('\t\t\t\t-> Board A: ' + powerA)
        print('\t\t\t\t-> Board B: ' + powerB)
        
    def printMissionOutput(self):
        os.system("cls")