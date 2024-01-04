import customtkinter
import tkinter

if __name__ == '__main__':
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500x800")

    def entry_verify(string):
        print("Current string: " + string)
        currentInputLabel.configure(text=string)
        outputBox.configure(state=tkinter.NORMAL)
        outputBox.insert('end', string[-1] if len(string) > 0 else "")
        outputBox.configure(state=tkinter.DISABLED)

        if (len(string) < 20): 
            return True
        else:
            return False
    
        
    def updateWordCountLabel(wordCount):
        wordCountLabel.configure(text="Current word count: " + '{:.0f}'.format(wordCount))

    def restartGame():
        return 0

        
    def switchLightAndDark(choice):
        if (choice == "Light"):
            customtkinter.set_appearance_mode("light")
        elif (choice == "Dark"):
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("system")

    frame = customtkinter.CTkFrame(master=root)

    frame.pack(pady=60,padx=10,fill="both",expand=True)


    currentInputLabel = customtkinter.CTkLabel(master=frame, text="", font=("Helvetica", 30))
    currentInputLabel.pack(pady = 5, padx = 5)




    inputEntry = customtkinter.CTkEntry(master=frame, validate='key')
    validationCommandName = inputEntry.register(entry_verify)
    inputEntry.configure(validatecommand=(validationCommandName, '%P'))
    inputEntry.pack()


    outputBox = customtkinter.CTkTextbox(frame, font=('Calibri', 14))
    outputBox.insert('end', "Lorem ipsum...\n...\n...'{:.2f}'.format(100 - ratioTypos * 100)nn\nnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnn\nnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    outputBox.tag_add('red', '1.0', '5.0')
    outputBox.tag_add('green', '6.0', '8.0')
    outputBox.tag_config('red', background='red', foreground='#FFFFFF')
    outputBox.tag_config('green', foreground='green')
    outputBox.configure(state=tkinter.DISABLED)
    outputBox.pack(padx=0,pady=0)
    inputEntry.focus_force()

    wordCountLabel = customtkinter.CTkLabel(frame, text="Current word count: 21", font=("Helvetica", 15))
    wordCountLabel.pack()

    wordCountSlider = customtkinter.CTkSlider(frame, from_=1, to=40, number_of_steps=39, command=updateWordCountLabel)
    wordCountSlider.pack()

    wordCountSetButton = customtkinter.CTkButton(frame, text="Restart game with selected word count", command = restartGame)

    appearanceSelector = customtkinter.CTkComboBox(frame, values=["Light", "Dark", "System"], state="readonly", command=switchLightAndDark)
    appearanceSelector.pack()
    appearanceSelector.set("System")


    root.mainloop() #this blocks execution D:

