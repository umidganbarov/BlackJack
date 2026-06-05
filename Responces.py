import random
class RandomResponce:
    def decide(self):
        return 1  if random.random()>0.5 else 0

def handSum(deck):
    total,aces = 0,0
    for card in deck:
        if card == "ACE":
            aces += 1
        else:total += card
    for _ in range(aces):
        if total + 11 <= 21:total+= 11
        else:total += 1
    return total

class StandX: #? Stand [<X] 
    def decide(self,player,stand):
        if handSum(player)<stand:
            return 1
        return 0
