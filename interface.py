# ITP 115, Spring 2024
# Project
# Name: Austin Hong
# Email: austinjh@usc.edu
# Section: 32024
# Description: gets events, stores them, and reprints them

import helper
import pretty_print


def displayRules(textfileStr='game_rules.txt'):
    fileObj = open(textfileStr, 'r')
    for line in fileObj:
        print(line, end="")
    fileObj.close()


def isValidNumber(userStr, startNum, endNum):
    if userStr.isdigit():
        num = int(userStr)
        return startNum <= num <= endNum
    return False


def pickPuzzle(puzzleList):
    bigNum = len(puzzleList)
    valid = False
    while not valid:
        userValue = input("Enter a puzzle number (1-" + str(bigNum) + "): ")
        if isValidNumber(userValue, 1, bigNum):
            valid = True
    return helper.getPuzzleByNum(puzzleList, userValue)


def getGuessList(wordList):
    print("Enter four items for your guess:")
    guessList = []
    count = 0
    while count < 4:
        item = input("Item #" + str(count + 1) + ": ").strip().upper()
        if item in wordList and item not in guessList:
            guessList.append(item)
            count += 1
        else:
            print("Invalid input or duplicate word, please try again.")
    guessList.sort()
    return guessList


def checkConnection(puzzleDict, guessList):
    for diff in range(1, 5):
        sorting = helper.getGroup(puzzleDict, diff)
        if guessList == sorting:
            return diff
    return 0


def playGame(puzzleDict):
    foundGroups = []
    error = 0
    allGroups = 4
    lives = 4  # Total number of allowed mistakes

    while len(foundGroups) < allGroups and error < lives:
        pretty_print.displayGrid(puzzleDict, foundGroups)

        # Display remaining lives
        remainingLives = lives - error
        lifeSym = "* " * remainingLives
        print("Mistakes remaining: " + lifeSym)

        wordList = helper.getWordList(puzzleDict, foundGroups)
        guessList = getGuessList(wordList)
        result = checkConnection(puzzleDict, guessList)
        if result:
            foundGroups.append(result)
        else:
            error += 1
            print("\nIncorrect guess. Please try again.")

    pretty_print.displayGrid(puzzleDict)

    # Check if game is lost
    if error >= lives:
        print("Better luck next time.")
    else:
        print("Congratulations!")

    return error < lives


def savePuzzle(puzzleDict):
    date = puzzleDict['date'].replace(' ', '')
    fileN = date + ".txt"
    file = open(fileN, 'w')
    num = 1
    while num <= 4:
        color = helper.getColor(puzzleDict, num)
        connect = helper.getConnection(puzzleDict, num)
        sorting = helper.getGroup(puzzleDict, num)
        file.write(color + ": " + connect + " " + str(sorting) + "\n")
        num += 1
    file.close()
    print("Puzzle " + str(puzzleDict['num']) + " has been saved to " + fileN)
