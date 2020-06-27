import time
from MaxConnect4Game import *
import sys
# !/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega
str = []


def oneMoveGame(currentGame):
    start = time.time()
    currentGame.printGameBoard()
    while currentGame.getPieceCount() != 42:
        currentGame.aiPlay()  # Make a move (only random is implemented)

        print('Game state after move:')
        currentGame.printGameBoard()

        currentGame.countScore()
        if(currentGame.firstPlayer == 1):
            print('Player 1 Score: %d and Player 2 Score: %d\n' %
                  (currentGame.player1Score, currentGame.player2Score))
        else:
            print('Player 1 Score: %d and Player 2 Score: %d\n' %
                  (currentGame.player2Score, currentGame.player1Score))
    currentGame.printGameBoard()
    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()
    if(currentGame.firstPlayer == 1):
        if currentGame.player1Score > currentGame.player2Score:
            print('Player 1 won by score: %d' %
                  int(currentGame.player1Score - currentGame.player2Score))
        elif currentGame.player2Score > currentGame.player1Score:
            print('Player 2 won by score: %d' %
                  int(currentGame.player2Score - currentGame.player1Score))
        else:
            print('draw match player 1 : %d = player 2 : %d' %
                  (currentGame.player1Score, currentGame.player2Score))
    else:
        if currentGame.player2Score > currentGame.player1Score:
            print('Player 1 won by score: %d' %
                  int(currentGame.player2Score - currentGame.player1Score))
        elif currentGame.player1Score > currentGame.player2Score:
            print('Player 2 won by score: %d' %
                  int(currentGame.player1Score - currentGame.player2Score))
        else:
            print('draw match player 1 : %d = player 2 : %d' %
                  (currentGame.player2Score, currentGame.player1Score))
    print(time.time() - start)

# for the interactive mode player and ai


