# Typing Game in Python, by Lisong (Michael) Lin
![](https://github.com/m1chellelinn/Typing-Game/blob/main/game%20showcase.gif)


## About
This project is a typing test-style mini game, originally inspired by https://monkeytype.com. 
Over the winter break, I wanted to challenge myself on two things: to practice my coding ability, and to learn a new language. 
So, I tasked myself with learning the Python language and, with it, building a typing game that I've always enjoyed playing online. 

Through 14 hours in 2 weeks, the majority of source code is complete. I am currently working on adding more unit & intgration tests and improving documentation.
(If you see that the test file is empty, that is why!) 

&nbsp;

## Game Features
- Randomly generated sentences each round
- Live input feedback
  - Untyped characters are gray
  - Typed, correct characters are black/white
  - Typed, incorrect characters are red
- Customizable number-of-words goal for each round
- Customizable light/dark theme
- End-of-game statistics report
  - Elapsed time and typing speed
  - Number of correct and incorrect keystrokes

## Source Code Features
- Object-oriented player tracker objects (TypingTracker class in typing-game.py)
- Support to execute & play game on a GUI (in play-on-GUI.py)
- Support to execute & play game on terminal (in play-on-terminal.py)
