from random import shuffle
from random import randint
import random
import Responces
import BET
import time
from statistics import median
from statistics import stdev
import CardCounting


def shuffling(lShoe):# shuffles fll deck|input:deck
    rng = random.SystemRandom()
    rng.shuffle(lShoe)
    rng.shuffle(lShoe)
    return lShoe 
def winBalance(balance,bet):
    return balance+bet
def loseBalance(balance,bet):
    return balance-bet
def enoghBalance(balance,bet):#-1 1 
    if bet>balance:
        return False
    return True
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
    global ccount
    ldealer=dealer.copy()
    while(handSum(ldealer)<17):# card draws till 16]
        ccount+=askCounting(lShoe[0])
        ldealer.append(lShoe.pop(0))
         #delete drawn card from deck and draws card
    return ldealer
def hit(player,lShoe):#gives player one card, deletes from lshoe
    global ccount
    ccount+=askCounting(lShoe[0])
    player.append(lShoe.pop(0))
    return player


def standCase(player,dealer,lShoe,bet):
    global lose ,win,tie,balance,lastHandWon,ccount
    dealer=stand(dealer,lShoe)
    if isBlackjack(dealer) and isBlackjack(player):
        
        tie+=1
        lastHandWon="Tie"
        return None
    if isBlackjack(dealer):
        balance=loseBalance(balance,bet)
        lose+=1
        lastHandWon=False
        return None
    if isOver21(dealer):
        balance=winBalance(balance,bet)
        win+=1
        lastHandWon=True
        return None
    ans=compareDP(dealer,player)
    if ans==0:
        lose+=1
        balance=loseBalance(balance,bet)
        lastHandWon=False
        return None
    if ans==1:
        win+=1
        balance=winBalance(balance,bet)
        lastHandWon=True
        return None
    else:
        tie+=1
        lastHandWon="Tie"
        return None
    
def hitCase(player,dealer,lShoe,bet):
    global lose ,win,tie,balance,lastHandWon,ccount
    player=hit(player,lShoe)
    if isBlackjack(player):
        win+=1
        balance=winBalance(balance,bet)
        lastHandWon=True
        return -1
    if isOver21(player):
        lose+=1
        balance=loseBalance(balance,bet)
        lastHandWon=False
        return -1


    r=askResponce(player,dealer)
    return r

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


def playHand(lShoe):#! Each hand 
    global lose,win,tie,balance,lastHandWon,lastHandBet,ccount
    if balance<=0:return -1
    bet=askBetting()
    

    if enoghBalance(balance,bet):pass
    else :
        """If player1 do not have engough balance for bet, There are 2 possible ways:
        1] He can exit shoe and player2 starts
        2] He can change the betting
        I will chose it as [2] and bet=balance so all in"""
        """If player gets stand he does nothn, The dealer must draw cards. If dealer sees total <17 he draw again, else stop. """
        bet=balance
    player=lShoe[0:3:2]# gets index 0 and 2
    dealer=lShoe[1:4:2]# gets index 1 and 3

    for card in lShoe[0:4]:
        ccount+=askCounting(card)
    del lShoe[:4]  #removing choosen cards
    lastHandBet=bet

    if isBlackjack(dealer) and isBlackjack(player):
        tie+=1
        lastHandWon="Tie"

        return None
    elif isBlackjack(dealer):
        balance=loseBalance(balance,bet)
        lose+=1
        lastHandWon=False
        
        return None

    elif isBlackjack(player):
        balance=winBalance(balance,bet)
        win+=1
        lastHandWon=True
        
        return None
    
    # Hit or Stand
    r=askResponce(player,dealer)            

    #Stand case
    if r==0:
        standCase(player,dealer,lShoe,bet)
    if r==1:
        r=hitCase(player,dealer,lShoe,bet)
        #-------------------------------
        while(r==1):
            r=hitCase(player,dealer,lShoe,bet)
        #-------------------
        if r==0:standCase(player,dealer,lShoe,bet)


def askCounting(card):#use before pop,del s
    global icounting,ccount,counting2
  
    counting=str(icounting).strip()
    try:
        counting=int(counting)
    except ValueError:
        pass
    if counting=="hilo":
        counting=CardCounting.CounterHiLo().count(card)
        return counting
    elif counting=="dont":
        ccount=0
        return 0

