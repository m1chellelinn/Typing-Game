import random
import time

class TypingTracker (object):
    """
    Abstraction function: Each TypingTracker object represents the state of a game of "typing game". 

    Representation invariant: all fields described in the constructor are not None

    Thread Safety Argument: This class is NOT thread safe. 
        However, all implementations of this class is purely sequential, so concurrent bugs are impossible. 
        (the GUI may seem multi-threaded at first. However, its mainloop() function is actually single-threaded).
 
    """
    
    def __init__(self, wordCount, words100, words3000):
        """
        Instantiates an object whose instance fields keep track of the game state

        Requires: 
            - words100 and words3000 are two tuples/lists of random English words. 
              Each element may contain letters, numbers, or dashes.
            - wordCount is an integer and wordCount > 0
        
        Modifies: nothing

        Returns: An object with the fields:
            - correctWordString - the string that the player will type
            - currentWordString - the string that the player has typed so far
            - currentCorrectChars - a list of booleans, each element representing whether
              the player's input at that index was correct
            - keyStrokeTimes - the system time at which each player input was made

            - numChars - the length of the correct word string
            - wordCount - the number of words in the correct word string
            - index - the position (index) of the player's cursor relative to the word string
            - totalTypos - the number of user inputs which were wrong
            - totalKeyStrokes - the number of user inputs made
        """
        wordString = ""

        for i in range(0, wordCount):
            if i % 2 == 1:
                wordString += (random.choice(words3000)).rstrip('\n')
            else:
                wordString += (random.choice(words100)).rstrip('\n')
        
        wordString = wordString.strip()
        
        self.index = 0
        self.correctWordString = wordString
        self.numChars = len(self.correctWordString)
        self.wordCount = wordCount

        # CurrentWordString: everything the user has typed until now
        # CurrentCorrecChars: did the user type everything correctly?
        self.currentWordString = ''
        self.currentCorrectChars = []
        for i in range(0,self.numChars):
            self.currentCorrectChars.append(True)

        # These deal with calculating statistics at the end of each round 
        # and is tracked throughout the round
        self.totalTypos = 0
        self.totalKeyStrokes = 0
        self.keyStrokeTimes = []
        for i in range(0,self.numChars):
            self.keyStrokeTimes.append(0)
        

    def processInput(self,input):
        """
        Processes a specific user input
        
        Requires: input is a string that is either 
            an ASCII-representable character, or the string "del"

        Modifies: all or nearly all fields in this TypingTracker object

        Returns: nothing
        """
        self.totalKeyStrokes += 1

        if input == 'del':
            if self.index > 0:
                self.index -= 1
                self.currentWordString = self.currentWordString[0:self.index]
        elif self.index >= len(self.correctWordString): 
            # do nothing. the game has ended
            self.totalKeyStrokes += 1
        elif input == ' ':
            self.currentCorrectChars[self.index] = True if (self.correctWordString[self.index] == ' ') else False
                
            if self.index > 0:
                while (not self.correctWordString[self.index - 1] == ' '):
                    self.index += 1
                    self.currentWordString += ' '
        else:
            self.currentWordString += input
            if input == self.correctWordString[self.index]:
                self.currentCorrectChars[self.index] = True
            else: 
                self.currentCorrectChars[self.index] = False
                self.totalTypos += 1
            self.keyStrokeTimes[self.index] = time.time()
            
            self.index += 1
        # This is a cheat code entirely for demo purposes
        # elif input == '`':
        #     self.currentWordString += input
        #     self.keyStrokeTimes[self.index] = time.time()
        #     self.index += 1

        # else do nothing: this input is not important
            
    def calculateStats(self):
        """
        At the end of each game, provides useful player statistics in a tuple
        
        Requires: nothing

        Modifies: nothing

        Returns: a tuple where:
        - the first element is the total elapsed time, 
        - the second element is the (average) words typed per minute
        - the third element is the number of typos made, 
        - the fourth element is the percentage of correct keystrokes
        - the fifth element is the percentage of correct characters (at the end of the game)
        """
        numCorrect = 0
        for correct in self.currentCorrectChars:
            if correct: numCorrect += 1
        return ((self.keyStrokeTimes[-1] - self.keyStrokeTimes[0]), 
                self.wordCount / (self.keyStrokeTimes[-1] - self.keyStrokeTimes[0]) * 60,
                self.totalTypos, 1 - self.totalTypos / self.totalKeyStrokes, 
                numCorrect / self.numChars)
    
    def reset(self, wordCount, words100, words3000):
        """
        Resets this TypingTracker object.
        
        This is almost indentical to the constructor. 
        I just made this because I needed a way to mutate object fields while 
        passing by reference 
        (the constructor just replace the object with a new one, breaking the reference to the original,
        which was not the desired effect since no fields in the original are changed) 
        """
        wordString = ""
        for i in range(0, wordCount):
            if i % 2 == 1:
                wordString += (random.choice(words3000)).strip() + ' '
            else:
                wordString += (random.choice(words100)).strip() + ' '
        wordString = wordString.strip()
        self.index = 0
        self.correctWordString = wordString
        self.numChars = len(self.correctWordString)
        self.wordCount = wordCount
        self.currentWordString = ''
        self.currentCorrectChars = []
        for i in range(0,self.numChars):
            self.currentCorrectChars.append(True)
        self.totalTypos = 0
        self.totalKeyStrokes = 0
        self.keyStrokeTimes = []
        for i in range(0,self.numChars):
            self.keyStrokeTimes.append(0)


def initializeFiles():
    """
    Initializes two lists of random words, returns them in a tuple.
    
    Requires: the two files "popular100.txt" and "popular3000.txt" be formatted as follows:
        - Contains ASCII-representable characters
        - Each line may contain words, numbers, or a mix of both. 
        - Each line may end in whitespaces, then a newline
        - Each line may start with whitespaces
    
    Modifies: nothing

    Returns: a tuple where the the first element is a list of lines from the first file, 
        and the second element is a list of lines from the second file. 
        Each elements in these two lists may start & end with whitespaces, 
        and may contain ASCII-representable characters
    """
    words100 = []
    with open('popular100.txt', 'r') as file100:
        for line in file100:
            words100.append(line)

    words3000 = []
    with open('popular3000.txt', 'r') as file3000:
        for line in file3000:
            words3000.append(line)
    
    return (words100, words3000)