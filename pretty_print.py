# ITP 115, Spring 2023
# Final Project
# Name: Trina Gregory
# Filename: pretty_print.py
# Description: This file contains functions to print a puzzle using colors

import helper
import random
import pickle

# Function: loadData
# Parameter: filenameStr with a default value of connections_data.bin
# Return value: a list of dictionaries where each dictionary represents one puzzle.
# This function reads the binary file and creates a list of puzzles.
def loadData(filenameStr="connections_data.bin"):
    # use pickle
    fileObj = open("connections_data.bin", "rb")
    puzzleList = pickle.load(fileObj)
    fileObj.close()
    return puzzleList

# Function: loadData
# Parameter 1: puzzleList is the list to dump to a binary file
# Parameter 2: filenameStr with a default value of connections_data.bin
# Return value: None
# This function write the puzzleList to the binary file.
def dumpData(puzzleList, filenameStr="connections_data.bin"):
    # pickle
    fileObj = open(filenameStr, "wb")
    pickle.dump(puzzleList, fileObj)
    fileObj.close()

# Color codes for ANSI
def getColorCode(colorStr):
    colorDict = {"YELLOW": "\x1b[48;5;229m", "GREEN": "\x1b[48;5;114m", "BLUE": "\x1b[48;5;111m",
                 "PURPLE": "\x1b[48;5;140m", "GREY": "\x1b[48;5;255m", "RESET": "\u001B[0m",
                 "BLACK": "\x1b[30m"}

    if colorStr in colorDict:
        return colorDict[colorStr]
    else:
        print("pretty_print.getColorCode: invalid colorStr")
        return colorDict["GREY"]

# Function: randomizeList
# Parameter: wordList is a list of strings
# Return value: a list of strings which are the same strings from wordList but in a random order
# This function randomly gets items from the wordList to create a new list and returns the new list.
def randomizeList(wordList):
    randomList = []
    while wordList:
        randomItem = random.choice(wordList)
        randomList.append(randomItem)
        wordList.remove(randomItem)
    return randomList

def longestWordLength(wordList):
    max = 0
    for word in wordList:
        if len(word) > max:
            max = len(word)
    return max

def getSpaces(infoStr, wordMax=6, numSpaces=3):
    rowLen = (wordMax + numSpaces) * 4
    strLen = len(infoStr)
    diff = rowLen - strLen
    half = diff // 2
    return " " * half

def displayGroup(wordList, colorStr, connectStr, wordMax=6):
    ansiCode = getColorCode(colorStr)
    spacesBefore = getSpaces(connectStr, wordMax)
    spacesAfter = spacesBefore
    if len(connectStr) % 2 == 1:
        spacesAfter += " "
    print(ansiCode + spacesBefore + connectStr + spacesAfter, end="")
    print(getColorCode("RESET"))
    groupStr = ", ".join(wordList)
    spacesBefore = getSpaces(groupStr, wordMax)
    spacesAfter = spacesBefore
    if len(groupStr) % 2 == 1:
        spacesAfter += " "
    print(ansiCode + spacesBefore + groupStr + spacesAfter, end="")
    print(getColorCode("RESET"))

def displayRow(wordList, colorStr="GREY", wordMax=6, numSpaces=3):
    ansiCode = getColorCode(colorStr)
    fgCode = getColorCode("BLACK")
    endStr = " " * numSpaces
    for word in wordList:
        wordSize = len(word)
        if wordSize < wordMax:
            diff = wordMax - wordSize
            word = word + " " * diff
        print(fgCode + ansiCode + word, end=endStr)
    print(getColorCode("RESET"))

# Function: displayGrid
# Parameter 1: puzzleDict is a dictionary representing one puzzle
# Parameter 2: foundGroupList is a list of integers with the difficulty numbers of the groups that have been found
# and has a default value of [1, 2, 3, 4]
# Parameter 3: mistakes is an integer with the number of mistakes used to display the mistakes remaining message
# and has a default value of -1 (which means do not display the mistakes message)
def displayGrid(puzzleDict, foundGroupList=[1, 2, 3, 4], mistakes=-1):
    if type(puzzleDict) != dict:
        print("pretty_print.displayGrid: puzzleDict parameter needs to be a dictionary.")
    if type(foundGroupList) != list:
        print("pretty_print.displayGrid: foundGroupList parameter needs to be a list.")
    if type(mistakes) != int:
        print("pretty_print.displayGrid: mistakes parameter needs to be an integer.")

    spacesAfterWord = 3
    numWordsInRow = 4
    wordList = helper.getWordList(puzzleDict, foundGroupList)
    size = len(wordList)
    if size > 0:
        if type(wordList[0]) != str:
            print("pretty_print.displayGrid: helper.getWordList does not return a list of strings.")
            print("\tAre you returning a list of lists of strings?")
            return
    wordLen = longestWordLength(helper.getWordList(puzzleDict, []))
    longestConnection = len(helper.getConnection(puzzleDict, 1))
    for difficultyNum in range(2, 5):
        connectionLen = len(helper.getConnection(puzzleDict, difficultyNum))
        if connectionLen > longestConnection:
            longestConnection = connectionLen
    if (wordLen + spacesAfterWord) * numWordsInRow < longestConnection:
        wordLen = (longestConnection + spacesAfterWord) // numWordsInRow - spacesAfterWord

    print()
    message = "Create four groups of four!"
    spaces = getSpaces(message, wordLen)
    print(spaces + message)
    for num in foundGroupList:
        rowList = helper.getGroup(puzzleDict, num)
        connectStr = helper.getConnection(puzzleDict, num)
        colorStr = helper.getColor(puzzleDict, num)
        displayGroup(rowList, colorStr, connectStr, wordLen)

    wordList = randomizeList(wordList)
    rows = size // numWordsInRow
    for row in range(rows):
        startIndex = row * numWordsInRow
        stopIndex = startIndex + numWordsInRow
        rowList = wordList[startIndex:stopIndex]
        displayRow(rowList, "GREY", wordLen)
    if mistakes >= 0:
        remain = 4 - mistakes
        message = "Mistakes remaining: " + "* " * remain
        spaces = getSpaces(message, wordLen)
        print(getColorCode("RESET") + spaces + message)

    print(getColorCode("RESET"))

