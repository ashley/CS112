import random

#Introduction to game with tutorial

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
	suits = ["clubs","diamonds","hearts","spades"]
	cardValues = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"]
	card = str(cardValues[card//4 - 1] + " of " + suits[card%4])
	return card

#function calculate codevalue
def getCardCodeNumber(card):
    card = (card.split(' '))
    val = card[0]
    suit = card[2]
    cardSuits= {"clubs":0,"diamonds":1,"hearts":2,"spades":3}
    cardValues = {"ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,
                   "8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
    cardCode = cardValues[val]*4 + cardSuits[suit] 
    #print(cardCode)
    return (cardCode)

def displayHand(hand):
	hand1 = [handValue(hand[0]), handValue(hand[1])]
	print("You have: " + ', '.join(hand1))
	total = blackJackValue(hand)
	#cardState = getCardCodeNumber(hand)
	return total

def blackJackValue(hand):
	total = 0
	#print(hand)
	cardValues = [10,2,3,4,5,6,7,8,9,10,10,10,10]
	for i in range(len(hand)):
		total += cardValues[hand[i]//4 - 1]
	print("total: " + str(total))
	return total

def checkValue(total, gameStatus):
	if total > 21:
		print("Bust!")
		gameStatus = False
	elif total == 21:
		print("BlackJack!")
		gameStatus = False
	return gameStatus

def hit(hand,total, deck):
        print(deck)

gameStatus = 'y'
while gameStatus == 'y':
	deck = createDeck()
	hand, deck = dealAHand(deck)
	total = displayHand(hand)
	play = input("Hit or nah?")
	if play == "hit":
		hit(hand,total,deck)
	else:
		pass
	gameStatus = input("continue?")
