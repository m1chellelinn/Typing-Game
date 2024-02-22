import customtkinter
import tkinter
from typing_game import *
import time

# Hexadecimal colour codes used in my GUI
LIGHT_BLUE      = "#9badbd"
MUTED_BLUE      = "#6f819e"
DEEP_BLUE       = "#203659"
LIGHT_YELLOW    = "#958a72"
MUTED_YELLOW    = "#decaa2"
DEEP_YELLOW     = "#e2b714"
WHITE           = "#ffffff"
LGIHT_GRAY      = "#ebeef4"
GRAY            = "#9d9d9d"
DARK_GRAY       = "#494a4d"
DARK_DARK_GRAY  = "#323437"
BLACK           = "#000000"
WARNING_RED     = "#f75252"


def processInput(char, action):
        if (myTracker.index >= myTracker.numChars):
            return False
        
        if (action == '0'):
            myTracker.processInput('del')
        elif (action == '1'):
            myTracker.processInput(char)
        elif (action == '-1'):
            if (not inputEntry.focus_get() == '.!ctkframe.!ctkentry.!entry'):
                inputEntry.focus_set()
            return True
        # else: do nothing
        
        # unlock the textbox for modification
        outputBox.configure(state=tkinter.NORMAL)

        # remove all red and grey tags
        outputBox.tag_remove('red','1.0','end')
        outputBox.tag_remove('grey', '1.0', 'end')
        outputBox.tag_remove('cursor', '1.0', 'end')

        # then cycle the currentCorrectChars list. If we find a "wrong char", mark it red.
        for i in range(0,myTracker.numChars):
            if (not myTracker.currentCorrectChars[i]):
                outputBox.tag_add('red', f'1.{i}', f'1.{i+1}')

        # re-lock the textbox after modification
        outputBox.configure(state=tkinter.DISABLED)

        # then for all characters after index, mark it grey
        outputBox.tag_add('grey', f'1.{myTracker.index}', 'end')

        # then at index, mark it with the cursor tag (orange background)
        outputBox.tag_add('cursor', f'1.{myTracker.index}', f'1.{myTracker.index + 1}')

        # then update the progress label with the new count of characters
        progressLabel.configure(text = f"{myTracker.index} / {myTracker.numChars}")

        # we have to return True or False here, as part of the requirement for CustomTKInter's Text Validation
        if (myTracker.index >= myTracker.numChars):
            # call function to display stats
            (totalTime, wordsPerMinute, numTypos, percentCorrectStrokes, percentCorrectChars) = myTracker.calculateStats()
            feedbackDescription.configure(text = 
                                    f"- Total elapsed time: {'{:.2f}'.format(totalTime)} seconds\n" + 
                                    f"- WPM: {'{:.2f}'.format(wordsPerMinute)} words/min\n" + 
                                    f"- Number of typos: {numTypos}\n" + 
                                    f"- Correct inputs: {'{:.2f}'.format(percentCorrectStrokes * 100)}%\n" + 
                                    f"- Correct final characters: {'{:.2f}'.format(percentCorrectChars * 100)}%\n")
            return False
        return True
    
def updateWordCountLabel(wordCount):
    wordCountLabel.configure(text="Current word count: " + '{:.0f}'.format(wordCount))

def restartGame():
    # stage 1: remove all colour tags, text from textbox, textentry
    inputEntry.delete('0', 'end')
    outputBox.configure(state=tkinter.NORMAL)
    outputBox.tag_remove('red','1.0','end')
    outputBox.tag_remove('grey', '1.0', 'end')
    outputBox.tag_remove('cursor', '1.0', 'end')
    outputBox.delete('1.0', 'end')

    # stage 2: reset the myTracker object with a new word count 
    wordCount = int(wordCountSlider.get())
    myTracker.reset(wordCount, words100, words3000)
    
    # stage 3: rebuild textbox with the new Tracker's string
    outputBox.insert('end', myTracker.correctWordString)

    outputBox.tag_add('cursor', '1.0', '1.1')
    outputBox.tag_add('grey', '1.0', 'end')
    outputBox.configure(state=tkinter.DISABLED)

    progressLabel.configure(text = f"{myTracker.index} / {myTracker.numChars}")

    inputEntry.focus_force()

