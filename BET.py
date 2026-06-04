class Bet5:#                Bet 5
    def __init__(self):
        self.bet=5
    def getBet(self):
        return self.bet
    def update(self,iWin):
        pass
class Bet10:
    def getBet():
        return 10
class BetFull:#             Bet your all balance
    def __init__(self,balance):
        self.balance=balance
    def getBet(self):
        return self.balance
    def update(self,iWin):
        pass
    
class BetMartingale:
    
    def getBet(self,lastHandWon,lastHandBet):#lasthandwon is trye or false
        #? If false bet2x, if none or True bet 1
        #? It must be none in starting shoe 
        if lastHandWon in [True,None]:
            return 1 #goes minimal bet
        elif lastHandWon=="Tie":
            return lastHandBet
        elif lastHandWon==False:
            return lastHandBet*2
    




#percents as experiment
class Bet10P:
    def getBet(self,iBalance):
        return max(1,int(iBalance*0.1))
class Bet20P:
 
    def getBet(self,iBalance):
        return max(1,int(iBalance*0.2))

            






