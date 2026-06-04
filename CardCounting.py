class CounterHiLo:
    def __init__(self):
        self.number=0
    def count(self,player,dealer):
        cards=player+dealer
        for x in cards:
            if x in [2,3,4,5,6]:number+=1
            elif x in [7,8,9]:pass
            else: number+=1
        
