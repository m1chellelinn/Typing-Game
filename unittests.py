import unittest
from typing_game import *
import time

class TestTypingGame(unittest.TestCase):

    def test_initializeFiles(self):
        (words100, words3000) = initializeFiles()

        self.assertEqual(len(words100), 100)
        self.assertEqual(len(words3000), 3200)

    def test_initiate(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(1, words100, words3000)

        self.assertEqual(myTracker.index, 0)
        self.assertEqual(len(myTracker.currentWordString), 0)

    def test_short_input(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(20, words100, words3000)

        input1 = ['a', 'b', 'c', 'd', 'e']
        for char in input1:
            myTracker.processInput(char)
        self.assertEqual(len(myTracker.currentWordString), 5)
        self.assertEqual(myTracker.index, 5)

        input2 = ['f', 'g', '-', '.', 'del', 'a']
        for char in input2:
            myTracker.processInput(char)
        self.assertEqual(len(myTracker.currentWordString), 9)
        self.assertEqual(myTracker.totalKeyStrokes, 11)

    def test_correct_input(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(10000, words100, words3000)

        input = myTracker.correctWordString

        startTime = time.time()
        for char in input:
            myTracker.processInput(char)
        endTime = time.time()

        (totalTime, wpm, numTypos, perCorrectStrokes, perCorrectChars) = myTracker.calculateStats()

        self.assertEqual(len(myTracker.correctWordString), len(myTracker.currentWordString))
        self.assertEqual(perCorrectChars, 1)
        self.assertEqual(perCorrectStrokes, 1)
        self.assertEqual(numTypos, 0)
        self.assertTrue(totalTime <= (endTime - startTime))
    
    def test_wrong_input(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(10000, words100, words3000)

        input = myTracker.correctWordString

        startTime = time.time()
        for char in input:
            if (char == 'a'):
                myTracker.processInput('b')
            else:
                myTracker.processInput('a')

        endTime = time.time()

        (totalTime, wpm, numTypos, perCorrectStrokes, perCorrectChars) = myTracker.calculateStats()

        self.assertEqual(len(myTracker.correctWordString), len(myTracker.currentWordString))
        self.assertEqual(perCorrectChars, 0)
        self.assertEqual(perCorrectStrokes, 0)
        self.assertEqual(numTypos, len(input))
        self.assertTrue(totalTime <= (endTime - startTime))

    def test_too_long_input(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(1, words100, words3000)

        for i in range(0, 1000):
            myTracker.processInput('a')
        self.assertEqual(len(myTracker.correctWordString), len(myTracker.currentWordString))
        self.assertEqual(len(myTracker.keyStrokeTimes), len(myTracker.correctWordString))

    def test_reset(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(1, words100, words3000)

        for i in range(0, 1000):
            myTracker.processInput('a')

        myTracker.reset(100, words100, words3000)
        self.assertEqual(myTracker.index, 0)
        self.assertEqual(len(myTracker.currentWordString), 0)

    def test5(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(1, words100, words3000)

    def test6(self):
        (words100, words3000) = initializeFiles()
        myTracker = TypingTracker(1, words100, words3000)


if __name__ == '__main__':
    unittest.main()
    
