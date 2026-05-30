# // It is used for non-user usage, simulation
from random import shuffle
from random import randint
import random
from randomresponse import response
import time
import BET









def shuffling(lShoe):# shuffles fll deck|input: deck
    rng = random.SystemRandom()
    rng.shuffle(lShoe)
    rng.shuffle(lShoe)
    return lShoe 
#def response():
    #while True:
        #try :
            #x=int(input())
            #if x in [0,1]:
                #return x
            #print("Only 0,1 accepted")
        #except ValueError:
            #print("Only digits of 0,1 are accepted")
        

def isBlackjack(deck):
    if handSum(deck)==21:
        return True
    return False
def compareDP(dealer,player):# return dealer0 player1 tie 2
    if handSum(player)==handSum(dealer):return 2
    if handSum(player)>handSum(dealer):return 1
    if handSum(player)<handSum(dealer):return 0
def isOver21(deck):
    if handSum(deck)>21:return True
    return False


def stand(dealer,lShoe):
    ldealer=dealer.copy()
    
    while(handSum(ldealer)<17):# card draws till 16]
        ldealer.append(lShoe.pop(0))
         #delete drawn card from deck and draws card
    return ldealer

def hit(player,lShoe):#gives player one card, deletes from lshoe
    player.append(lShoe.pop(0))
    return player


def standCase(player,dealer,lShoe,bet):
    global lose ,win,tie,balance
    dealer=stand(dealer,lShoe)
    if isBlackjack(dealer) and isBlackjack(player):
        
        tie+=1
        return None
    if isBlackjack(dealer):
        balance=loseBalance(balance,bet)
        lose+=1
        return None
    if isOver21(dealer):
        balance=winBalance(balance,bet)
        win+=1
        return None
    ans=compareDP(dealer,player)
    if ans==0:
        lose+=1
        balance=loseBalance(balance,bet)
        return None
    if ans==1:
        win+=1
        balance=winBalance(balance,bet)
        return None
    else:
        tie+=1
        return None
    
def hitCase(player,dealer,lShoe,bet):
    global lose ,win,tie,balance
    player=hit(player,lShoe)
    if isBlackjack(player):
        win+=1
        balance=winBalance(balance,bet)
        return -1
    if isOver21(player):
        lose+=1
        balance=loseBalance(balance,bet)
        return -1
    

    r=response()
    return r

def handSum(deck):
    total = 0
    aces = 0
    for card in deck:
        if card == "ACE":
            aces += 1
        else:
            total += card
    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total





def playHand(lShoe):#! Each hand 
    global lose,win,tie,balance
    if balance<=0:return -1
    bet=askBetting()#! Strategy/ Asked in every hand
    if enoghBalance(balance,bet):pass
    else :
        """If player1 do not have engough balance for bet, There are 2 possible ways:
        1] He can exit shoe and player2 starts
        2] He can change the betting
        I will chose it as [2] and bet=balance so all in"""
        bet=balance
        
    
    player=lShoe[0:3:2]# gets index 0 and 2
    dealer=lShoe[1:4:2]# gets index 1 and 3
    del lShoe[:4]  #removing choosen cards
    
    if isBlackjack(dealer) and isBlackjack(player):
        tie+=1
        
        return None
    elif isBlackjack(dealer):
        balance=loseBalance(balance,bet)
        lose+=1
        return None

    elif isBlackjack(player):
        balance=winBalance(balance,bet)
        win+=1
        return None
    
    r=response() # Hit or Stand
    """If player gets stand he does nothn, The dealer must draw cards. If he sees total <17 he draw again, else stop.
    """
    #Stand case
    if r==0:
        standCase(player,dealer,lShoe,bet)
    if r==1:
        r= hitCase(player,dealer,lShoe,bet)
        #-------------------------------
        while(r==1):
            r=hitCase(player,dealer,lShoe,bet)
        #-------------------
        if r==0:standCase(player,dealer,lShoe,bet)





def winBalance(balance,bet):
    return balance+bet
def loseBalance(balance,bet):
    return balance-bet

def enoghBalance(balance,bet):#-1 1 
    if bet>balance:
        return False
    return True

def askBetting():
    strategy=5 #bet 5
    if strategy==5:
        strategy=BET.Bet5().getBet()#5
        return strategy
    
if __name__=="__main__":
    start = time.perf_counter()
    shoe = [10,2, 3, 4, 10, 5,  "ACE"     ,6, 7, 8, 10, 9, 10] * 4  * 6


    win=0
    lose=0
    tie=0
    balances=[]
    times=int(input("How many total shoes you want?"))
    countHands:int =0
    for game in range(1,times+1):#! Game starts

        balance =100
         #?<-- Each Shoe balance is same

        initialbalance=balance
        lShoe=shoe.copy()
        #print(f"Game {game} starts!!\nStand: 0\tHit: 1")
        shuffling(lShoe)
        #?counts how many hands played per one game
        if (game==times//2):
            print("50%")
        while(len(lShoe)>78):
            countHands+=1
            ans=playHand(lShoe)
            if ans==-1:
                break
        balances.append(balance)



    print(f"\n\n\n\n\nWin: {win}, Lose: {lose}, Tie: {tie}\n{win/(lose+tie+win)*100:.3f}%, Total hands: {countHands}")
    for i in range(0,len(balances)):
        #print(f"Player[{i+1}]: {balances[i]}")
        pass
    print(f"Average win% based on balance: {sum(balances)/(times*initialbalance):.3f}%")
    end = time.perf_counter()

    print(f"Time: {end-start:.4f} secs")
        





