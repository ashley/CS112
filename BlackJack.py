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
	print(deck)
	hand = [deck[-1], deck[-2]]
	deck.pop()
	deck.pop()
	return hand,deck

#function calculate a hand
def handValue(hand):
	hand[0] 

#function display hand

deck = createDeck()
hand, deck = dealAHand(deck)