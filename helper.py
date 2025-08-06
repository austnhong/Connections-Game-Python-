# ITP 115, Spring 2024
# Project
# Name: Austin Hong
# Email: austinjh@usc.edu
# Section: 32024
# Description: gets events, stores them, and reprints them

import csv


def createPuzzleList(filenameStr='connections_data.csv'):
    listOfPuzzles = []  # List to hold the puzzles
    file = open(filenameStr, 'r')
    holder = file.readline().strip().split(',')

    for line in file:
        values = line.strip().split(',')  # Process each  line
        puzzle_dict = {}
        for i in range(len(holder)):
            puzzle_dict[holder[i]] = values[i]
        listOfPuzzles.append(puzzle_dict)

    file.close()
    return listOfPuzzles


def getPuzzleByNum(puzzleList, numStr):
    for puzzle in puzzleList:
        if puzzle['num'] == numStr:
            return puzzle
    return {}


def getColor(puzzleDict, difficultyNum):
    color = 'color' + str(difficultyNum)  # create the key based on the difficulty number
    return puzzleDict.get(color, '')


def getConnection(puzzleDict, difficultyNum):
    connection = 'connection' + str(difficultyNum)  # Construct the key for the connection
    return puzzleDict.get(connection, '')


def getGroup(puzzleDict, difficultyNum):
    words = []  # Initialize an empty list to hold the words
    # Loop through the numbers 1 to 4 to access each word key
    for i in range(1, 5):
        holder = 'word' + str(difficultyNum) + str(i)
        words.append(puzzleDict.get(holder, ''))  # Get the value for the key from the puzzle dictionary
    words.sort()
    return words


def getWordList(puzzleDict, foundGroupList):
    completeWords = []  # create an empty list to hold all unconnected words
    # Loop through the numbers 1 to 4
    for diffNum in range(1, 5):
        if diffNum not in foundGroupList:
            group_words = getGroup(puzzleDict, diffNum)  # Get the group of words for the current difficulty
            completeWords.extend(group_words)
    return completeWords