def askResponce(player,dealer):
    global iresponce,ccount,icounting
    
    responce= str(iresponce).strip()
    try:
        responce=int(responce)
    except ValueError:
        pass
    #if icounting=="dont":
        #pass
    #else: 
    #    if ccount>=12:responce="stand15"
     #   elif ccount>=5:responce="stand16"
      #  elif ccount>=-5:responce="stand17"
       # elif ccount>=-12:responce="stand18"
        #else:responce="stand19"

    if responce=="random":
        responce=Responces.RandomResponce().decide()
        return responce
    elif responce=="stand19":
        responce=Responces.StandX().decide(player,19)
        return responce
    elif responce=="stand18":
        responce=Responces.StandX().decide(player,18)
        return responce
    elif responce=="stand17":
        responce=Responces.StandX().decide(player,17)
        return responce
    elif responce=="stand16":
        responce=Responces.StandX().decide(player,16)
        return responce
    elif responce=="stand15":
        responce=Responces.StandX().decide(player,15)
        return responce
    elif responce=="stand14":
        responce=Responces.StandX().decide(player,14)
        return responce

def askBetting():
    global lastHandWon,lastHandBet,istrategy, icounting, ibet

    istrategy=str(ibet)
    strategy=istrategy.strip()

    if icounting=="dont":
        pass
    else:
        if ccount >= 10: return max(1, int(balance * 0.07))
        elif ccount >= 5: return max(1, int(balance * 0.04))
        elif ccount >= 2: return max(1, int(balance * 0.02))
        else: return max(1, int(balance * 0.01))

    if strategy.isdigit():
        strategy=int(strategy)
        strategy=BET.BetX().getBet(strategy)#5
        return strategy
    elif strategy.endswith("p"):
        strategy=BET.BetXP().getBet(balance,int(strategy[:-1]))
        return strategy
    elif strategy=="full":
        strategy=BET.BetFull(balance).getBet()
        return strategy
    elif strategy=="ma":
        strategy=BET.BetMartingale().getBet(lastHandWon,lastHandBet) 
        return strategy



def Main(times2,ibalance2,ibet2,counting2,resp2):
    global istrategy, iresponce, icounting
    global balance, ccount, win, lose, tie, lastHandWon, lastHandBet,ibet,icounting
    shoe = [10,2, 3, 4, 10, 5,  "ACE"     ,6, 7, 8, 10, 9, 10] * 4  * 6

    
    
    win=0
    lose=0
    tie=0
    
    balances=[]
    counts=[]
    times=times2
    start = time.perf_counter()
    countHands:int =0
    for game in range(1,times+1):#! Game starts
        lastHandWon=None
        lastHandBet=None
        balance=ibalance2
        ccount=0
        icounting=counting2
        iresponce=resp2
        ibet=ibet2
        
        initialbalance=balance
        lShoe=shoe.copy()
        shuffling(lShoe)
        #?counts how many hands played per one game
        

        while(len(lShoe)>78):
            countHands+=1
            ans=playHand(lShoe)
            if ans==-1:
                break

        balances.append(balance)
        counts.append(ccount)
    #print(f"Balance: {initialbalance}, Betting: {istrategy}, Strategy: {iresponce}, CardCounting: {icounting}\nWin: {win}, Lose: {lose}, Tie: {tie}\n{win/(lose+tie+win)*100:.8f}%, Total hands: {countHands}")

    ##print(f"Average win% based on balance: {sum(balances)/(times*initialbalance)*100:.5f}%")
    end = time.perf_counter()
    #print(f"\n\n Max won: {max(balances)}")
    #print(f"Brokes: {sum (1 for x in balances if x<2)}")
    #print(f"Time: {end-start:.4f} secs\n")
        #these store like average and full number of stats in given shoe times. Such as lets say times ==25000, it shows sum of asners of 25000 such as win, or some show averages such as win_rate[num]
    return {
        "shoes":times,
        "total_hands":countHands,
        "initial_balance":initialbalance,
        "strategy":iresponce,
        "card_counting":icounting,
        "betting":istrategy if icounting=="dont" else "card_counting",
        
        "wins[num]":win,
        "losses[num]":lose,
        "ties[num]":tie,
        "win_rate[num]%":(win/(lose+tie+win)*100),

        "winrate[balance]%":sum(balances)/(times*initialbalance)*100,
        "median":median(balances),
        "std":stdev(balances),
        "min_balance":min(balances),
        "max_balance":max(balances),
        "sharpe_like": (sum(balances)/times - initialbalance) / stdev(balances) if stdev(balances) > 0 else 0,


        "brokes":sum (1 for x in balances if x<2),
        "broke_rate%":(sum (1 for x in balances if x<2))/times*100,
        "profit_count[num]":sum(1 for x in balances if x>initialbalance),
        "profit_rate%":(sum(1 for x in balances if x>initialbalance))/times*100,

        "performance[sec]":f"{end-start:.3f}"   }


