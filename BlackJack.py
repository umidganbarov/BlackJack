from random import shuffle
from random import randint
import random
shoe = [10,2, 3, 4, 10, 5,  "ACE"     ,6, 7, 8, 10, 9, 10] * 4  * 6
win=0
lose=0
tie=0


def winMessage(player,dealer):
    print(f"Player Won!\nPlayer: {player}, Dealer: {dealer}")
def loseMessage(player,dealer):
    print(f"Player Lost!\nPlayer: {player}, Dealer: {dealer}")
def tieMessage(player,dealer):
    print(f"Player and dealer Tie!\nPlayer: {player}, Dealer: {dealer}")
def toStringP(player,dealer):
    print("Player:", *player, f" Sum: {handSum(player)}")
    print("Dealer:", *dealer[:-1]," ?")


def shuffling(lShoe):# shuffles fll deck|input: deck
    rng = random.SystemRandom()
    rng.shuffle(lShoe)
    rng.shuffle(lShoe)
    return lShoe 
def response():
    while True:
        try :
            x=int(input())
            if x in [0,1]:
                return x
            print("Only 0,1 accepted")
        except ValueError:
            print("Only digits of 0,1 are accepted")
        

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


def standCase(player,dealer,lShoe):
    global lose ,win,tie
    dealer=stand(dealer,lShoe)
    if isBlackjack(dealer) and isBlackjack(player):
        tieMessage(player,dealer)
        tie+=1
        return None
    if isBlackjack(dealer):
        loseMessage(player,dealer)
        lose+=1
        return None
    if isOver21(dealer):
        winMessage(player,dealer)
        win+=1
        return None
    ans=compareDP(dealer,player)
    if ans==0:
        lose+=1
        loseMessage(player,dealer)
        return None
    if ans==1:
        win+=1
        winMessage(player,dealer)
        return None
    else:
        tie+=1
        tieMessage(player,dealer)
        return None
    
def hitCase(player,dealer,lShoe):
    global lose ,win,tie
    player=hit(player,lShoe)
    if isBlackjack(player):
        winMessage(player,dealer)
        win+=1
        return -1
    if isOver21(player):
        loseMessage(player,dealer)
        lose+=1
        return -1
    

    toStringP(player,dealer)
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





def playHand(lShoe):
    global lose,win,tie
    print("\n-------------")
    player=lShoe[0:3:2]# gets index 0 and 2
    dealer=lShoe[1:4:2]# gets index 1 and 3
    del lShoe[:4]  #removing choosen cards
    toStringP(player,dealer)
    if isBlackjack(dealer) and isBlackjack(player):
        tie+=1
        tieMessage(player,dealer)
        return None
    if isBlackjack(dealer):
        loseMessage(player,dealer)
        lose+=1
        return None

    if isBlackjack(player):
        winMessage(player,dealer)
        win+=1
        return None
    print("Hit or stand?")
    r=response() # Hit or Stand
    """If player gets stand he does nothn, The dealer must draw cards. If he sees total <17 he draw again, else stop.
    """
    #Stand case
    if r==0:
        standCase(player,dealer,lShoe)
    if r==1:
        r= hitCase(player,dealer,lShoe)
        #-------------------------------
        while(r==1):
            r=hitCase(player,dealer,lShoe)
        #-------------------
        if r==0:standCase(player,dealer,lShoe)







times=1
for game in range(1,times+1):
    lShoe=shoe.copy()
    print(f"Game {game} starts!!\nStand: 0\tHit: 1")
    shuffling(lShoe)
    countHands:int =0#?counts how many hands played per one game
    while(len(lShoe)>78):
        countHands+=1
        print(f"Hand {countHands} starts!!!")
        playHand(lShoe)
    print(f"done {game}")
    print(f"Win: {win}, Lose: {lose}, Tie: {tie}")

