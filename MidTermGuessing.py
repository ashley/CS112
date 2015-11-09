import random

"""
Notes to self
- Make the computer "less robotic" aka repetitively use user's name
- Check player 2 fancy game 
"""

#local variables
oneName = 0
twoName = 0
oneScore = 0
twoScore = 0
gameContinue = 'Y'
counter = 0
guess = 0
turn = oneName
otherTurn = twoName
previousString = " "
highLow = " "
high = "Guess higher"
low = "Guess lower"
fancyGame = 0
introPrompt = 1
startOver = "Y"


#Prompt Intro
while startOver == "Y" or startOver == "S":
  if introPrompt == 1:
    print("This is a number guessing game. The computer will generate a number between 1 and 10. You will guess the number to win.")
    oneName = input("\n" + "Enter your name: ")
    multiplayer = input("Hi " + oneName + ". Would you like to play with someone else? (Enter 'Y' for yes and 'N' for no)  ")
    if multiplayer == "Y":
        twoName = input("Enter the second player's name: ")
        fancyGame = input("\n" + "Howdy " + oneName + " and " + twoName + ". \n" + "Would you like to play two out of three games? (Enter 'Y' for yes and 'N' for no)")
  gameContinue = 'Y'
  while gameContinue == 'Y':
      number = random.randrange(1,11)
      print("\n" + "------------------------------------------------------" + "\n" + "Begin!")
      print(number)
      counter = 0 #reset counter
      guess = 0 #reset guess, just in case the next random number in the same as the previous random number
      previousString = " "
      while guess != number and counter < 10:
          if multiplayer == "Y": #multiplayer
              if(10 - counter) % 2 == 0:
                  turn = oneName
                  otherTurn = twoName
              else:
                  turn = twoName
                  otherTurn = oneName
          else:
              turn = oneName
          guess = int(input("\n" + "Enter your guess: "))

          if guess == number:
              counter = 10
              print("\n" + "Congratulations, " + turn + "! You have guessed the correct number!")
              if fancyGame == "Y":
                if turn == oneName:
                  oneScore += 1
                else:
                  twoScore += 1
                print("The current score: " + oneName + "- " + str(oneScore) + "  " + twoName + "- " + str(twoScore)) 
                if oneScore + twoScore >= 2:
                  if oneScore > 0 or twoScore > 0:
                    if oneScore > twoScore:
                      print("\n" + oneName + ", You have won the two out of three game!!!")
                      fancyGame = "N"
                    elif twoScore > oneScore:
                      print("\n" + twoName + ", You have won the two out of three game!!!")
                      fancyGame = "N"
                gameContinue = "Y"
          elif counter == 9:
              if multiplayer == "Y":
                  gameContinue = input("\n" + "Opps, Both of you have used up all of your tries. How hard is it to guess a number between 1 and 10 when you have ten tries. Play again? (Enter 'Y' for yes and 'N' for no)")
              else:
                  gameContinue = input("\n" + "Opps," + turn + "You have used up all of your tries. How hard is it to guess a number between 1 and 10 when you have ten tries. Play again? (Enter 'Y' for yes and 'N' for no)")
          elif guess !=number:
              if guess < number:
                  highLow = high
              else:
                  highLow = low
              if multiplayer == "Y":
                  print("Incorrect, " + turn + ".You and " + otherTurn + " have " + str(9 - counter) + " more tries. " + highLow + " next time. Now, it's " + otherTurn + "'s turn.")
                  print("Here are the numbers which both of you have already guessed: " + previousString) #Extra credit code
              else:
                  print("Incorrect, " + turn + ".You have " + str(9 - counter) + " more tries. " + highLow + " next time.")
                  print("Here are the number(s) which you have already guessed: " + previousString) #Extra credit code
              previousString += str(guess) + ", " #Extra credit code pt. 2
              counter += 1
      if fancyGame != "Y":
        startOver = input("\n" + "Would you like play the game again? Enter 'S' to start from the beginning. Enter 'Y' to keep the names and game setting. Enter 'N' to quit:  ")
        if startOver == 'S':
          gameContinue = 'N'
          introPrompt = 1
        elif startOver == 'Y':
          introPrompt = 0
        else:
          gameContinue = 'N'
print("Goodbye!")
