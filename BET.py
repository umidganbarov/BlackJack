class BetX:#                Bet 5
    def getBet(self,X):
        return X
#percents as experiment

class BetXP:
    def getBet(self,iBalance,X):
        return max(1,int(iBalance*(X/100)))
class BetFull:#             Bet your all balance
    def __init__(self,balance):
        self.balance=balance
    def getBet(self):
        return self.balance
class BetMartingale:  
    def getBet(self,lastHandWon,  lastHandBet): #lasthandwon is trye or false
        #? If false bet2x, if none or True bet 1
        #? It must be none in starting shoe 
        if lastHandWon in [True,None]:
            return 1 #goes minimal bet
        elif lastHandWon=="Tie":
            return lastHandBet
        elif lastHandWon==False:
            return lastHandBet*2
    

            








#!  ADD COUNTING PLAYER DEALER IN MAIN HARA QOYASSAN ONA BAX
