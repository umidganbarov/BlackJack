class CounterHiLo:
    def count(self,card):
        if card in [2,3,4,5,6]:return 1
        elif card in [7,8,9]:return 0
        else: return -1
            
class Dont():
    def count(self,player,dealer):
        return 0
