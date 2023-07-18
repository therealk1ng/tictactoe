Game = "TicTacToe By ASAD."
Game_Bold = '\x1B[1m' + Game + '\x1B[0m'
print(Game_Bold)
print("—————————————————")
print("Player 1 is 'X' and Player 2 is 'O'.")
print("Game Board = |1|2|3|")
print("             |4|5|6|")
print("             |7|8|9|")
print("\n")

Continue = 0
while Continue == 0:
    
    Game1 = 0
    while Game1 == 0:
        print("Multiplayer or SinglePlayer? : ")
        print("' m ' for Multiplayer, ' s ' for Singleplayer")
        Gamemode = input(":- ")
        Gamemode_Lower = Gamemode.lower()
        if Gamemode_Lower == ("m"):
            Game1 = 1
        elif Gamemode_Lower == ("s"):
            Game1 = 2
        else:
            Game1 = 0


    Board = ['_'] * 9
    def GameBoard(Board):
        count = 0
        for i in range(3):
            print("|"+(Board[0+count])+"|"+(Board[1+count])+"|"+(Board[2+count])+"|")
            count += 3
    def WinningConditions(Board):

        # Winning Conditions (Rows)

        count = 0 
        for i in range(3):
            if Board[0+count] == Board[1+count] == Board[2+count] == 'X':
                return True
            count += 3
    
        count = 0 
        for i in range(3):
            if Board[0+count] == Board[1+count] == Board[2+count] == 'O':
                return True
            count += 3

        ## Winning Conditions ( Columns )

        count = 0
        for i in range(3):
            if Board[0+count] == Board[3+count] == Board[6+count] == 'X':
                return True
            count += 1    

        count = 0
        for i in range(3):
            if Board[0+count] == Board[3+count] == Board[6+count] == 'O':
                return True
            count += 1   

        ### Winning Conditions ( Diagnols )

        if Board[0] == Board[4] == Board[8] == 'X':
            return True

        if Board[2] == Board[4] == Board[6] == 'X':
            return True 
        
        if Board[0] == Board[4] == Board[8] == 'O':
            return True

        if Board[2] == Board[4] == Board[6] == 'O':
            return True 

    # The Game Starts Here

    if Game1 == 1:
        print("Player 1 is 'X' and Player 2 is 'O'. ")
        Moves = 9
        while Moves > 0:
            GameBoard(Board)
            Valid2 = 0
            while Valid2 == 0:
                try:
                    Player1 = int(input("Make the move 'X' : "))
                    if 1 <= Player1 <= 9:
                        pass
                    else:
                        Player1 = int(input("Enter Between 1 and 9 : "))
                    if Board[Player1-1] == '_':
                        Board[Player1-1] = 'X'
                        Valid2 += 1
                    else:
                        print("Perhaps that place is occupied, Make a Move Again ! ")
                except Exception:
                    print("Enter only Numbers... ")
            Moves = Moves - 1
            if WinningConditions(Board) == True:
                GameBoard(Board)
                print("Player 1 (X) won.")
                break

            GameBoard(Board)
            if Moves == 0:
                break
            Valid = 0
            while Valid == 0:
                try:
                    Player2 = int(input("Make the move 'O' : "))
                    if 1 <= Player2 <= 9:
                        pass
                    else:
                        Player2 = int(input("Enter Between 1 and 9 : "))
                    if Board[Player2-1] == '_':
                        Board[Player2-1] = 'O'
                        Valid += 1
                    else:
                        print("Perhaps that place is occupied, Make a Move Again ! ")
                except Exception:
                    print("Enter only Numbers... ")
            if WinningConditions(Board) == True:
                GameBoard(Board)
                print("Player 2 (O) won.")
                break
            Moves = Moves - 1

        if Moves == 0 and WinningConditions(Board) != True:
            print("Game Draw!! ")

    if Game1 == 2:
        import random
        print("You are 'X' and Computer is '0'")
        Moves2 = 9
        while Moves2 > 0:

            GameBoard(Board)
            Valid3 = 0
            while Valid3 == 0:
                try:
                    Player1 = int(input("Make the move 'X' : ")) 
                    if 1 <= Player1 <= 9:
                        pass
                    else:
                        Player1 = int(input("Enter Between 1 and 9: "))
                    if Board[Player1-1] == '_':
                        Board[Player1-1] = 'X'
                        Valid3 += 1
                    else:
                        print("Perhaps that place is occupied, Make a Move Again ! ")
                except Exception:
                    print("Enter only Numbers... ")
            Moves2 = Moves2 - 1
            if WinningConditions(Board) == True:
                GameBoard(Board)
                print("You (X) won.")
                break
            
            Valid4 = 0
            while Valid4 == 0:
                if Moves2 == 0:
                    break
                Bot = random.randint(0,8)
                if 1 <= Bot <= 9:
                    pass
                else:
                    Bot = random.randint(0,8)
                if Board[Bot] == '_':
                    Board[Bot] = 'O'
                    Valid4 += 1
            Moves2 = Moves2 - 1
            if WinningConditions(Board) == True:
                GameBoard(Board)
                print("Computer (O) wins.")
                break
        
        if Moves2 < 0 and WinningConditions(Board) != True:
            print("Game Draw!!")
            
    print("Do you want to exit the Game?\n'y' for yes, 'n' for no.")
    exit = input(":- ")
    Valid5 = 0
    while Valid5 == 0: 
        if exit == "y":
            Continue += 1
            Valid5 += 1
        elif exit == "n": 
            Continue += 0
            Valid5 += 1
        else:
            exit = input("Enter y or n : ")