def switchLightAndDark(choice):
    if (choice == "Light"):
        customtkinter.set_appearance_mode("light")
        outputBox.tag_config('cursor', foreground = WHITE, background = MUTED_BLUE, underline = 0)
    elif (choice == "Dark"):
        customtkinter.set_appearance_mode("dark")
        outputBox.tag_config('cursor', foreground = BLACK, background = MUTED_YELLOW, underline = 0)


############ THE MAIN PYTHON SCRIPT STARTS HERE ############
if __name__ == '__main__':
    (words100, words3000) = initializeFiles()

    myTracker = TypingTracker(15, words100, words3000)

# Deals with the colours used in the GUI
    customtkinter.set_default_color_theme("dark-blue")
    customtkinter.set_appearance_mode("dark")
    textColour = "#E2B714"

# Creates the mainWindow object. This will be where we put all our widgets
    mainWindow = customtkinter.CTk(fg_color=(LGIHT_GRAY,BLACK))
    mainWindow.title("Python Typing Game, made with CustomTKInter")
    mainWindow.geometry("1152x648")
    mainWindow.grid_columnconfigure((0,2), weight=0)
    mainWindow.grid_columnconfigure((1,), weight=1)
    mainWindow.grid_rowconfigure(0, weight=1)

# Creates the left sidebar's frame. This acts as a visual separator and is nice to look at
    leftSidebarFrame = customtkinter.CTkFrame(mainWindow, width=150, corner_radius=0, bg_color=(LGIHT_GRAY,DARK_GRAY))
    leftSidebarFrame.grid(row = 0, column = 0, sticky = 'nsew', rowspan=2)
    leftSidebarFrame.grid_rowconfigure(2, weight=1)



# These are a series of text labels that go on the left side bar.
# The following three widgets fit in this frame
    # The grid row# and col#'s inside this frame may seem weird.
    # This is normal because, while this frame fits inside a grid of the main window,
    # it also contains a new grid inside itself. And that grid starts from row=0, col=0 all over again
    titleLabel = customtkinter.CTkLabel(leftSidebarFrame, text="Typing Game", font=("Verdana", 30, tkinter.font.BOLD), text_color = (DEEP_BLUE, DEEP_YELLOW))
    titleLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky='nw')

    instructionsLabel = customtkinter.CTkLabel(leftSidebarFrame, text="Instructions", font=("Verdana", 20), text_color = (DEEP_BLUE, DEEP_YELLOW))
    instructionsLabel.grid(row = 1, column = 0, padx = 10, pady = 0, sticky = 'w')

    instructionsDescription = customtkinter.CTkLabel(leftSidebarFrame, font=("Verdana", 14), text_color = (DEEP_BLUE, DEEP_YELLOW), justify = 'left',
                                                     text = "- Type the phrase in the middle!\n- Timer starts whenever you start\n" + 
                                                            "- Want a new phrase?\n   Choose a word count and\n   press \"Restart\" below!")
    instructionsDescription.grid(row = 2, column = 0, padx = 10, pady = 0, sticky = 'nw')

# These following are a word count label - displays the current selected word count
# a word count slider, where the user inputs the desired word count
# and a word count set button, which, on press, starts a new game with the chosen word count
    wordCountLabel = customtkinter.CTkLabel(leftSidebarFrame, text="Current word count: 15", font=("Consolas", 20), text_color = (DEEP_BLUE, DEEP_YELLOW))
    wordCountLabel.grid(row = 3, column = 0, sticky = 'w', padx = 20, pady = 0)

    wordCountSlider = customtkinter.CTkSlider(leftSidebarFrame, button_color=(DEEP_BLUE, DEEP_YELLOW), button_hover_color=(LIGHT_BLUE,LIGHT_YELLOW),
                                              from_=1, to=50, number_of_steps=49, command=updateWordCountLabel)
    wordCountSlider.grid(row = 4, column = 0, sticky = 'w', padx = 20, pady = 0)
    wordCountSlider.set(15)

    wordCountSetButton = customtkinter.CTkButton(leftSidebarFrame, corner_radius=13, border_width=2, 
                                                 border_color=(DEEP_BLUE, DEEP_YELLOW), fg_color='transparent', hover_color=(LIGHT_BLUE,LIGHT_YELLOW),
                                                 text="Restart", text_color = (DEEP_BLUE, DEEP_YELLOW), font = ("Consolas", 28), 
                                                 command = restartGame)
    wordCountSetButton.grid(row = 5, column = 0, sticky = 'sw', padx = 20, pady = 20)
    


