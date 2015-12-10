import random

#Introduction to game with tutorial

def playName(number):
        name = input("Player " + number + "'s name: ")
        return name

#function to create a deck
def createDeck():
        deck = []
        for i in range(52):
                deck.append(i)
        #print(deck)
        return deck

#function to deal a hand
def dealAHand(deck):
        random.shuffle(deck)
        #print(deck)
        hand = [deck[-1], deck[-2]]
        deck.pop()
        deck.pop()
        #print("hand: " + str(hand) + "  . " + str(deck))
        return hand,deck

#function calculate a hand
def handValue(card):
        #print("hand: " + str(card))
        suits = ["♤","♢","♡","♧"]
        cardValues = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"]
        card = str(cardValues[card//4 - 1] + " of " + suits[card%4])
        return card

#function calculate codevalue
def getCardCodeNumber(card):
    card = (card.split(' '))
    val = card[0]
    suit = card[2]
    cardSuits= {"♠":0,"♢":1,"♡":2,"♧":3}
    cardValues = {"ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
                   "8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
    cardCode = cardValues[val]*4 + cardSuits[suit] 
    #print(cardCode)
    return (cardCode)

def displayHand(hand, name):
        hand0 = [handValue(hand[0]), handValue(hand[1])]
        total = blackJackValue(hand)
        print(name + ", you have: " + ', '.join(hand0) + ". A total of " + str(total))  
        #cardState = getCardCodeNumber(hand)
        return total

def blackJackValue(hand):
        total = 0
        #print(hand)
        cardValues = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        for i in range(len(hand)):
                        value = hand[i]//4 - 1
                        if total <= 10 and value == 0:
                                total += 11
                        else:
                                total += cardValues[value]
        return total

def checkValue(total, keepPlay):
        if total > 21:
                print("Bust!")
                keepPlay = False
                total = 0
        elif total == 21:
                print("BlackJack!")
                keepPlay = False
        return keepPlay,total

def hit(hand,total, deck):
        hand.append(deck[-1])
        print("It's a " + str(handValue(deck[-1])))
        deck.pop()
        total = blackJackValue(hand)
        print(total)
        return total

def choice(name, hand, total,deck):
        keepPlay = True
        while keepPlay == True:
                print("------------------------------------")
                total = displayHand(hand,name)
                play = 'o'
                if total == 21:
                        print("Black Jack!")
                        keepPlay = False
                else:
                        while play != 'h' and play != 'n':
                                play = input(name + ", Hit or nah? (type 'h' for hit and 'n' for nah): ")
                                if play == "h":
                                        total = hit(hand,total,deck)
                                        keepPlay,total = checkValue(total,keepPlay)
                                elif play == 'n':
                                        keepPlay,total = checkValue(total,keepPlay)
                                        keepPlay = False
                                else:
                                        print("Please type 'h' for hit and 'n' for nah")
        return total

def winner(total, name1, name2):
        if total[0] < total[1]:
                print("Congrats, " + name2 + "! You won!")
        elif total[0] > total[1]:
                print("Congrats, " + name1 + "! You won!")
        elif total[0] == total[1]:
                print("It's a tie!")
gameStatus = 'y'
total = [0,0]
play1Name = playName(str(1))
play2Name = playName(str(2))
print("\n")
deck = createDeck()
while gameStatus == 'y':
        hand1, deck = dealAHand(deck)
        hand2, deck = dealAHand(deck)        
        total[0] = choice(play1Name,hand1,total[0],deck)
        total[1] = choice(play2Name,hand2,total[1],deck)
        print("\n")
        winner(total,play1Name,play2Name)
        gameStatus = input("Play again? (type 'y' for yes or 'n' for no)")
        
