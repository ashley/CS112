import time

#Intro 
def intro():
    print("Welcome to the game of Tic Tac Toe! You will be playing the classic game. The first to get a row/column/diagonal will win." + "\n")
    playerOneName = input("Player 1, enter your name: ") #Ask for users' names
    playerTwoName = input("Hi, " + playerOneName + ". Now enter Player 2's name: ")
    tutorial = input("Do you need a tutorial? (Enter 'y' for yes and 'n' for no): ") #Execute(?) Tutorial
    return playerOneName, playerTwoName, tutorial

#Tutorial. Just filled with text and an input for replay
def tutorial():
    print("\n" + "-------START OF TUTORIAL-------")
    board = [["*","*","*"],["*","*","*"],["*","*","*"]]
    board[0][0] = "_|"
    board[0][1] = "_"
    board[0][2] = "|_"
    board[1][0] = "_|"
    board[1][1] = "_"
    board[1][2] = "|_"
    board[2][0] = "  |"
    board[2][1] = "  "
    board[2][2] = "|  "
    print("\n" + "This is what the board looks like...")
    time.sleep(1)
    display(board)
    time.sleep(1)
    print("\n" + "You will be asked to enter in a value when it's your turn. Here are some examples.")
    time.sleep(2)
    print("Row '1' --> ", board[0][0], board[0][1], board[0][2])
    print("Row '2' --> ", board[1][0], board[1][1], board[1][2])
    print("Row '3' --> ", board[2][0], board[2][1], board[2][2])
    time.sleep(2)
    print("\n" + "Columns run the other way.")
    time.sleep(2)
    print("\n" + "You can either enter the row/column number or phrases:" + "\n" + "ROW: 'left'/'mid/'right'" + "\n" + "COLUMN: 'top'/'mid'/'bottom'")
    time.sleep(2)
    print("\n" + "EXAMPLE: You enter 'top' for row and 'left' for column....")
    time.sleep(2)
    board[0][0] = 'X'
    display(board)
    print("\n" + "EXAMPLE: You enter 'mid' for row and 'mid' for column....")
    time.sleep(2)
    board[1][1] = 'X'
    display(board)
    print("\n" + "EXAMPLE: You enter 'bottom' for row and 'right' for column....")
    time.sleep(2)
    board[2][2] = 'X'
    display(board)
    time.sleep(1)
    print("\n" + "And that's a winning board!")
    time.sleep(2)
    board[1][1] = "_"
    board[2][2] = " "
    print("\n" + "You can either enter the row/column number or phrases:" + "\n" + "ROW: 1 / 2 / 3" + "\n" + "COLUMN: 1 / 2 / 3")
    time.sleep(2)
    print("\n" + "EXAMPLE: You enter '1' for row and '1' for column....")
    time.sleep(2)
    board[0][0] = 'O'
    display(board)
    print("\n" + "EXAMPLE: You enter '2' for row and '2' for column....")
    time.sleep(2)
    board[1][1] = 'O'
    display(board)
    print("\n" + "EXAMPLE: You enter '3' for row and '3' for column....")
    time.sleep(2)
    board[2][2] = 'O'
    display(board)
    time.sleep(2)
    print("-------END OF TUTORIAL-------")
    tutorial = input("Replay or continue to play the game ('y' for yes and 'n' for no): ")
    return tutorial

#Resets everything
def create(playerOneName, playerTwoName): 
    board = [["*","*","*"],["*","*","*"],["*","*","*"]]
    board[0][0] = "_|"
    board[0][1] = "_"
    board[0][2] = "|_"
    board[1][0] = "_|"
    board[1][1] = "_"
    board[1][2] = "|_"
    board[2][0] = "  |"
    board[2][1] = "  "
    board[2][2] = "|  "
    display(board) 
    inGame = True #Whether to stay within game loop
    counter = 0 #To decide ties
    print("Good luck, " + playerOneName + " and " + playerTwoName + "\n")
    return board, inGame, counter

#Just display
def display(board):
    print(board[0][0], board[0][1], board[0][2])
    print(board[1][0], board[1][1], board[1][2])
    print(board[2][0], board[2][1], board[2][2])

