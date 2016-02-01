import random

#Template for a player
class Player:
        def __init__(self):
                self.name = playName() #player's name, uses playerName function
                self.total = 0 #Handvalue
                self.hand = [] #Empty hand
                deck1 = createDeck() #Creates a full deck
                random.shuffle(deck1) #Shuffles the deck
                self.deck = deck1 #Replaces old deck with shuffle deck
                self.points = 0 #Initalize games won

        def __str__(self):
                return (self.name + ", you got: " + str(self.hand[-1])  + ". A total of " + str(self.total)) #Nicely displays card and total

        #Gives player 2 cards
        def dealAHand(self):
                self.total = 0
                self.hand =[]
                self.hit()
                self.hit()
                print (self.name + ", you have: " + str(self.hand[0]) + " and " + str(self.hand[1])  + ". A total of " + str(self.total))

        #Deals a hand for the player
        def hit(self):
                self.hand.append(self.deck[-1])
                self.deck.pop()
                if self.hand[-1].bjValue == 1:
                        if self.total <= 10:
                                self.total += 11
                        else:
                                self.total += self.hand[-1].bjValue
                else:
                        self.total += self.hand[-1].bjValue


        #Ask to hit or nah. Uses checkValue
        def choice(self):
                keepPlay = True
                while keepPlay == True:
                        print("------------------------------------")
                        play = 'o'
                        if self.total == 21:
                                print("Black Jack!")
                                keepPlay = False
                        else:
                                while play != 'h' and play != 'n':
                                        play = input(self.name + ", Hit or nah? (type 'h' for hit and 'n' for nah): ")
                                        if play == "h":
                                                self.hit()
                                                print(self)
                                                keepPlay = self.checkValue(keepPlay)
                                        elif play == 'n':
                                                keepPlay = self.checkValue(keepPlay)
                                                keepPlay = False
                                        else:
                                                print("Please type 'h' for hit and 'n' for nah")

        #Checks if value is over 21
        def checkValue(self, keepPlay):
                if self.total > 21:
                        print("Bust!")
                        keepPlay = False
                        self.total = 0
                elif self.total == 21:
                        print("BlackJack!")
                        keepPlay = False
                return keepPlay
        

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
                return str(cardValues[self.cardCode//4 - 1] + " of " + suits[self.cardCode%4] + "bjValue: " +str( self.bjValue)) #Prints out the card

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

#Determines a winner based on total
def winner(name1, name2):
        if name1.total < name2.total:
                print("Congrats, " + name2.name + "! You won!")
                name2.points += 1
        elif name1.total > name2.total:
                print("Congrats, " + name1.name + "! You won!")
                name1.points += 1                
        elif name1.total == name2.total:
                print("It's a tie!")
        print("Score: " + name1.name + ": " + str(name1.points) + "  "  + name2.name + ": " + str(name2.points))

        
def main():
        gameStatus = 'y' #turns on a game
        intro() 
        play1 = Player() #Creates players
        play2 = Player()
        print("\n")
        while gameStatus == 'y': #LCV for game
                play1.dealAHand() #deal two cards
                play1.choice() #hits or nah
                print("\n")
                play2.dealAHand() #deal two cards               
                play2.choice() #hit or nah
                print("\n")
                winner(play1,play2) #determines winner
                gameStatus = input("Play again? (type 'y' for yes or 'n' for no)") #turns on/off the game


