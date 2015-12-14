import random

#Template for a player
class Player:
        def __init__(self):
                self.name = playName() #player's name, uses playerName function
                self.total = 0 #Handvalue

        #Deals a hand for the player
        def dealAHand(self,deck):
                random.shuffle(deck)
                #print(deck)
                hand = [deck[-1], deck[-2]]
                deck.pop()
                deck.pop()
                #print("hand: " + str(hand) + "  . " + str(deck))
                self.hand = hand
                return deck #The deck leftover

#Template for each card
class Card:
        def __init__(self,cc):
                self.cardCode = cc #Card number
                cardValues = [1,2,3,4,5,6,7,8,9,10,10,10,10]
                self.bjValue = cardValues[self.cardCode//4 - 1] #Black jack value
                
        def __str__(self):
                #print("hand: " + str(card))
                suits = ["♤","♢","♡","♧"]
                cardValues = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"]
                return str(cardValues[self.cardCode//4 - 1] + " of " + suits[self.cardCode%4]) #Prints out the card

#Introduction to game with tutorial
def intro():
        print("This is the game of Black Jack. This is for two players. You will both receive two cards from a deck. The first player will choose whether or not to hit (ick another card) or stay. 21 is the highest number." + "\n")

#Function to ask for player's name
def playName():
        name = input("Enter Player's name: ")
        return name

#function to create a deck
def createDeck():
        deck = []
        for i in range(4,56):
                deck.append(Card(i))    
        return deck

#Calculate blackJack total
def blackJackValue(hand):
        total = 0
        for i in range(len(hand)):
                        if total <= 10 and hand[i].bjValue == 0: #Determines if an ace is worth 11 or 1
                                total += 11
                        else:
                                total += hand[i].bjValue
        return total

#Displays all of the cards from a hand
def displayHand(hand, name):
        total = blackJackValue(hand)
        print(name + ", you have: " + ', ' + str(hand[0])+ str(hand[1]) + ". A total of " + str(total))
        return total

#Checks if the total is over 21
def checkValue(total, keepPlay):
        if total > 21:
                print("Bust!")
                keepPlay = False
                total = 0
        elif total == 21:
                print("BlackJack!")
                keepPlay = False
        return keepPlay,total

#Function when player decides to hit
def hit(hand,total, deck):
        hand.append(deck[-1])
        deck.pop()
        total = blackJackValue(hand)
        print("It's a " + str(hand[-1]) + ". A total of " + str(total))
        return total

#Each player's turn
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

#Determines a winner based on total
def winner(total1,total2, name1, name2):
        if total1 < total2:
                print("Congrats, " + name2 + "! You won!")
        elif total1 > total2:
                print("Congrats, " + name1 + "! You won!")
        elif total1 == total2:
                print("It's a tie!")

        
def main():
        gameStatus = 'y' #turns on a game
        intro() 
        play1 = Player() #Creates players
        play2 = Player()
        print("\n")
        deck = createDeck() #Creates a full deck

        while gameStatus == 'y': #LCV for game
                deck = play1.dealAHand(deck)
                deck = play2.dealAHand(deck)
                play1.total = choice(play1.name,play1.hand,play1.total,deck)
                play2.total = choice(play2.name,play2.hand,play2.total,deck)
                print("\n")
                winner(play1.total,play2.total,play1.name,play2.name)
                
                gameStatus = input("Play again? (type 'y' for yes or 'n' for no)") #turns on/off the game

main()
