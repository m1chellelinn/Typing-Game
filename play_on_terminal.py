import msvcrt
import os
from typing_game import *


if __name__ == '__main__':
    clearTerminal = lambda: os.system('cls')
    (words100, words3000) = initializeFiles()
    
    while True:
        # Gets if the user wants to play another round
        clearTerminal()
        userAnswer = input("\033[91m{}\033[00m".format('Typing Game in Python.\n') + "Please enter a positive number to indicate the number of words to type.\n- Enter anything else to end the program.\n")
        if userAnswer.isdigit():
            wordsCount = int(userAnswer)
            if (wordsCount <= 0): 
                break
        else:
            break

        # Initializes the string and terminal to prepare to start the game
        clearTerminal()
        myTracker = TypingTracker(wordsCount, words100, words3000)
        print('v\n' + "\033[2m{}\033[00m".format(myTracker.correctWordString) + '\n^\n')
        print(f'Starting game with {wordsCount} words. Type the words above as fast as you can!')

        while myTracker.index < myTracker.numChars:
            newByteStr = msvcrt.getch()
            
            if newByteStr == b'\r':
                break
            
            if newByteStr == b'\x08':
                newStr = 'del'
            else: 
                newStr = newByteStr.decode()
            
            myTracker.processInput(newStr)

            outputUpper = ""
            outputMiddleLeft = ""
            outputMiddleRight = ""
            outputLower = ""

            clearTerminal()
            for i in range(0, myTracker.numChars):
                if i < myTracker.index: 
                    outputLower += ' ' if myTracker.currentCorrectChars[i] else 'X'
                    outputUpper += ' '
                    outputMiddleLeft += myTracker.correctWordString[i]
                elif i == myTracker.index:
                    outputLower += '^'
                    outputUpper += 'v'
                    outputMiddleRight += myTracker.correctWordString[i]
                else:
                    outputMiddleRight += myTracker.correctWordString[i]
            
            
            print("\033[1m{}\033[00m".format(outputUpper) + '\n' + outputMiddleLeft + "\033[2m{}\033[00m".format(outputMiddleRight) + '\n' + "\033[1m{}\033[00m".format(outputLower))
        
        clearTerminal()
        (totalTime, wordsPerMinute, totalTypos, ratioTypos, finalRatioCorrects) = myTracker.calculateStats()
        print(
            f"Stats:\n- Total elapsed time: {'{:.2f}'.format(totalTime)} seconds\n" + 
            f"- Word-per-minute: {'{:.2f}'.format(wordsPerMinute)} words/min\n" + 
            f"- Number of typos made: {totalTypos}\n" + 
            f"- Percentage of correct inputs: {'{:.2f}'.format(ratioTypos * 100)}%\n" + 
            f"- Percentage of correct (final) characters: {'{:.2f}'.format(finalRatioCorrects * 100)}%\n")
        
        print("Press any key to continue!")
        msvcrt.getch()
        clearTerminal()