# This is the heart of my implementation.
# This is where the user input gets taken by the TypingTracker class and outputted in real time with text highlighting
# CustomTKInter does not offer a widget that lets me take inputs AND format its text in real time,
# so I had to split this functionality in two parts.
    
# The first part is the input entry, where the user actually types to.
# this widget always get "input focus" as soon as the app is opened.
# Whenever a keystroke is detected, a function is called (processInput) to, well, 
# process this input and print it to the box in the second part
    inputEntry = customtkinter.CTkEntry(master=mainWindow, validate='all', width=0, height=0)
    validationCommandName = inputEntry.register(processInput)
    inputEntry.configure(validatecommand=(validationCommandName, '%S', '%d'))
    inputEntry.grid(row = 0, column = 1, sticky = 'nw', padx=50, pady=50)

# The second part is the output box, where we print out the "graded" text that we get from TypingTracker
    outputBox = customtkinter.CTkTextbox(mainWindow, corner_radius=10, wrap='word', border_spacing=70,
                                         fg_color=(WHITE, DARK_DARK_GRAY), font=('Cascadia Mono', 28), text_color = (DEEP_BLUE, WHITE))
    outputBox.insert('end', myTracker.correctWordString)
    outputBox.tag_config('red', foreground=WARNING_RED, underline = 1)
    outputBox.tag_config('grey', foreground=GRAY, underline = 0)
    outputBox.tag_config('cursor', foreground = BLACK, background = MUTED_YELLOW, underline = 0)
    outputBox.tag_add('cursor', '1.0', '1.1')
    outputBox.tag_add('grey', '1.0', 'end')
    outputBox.configure(state=tkinter.DISABLED)
    outputBox.grid(row = 0, column = 1, padx=7,pady=7, sticky = 'nsew')

# Creates a character counter, keeping track of how many characters the user has typed.
    progressLabel = customtkinter.CTkLabel(mainWindow, bg_color=(WHITE,DARK_DARK_GRAY), fg_color='transparent',
                                           font = ("Consolas", 20), text_color = (DEEP_BLUE,DEEP_YELLOW), 
                                           text = f"{myTracker.index} / {myTracker.numChars}", )
    progressLabel.grid(row = 0, column = 1, sticky = 'nw', pady=40, padx=80)

# Creates the right sidebar's frame. This is another visual separator, nice to look at.
# The following three widgets fit inside this frame
    rightSidebarFrame = customtkinter.CTkFrame(mainWindow, width = 200, corner_radius=0, bg_color=(WHITE, DARK_GRAY))
    rightSidebarFrame.grid(row = 0, column = 2, sticky = 'nsew', rowspan=2)
    rightSidebarFrame.rowconfigure(1, weight=1)

# A label with the title "Stats from last round"
    feedbackLabel = customtkinter.CTkLabel(rightSidebarFrame, text="Stats from last round", font = ("Verdana", 24, tkinter.font.BOLD), justify = 'left', text_color = (DEEP_BLUE, DEEP_YELLOW))
    feedbackLabel.grid(row = 0, column = 0, sticky = 'nw', padx = 5, pady = 20)

# A label with smaller text this time, detailing every stat that we get out of TypingTracker.calculateStats
    feedbackDescription = customtkinter.CTkLabel(rightSidebarFrame, text="play a round to find out!", font = ("Consolas", 14), justify = 'left', text_color = (DEEP_BLUE, DEEP_YELLOW))
    feedbackDescription.grid(row = 1, column = 0, sticky = 'nw', padx = 5, pady = 0)
    

# A dropdown menu that the user can use to select the appearance (light/dark) of this app
    appearanceSelector = customtkinter.CTkComboBox(rightSidebarFrame, corner_radius=13, border_width=2,
                                                   border_color=(DEEP_BLUE,DEEP_YELLOW), fg_color=(WHITE, DARK_GRAY), button_hover_color=(LIGHT_BLUE,LIGHT_YELLOW),
                                                   font = ("Consolas", 28), text_color = (DEEP_BLUE, DEEP_YELLOW), 
                                                   values=["Light", "Dark"], command=switchLightAndDark, state='readonly')
    appearanceSelector.grid(row = 3, column = 0, sticky = 'se', padx=20, pady=20)



# Adds finishing touches, fixes a bug in a really dumb way, and boots up the CustomTKInter window using .mainloop().
    appearanceSelector.after(500, lambda: appearanceSelector.set("Dark"))
    inputEntry.after(1000, lambda: inputEntry.focus_force())
    mainWindow.mainloop() 

