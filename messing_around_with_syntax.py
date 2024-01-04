import customtkinter
import tkinter

if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500x500")

    def start():
        customtkinter.set_appearance_mode("light")
    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)

    def entry_verify(string):
        print("Current string: " + string)
        label.configure(text=string)
        text.configure(state=tkinter.NORMAL)
        text.insert('end', string[-1] if len(string) > 0 else "")
        text.configure(state=tkinter.DISABLED)

        if (len(string) < 20): 
            return True
        else:
            return False

    frame = customtkinter.CTkFrame(master=root)

    frame.pack(pady=60,padx=10,fill="both",expand=True)


    label = customtkinter.CTkLabel(master=frame, text="", font=("Helvetica", 30))
    label.pack(pady = 5, padx = 5)




    entry3 = customtkinter.CTkEntry(master=frame, validate='key')
    validationCommandName = entry3.register(entry_verify)
    entry3.configure(validatecommand=(validationCommandName, '%P'))
    entry3.pack()


    text = customtkinter.CTkTextbox(frame, font=('Calibri', 14))
    text.insert('end', "Lorem ipsum...\n...\n...nnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnn\nnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnnnn\nnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    text.tag_add('red', '1.0', '5.0')
    text.tag_add('green', '6.0', '8.0')
    text.tag_config('red', background='red', foreground='#FFFFFF')
    text.tag_config('green', foreground='green')
    text.configure(state=tkinter.DISABLED)
    text.pack(padx=0,pady=0)
    
    entry3.grab_set()
    root.mainloop() #this blocks execution D:

