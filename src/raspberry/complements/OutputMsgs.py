import os

class OutMsg:
    
    def printManualOutput(self,speed,steer,limit):
        os.system("clear")
        print('\t\t\t       * Manual Mode *\n')
        print('\t\t\t\t-> Speed: ' + speed)
        print('\t\t\t\t-> Steer: ' + steer)
        print('\t\t\t\t-> Limit: ' + limit + '\n')
        
    def printMissionOutput(self):
        os.system("cls")