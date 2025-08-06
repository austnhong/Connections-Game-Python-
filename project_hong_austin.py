# ITP 115, Spring 2024
# Project
# Name: Austin Hong
# Email: austinjh@usc.edu
# Section: 32024
# Description: gets events, stores them, and reprints them


import helper
import interface


def main():

    print("Let's play Connections!")


    interface.displayRules("game_rules.txt")


    puzzleList = helper.createPuzzleList("connections_data.csv")


    chosenPuzzle = interface.pickPuzzle(puzzleList)


    if interface.playGame(chosenPuzzle):
        print("Congratulations!")
    else:
        print("Better luck next time.")

    interface.savePuzzle(chosenPuzzle)

main()