#Actual moving function
def move(game, symbolOne, symbolTwo, counter, playerOneName, playerTwoName):
    if counter%2 == 0: #Decides if its player one or player two's turn
        symbolSign = symbolOne
        playerName = playerOneName
        i = 0
    else:
        symbolSign = symbolTwo
        playerName = playerTwoName
        i = 1

    moveOn = 0 #Bool for valid inputs

    #Figures out array number from words
    def translate(word):
        number = 0
        phrase = {'left':1, 'mid':2, 'right':3, 'top':1, 'bottom':3, '1':1,'2':2,'3':3}
        for x in phrase:
            if word.lower() == x:
                number = phrase[x]
        if number == 0:
            print("You've entered an invalid input.")

        return number

    #magicSquare = [[8,1,6],[3,5,7],[4,9,2]]
    
    while moveOn == 0:
        error = False #error from illegal Function
        row = input("\n" + playerName + ", Enter the ROW number (1/2/3 or top/mid/bottom): ") #ACTUAL input
        row = int(translate(row)) - 1 #After translate
        column = input("Enter the COLUMN number (1/2/3 or left/mid/right): ") #ACTUAL input
        column = int(translate(column)) - 1 #After translate

        moveOn = illegal(row, column, moveOn, error, game, symbolSign, playerName) #execute illegal function


    counter += 1 #Determines ties
    return game, row, column, counter, symbolSign, playerName

#Function to determine valid inputs
def illegal(row, column, moveOn, error, game, symbolSign, playerName):
    if -1 < row < 3 and -1 < column < 3: #Makes sure inputs are within list range
        moveOn = 1
    else: #Not within range
        print(playerName.upper() + "!!! You've entered an invalid row/column.")
        error = True #bool for illegal
    if error == False:  #Pass the first bool          
        if game[row][column] != "X" and game[row][column] != "O": #Valid symbols
            game[row][column] = symbolSign #If the user did their job
            display(game) #Displays board
            moveOn = 1 #bool passed
            #print("Good")
        else:
            print(playerName.upper() + "!!! This cell is already taken. Choose another one.") #Taken cell
            moveOn = 0
    return moveOn

#Function to check if a row has been made
def isFull(counter, gameStatus):
    if counter == 9: #Board in filled
        print("It's a tie")
        gameStatus = False
        #print(gameStatus)
    return gameStatus

#Function to check if there's a winner
def isWinner(row, column, counter, board, gameStatus, symbolSign, playerName):
    symbol = symbolSign
    i = 0
    winner = False #Right now, there's no winner
    #print(board)

    #Check for rows
    while i < 3:
        if symbol+symbol+symbol == ''.join(board[i]):
            winner = True
            i = 3
        else:
            i += 1

    i = 0
    #Checks for columns
    while i < 3:
        if symbol+symbol+symbol == board[0][i]+board[1][i]+board[2][i]:
            winner = True
            i = 3
        else:
            i += 1
    
    #Checks for diagonals
    if symbol+symbol+symbol == board[0][0]+board[2][2]+board[1][1]:
        winner = True
    elif symbol+symbol+symbol == board[0][2]+board[1][1]+board[2][0]:
        winner = True

    #Bool passes for a winner
    if winner == True:
            print(playerName, "!! You've won")
            if counter == 9:
                counter = 0 #Makes sure that a tie is not initialized if there's a winner on the last move
            gameStatus = False
    return gameStatus, counter

#Function to toggle between symbols
def twoPlayer(playerOneName):
    symbolOne = ''
    while symbolOne == '': #bool to make sure the input is valid
        symbolOne = input(playerOneName + ", Choose your symbol by entering either 'X' or 'O': ").upper()

        if symbolOne == "O":
            symbolTwo = "X"
        elif symbolOne == "X":
            symbolTwo = "O"
        else:
            print("Invalid Symbol. Enter EITHER 'X' or 'O': ")
            symbolOne = ''
    return symbolOne, symbolTwo

#Done
def main():
    playerOneName,playerTwoName, tutorialSign = intro() #Intro initailized
    while tutorialSign == 'y': #Initialize tutorial if user asks
        tutorialSign = tutorial()
    continueGame = "y" #bool for a continuous game
    while continueGame == "y":
        print("\n" + "BEGIN!!!")
        board,inGame, counter = create(playerOneName,playerTwoName) #Resets everything
        symbolOne,symbolTwo = twoPlayer(playerOneName) #Toggles symbols
        while inGame == True: #Actual game
            board,row, column,counter, symbolSign, playerName = move(board, symbolOne, symbolTwo, counter, playerOneName, playerTwoName)
            inGame,counter = isWinner(row, column, counter, board,inGame, symbolSign, playerName)
            inGame = isFull(counter,inGame)
    
        continueGame = input("Continue playing by entering 'y' for yes or 'n' for no: ").lower()
    print("GoodBye!")

main()