def interactiveGame(currentGame, next_player):
    currentGame.printGameBoard()  # initial state of game is printed
    currentGame.countScore()  # intital score of player1score and player2score is counted
    if(currentGame.firstPlayer == 1):
        print('Player 1 Score: %d and Player 2 Score: %d\n' %
              (currentGame.player1Score, currentGame.player2Score))
    else:
        print('Player 1 Score: %d and Player 2 Score: %d\n' %
              (currentGame.player2Score, currentGame.player1Score))

    if next_player == 'human-next':
        while currentGame.getPieceCount() != 42:  # if this is true than we can play forward
            print('Now human player turn whose piece is %d' %
                  currentGame.currentTurn)
            # ask for input which is column number

            try:
                columnChoosed = int(
                    input("Enter the column number 1-7 where you want to play your piece: "))
                if not 0 < columnChoosed < 8:
                    print(
                        'It is not valid. Please reenter the column number between 1-7')
                    continue
                if not currentGame.playPiece(columnChoosed - 1):
                    print(
                        "Column you choosed: %d is full. Please choose another." % columnChoosed)
                    continue
                # if the column no is approved
                print('Human piece is placed in %dth column' % columnChoosed)
                currentGame.printGameBoard()  # print in console
                currentGame.gameFile = open("human.txt", 'w')  # write in file
                currentGame.printGameBoardToFile()  # print in file
                currentGame.gameFile.close()
                # check again if there is any move possible if not terminate printing score
                if currentGame.getPieceCount() == 42:

                    print('All pieces are used and game board is full\n')
                    currentGame.countScore()
                    if(currentGame.firstPlayer == 1):
                        print('Player 1 Score: %d and Player 2 Score: %d\n' %
                              (currentGame.player1Score, currentGame.player2Score))
                    else:
                        print('Player 1 Score: %d and Player 2 Score: %d\n' %
                              (currentGame.player2Score, currentGame.player1Score))
                    break
                else:

                    currentGame.turn_move()  # need to change current turn after human play
                    print('Now its computer turns whose piece is %d' %
                          currentGame.currentTurn)
                    currentGame.aiPlay()  # ai change turn itself after it plays
                    currentGame.printGameBoard()
                    currentGame.gameFile = open('computer.txt', 'w')
                    currentGame.printGameBoardToFile()
                    currentGame.gameFile.close()
                    currentGame.countScore()
                    if(currentGame.firstPlayer == 1):
                        print('Player 1 Score: %d and Player 2 Score: %d\n' %
                              (currentGame.player1Score, currentGame.player2Score))
                    else:
                        print('Player 1 Score: %d and Player 2 Score: %d\n' %
                              (currentGame.player2Score, currentGame.player1Score))
                    if currentGame.getPieceCount() == 42:
                        break
            except SyntaxError:
                print("please enter appropirate value")
                continue
    else:
        # its ai turn
        print('Computer is first player')
        currentGame.aiPlay()
        currentGame.printGameBoard()
        currentGame.gameFile = open('computer.txt', 'w')
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        currentGame.countScore()
        # after ai first play again go to loop of human and ai turn wise play till all moves are done
        interactiveGame(currentGame, 'human-next')

    # now check who has won
    currentGame.countScore()
    if(currentGame.firstPlayer == 1):
        if currentGame.player1Score > currentGame.player2Score:
            print('Player 1 won by score: %d' %
                  int(currentGame.player1Score - currentGame.player2Score))
        elif currentGame.player2Score > currentGame.player1Score:
            print('Player 2 won by score: %d' %
                  int(currentGame.player2Score - currentGame.player1Score))
        else:
            print('draw match player 1 : %d = player 2 : %d' %
                  (currentGame.player1Score, currentGame.player2Score))
    else:
        if currentGame.player2Score > currentGame.player1Score:
            print('Player 1 won by score: %d' %
                  int(currentGame.player2Score - currentGame.player1Score))
        elif currentGame.player1Score > currentGame.player2Score:
            print('Player 2 won by score: %d' %
                  int(currentGame.player1Score - currentGame.player2Score))
        else:
            print('draw match player 1 : %d = player 2 : %d' %
                  (currentGame.player2Score, currentGame.player1Score))
    # end prints
    if str[0] == 'computer-next':
        print('Computer player is Player 1')
        print('Human player is Player 2')
    else:
        print('Human player is Player 1')
        print('Computer player is Player 2')
    print('GAME OVER!!!')


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print(
            'Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game()  # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        # self generate the input file if it doesn't have
        currentGame.gameFile = open("self_generated_input.txt", "a")
        for i in range(6):
            for j in range(7):
                currentGame.gameFile.write("0"),
            currentGame.gameFile.write("\n")
        currentGame.gameFile.write("1")
        currentGame.gameFile.close()

        # open and read the file after the making a game board from start and the next player is 1
        currentGame.gameFile = open("self_generated_input.txt", "r")
        # sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]]
                             for line in file_lines[0:-1]]
    # currentGame.printGameBoard()
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.firstPlayer = currentGame.currentTurn
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    if(currentGame.firstPlayer == 1):
        print('Player 1 Score: %d and Player 2 Score: %d\n' %
              (currentGame.player1Score, currentGame.player2Score))
    else:
        print('Player 1 Score: %d and Player 2 Score: %d\n' %
              (currentGame.player2Score, currentGame.player1Score))

    currentGame.depth = argv[4]

    if game_mode == 'interactive':
        # Be sure to pass whatever else you need from the command line
        if argv[3] == 'computer-next':
            str.append('computer-next')
            currentGame.maxP = currentGame.currentTurn
            if(currentGame.maxP == 1):
                currentGame.minP = 2
            else:
                currentGame.minP = 1
            print('Computer player is player 1 and has move:%d' %
                  currentGame.currentTurn)
            print('Human player is player 2')
        else:
            str.append('human-next')
            currentGame.minP = currentGame.currentTurn
            if(currentGame.minP == 1):
                currentGame.maxP = 2
            else:
                currentGame.maxP = 1
            print('Human player is player 1 and has move:%d' %
                  currentGame.currentTurn)
            print('Computer player is player 2')
        interactiveGame(currentGame, argv[3])
    else:  # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        # Be sure to pass any other arguments from the command line you might need.
        currentGame.maxP = currentGame.currentTurn
        if(currentGame.maxP == 1):
            currentGame.minP = 2
        else:
            currentGame.minP = 1
        oneMoveGame(currentGame)


if __name__ == '__main__':
    main(sys.argv)
