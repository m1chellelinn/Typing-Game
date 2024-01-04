import customtkinter
import tkinter
from typing_game import *

def processInput(char, action):
        

        if (action == '0'):
            myTracker.processInput('del')
        elif (action == '1'):
            myTracker.processInput(char)
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

        # we have to return True or False here, as part of the requirement for CustomTKInter's Text Validation
        if (myTracker.index >= myTracker.numChars - 1):
            # call function to open new window and display stats
            feedbackWindow = customtkinter.CTkToplevel()
            feedbackLabel = customtkinter.CTkLabel(feedbackWindow, text="aaaaa")
            feedbackLabel.pack()
            restartButton = customtkinter.CTkButton(feedbackWindow, text="restart?", command=restartGame)
            restartButton.pack()
            return False
        else:
            return True
    
def updateWordCountLabel(wordCount):
    wordCountLabel.configure(text="Current word count: " + '{:.0f}'.format(wordCount))

def restartGame():
    # stage 1: remove all colour tags, text from textbox, textentry
    outputBox.configure(state=tkinter.NORMAL)
    outputBox.tag_remove('red','1.0','end')
    outputBox.tag_remove('grey', '1.0', 'end')
    outputBox.tag_remove('cursor', '1.0', 'end')
    outputBox.delete('1.0', 'end')
    inputEntry.delete('0', 'end')

    # stage 2: reset the myTracker object with a new word count 
    wordCount = int(wordCountSlider.get())
    myTracker.reset(wordCount, words100, words3000)
    
    # stage 3: rebuild textbox with the new Tracker's string
    outputBox.insert('end', myTracker.correctWordString)
    outputBox.tag_add('cursor', '1.0', '1.1')
    outputBox.tag_add('grey', '1.0', 'end')
    outputBox.configure(state=tkinter.DISABLED)

def switchLightAndDark(choice):
    if (choice == "Light"):
        customtkinter.set_appearance_mode("light")
    elif (choice == "Dark"):
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("system")



if __name__ == '__main__':
    (words100, words3000) = initializeFiles()

    myTracker = TypingTracker(15, words100, words3000)

    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500x800")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=60,padx=10,fill="both",expand=True)

    currentInputLabel = customtkinter.CTkLabel(master=frame, text="", font=("Helvetica", 30))
    currentInputLabel.pack(pady = 5, padx = 5)

    inputEntry = customtkinter.CTkEntry(master=frame, validate='key')
    validationCommandName = inputEntry.register(processInput)
    inputEntry.configure(validatecommand=(validationCommandName, '%S', '%d'))
    inputEntry.pack()

    outputBox = customtkinter.CTkTextbox(frame, font=('Calibri', 28), width=500, height=200)
    outputBox.insert('end', myTracker.correctWordString)
    outputBox.tag_config('red', foreground='red', underline = 1)
    outputBox.tag_config('grey', foreground='grey', underline = 0)
    outputBox.tag_config('cursor', background = '#9ba3b0', underline = 0)
    outputBox.tag_add('cursor', '1.0', '1.1')
    outputBox.tag_add('grey', '1.0', 'end')

    outputBox.configure(state=tkinter.DISABLED)

    outputBox.pack(padx=0,pady=0)
    inputEntry.focus_force()

    wordCountLabel = customtkinter.CTkLabel(frame, text="Current word count: 15", font=("Helvetica", 15))
    wordCountLabel.pack()

    wordCountSlider = customtkinter.CTkSlider(frame, from_=1, to=40, number_of_steps=39, command=updateWordCountLabel)
    wordCountSlider.pack()
    wordCountSlider.set(15)

    wordCountSetButton = customtkinter.CTkButton(frame, text="Restart game with selected word count", command = restartGame)
    wordCountSetButton.pack()

    appearanceSelector = customtkinter.CTkComboBox(frame, values=["Light", "Dark", "System"], state="readonly", command=switchLightAndDark)
    appearanceSelector.pack()
    appearanceSelector.set("System")


    root.mainloop() #this blocks execution D:

