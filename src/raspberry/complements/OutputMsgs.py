#####################
#----> Imports <----#
#####################

import os
import time

##########################
#----> OutMsg Class <----#
##########################

class OutMsg:
    def __init__(self):
        self.powerA = False
        self.powerB = False
        self.pulverizer = False
    
    #Debug print message for control mode
    def printManualOutput(self,speed,steer,limit,powerBoardA,powerBoardB,pulverizer):
        os.system("clear")
        print('\t\t\t       * Manual Mode *\n')
        print('\t\t\t\t-> Speed: ' + speed)
        print('\t\t\t\t-> Steer: ' + steer)
        print('\t\t\t\t-> Limit: ' + limit)
        if(powerBoardA == '1'):
            self.powerA = not self.powerA
            time.sleep(0.2)
        if(powerBoardB == '1'):
            self.powerB = not self.powerB
            time.sleep(0.2)
        if(pulverizer == '1'):
            self.pulverizer = True
        else:
            self.pulverizer = False
        if(self.powerA == True):
            print('\t\t\t\t-> Placa A: Ligada')
        else:
            print('\t\t\t\t-> Placa A: Desligada')
        if(self.powerB == True):
            print('\t\t\t\t-> Placa B: Ligada')
        else:
            print('\t\t\t\t-> Placa B: Desligada')
        if(self.pulverizer == True):
            print('\t\t\t\t-> Pulverizador: Ligado' + '\n')
        else:
            print('\t\t\t\t-> Pulverizador: Desligado' + '\n')
            