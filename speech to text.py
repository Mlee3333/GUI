from tkinter import *
import speech_recognition
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile

def recording():
    recogniser = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = recogniser.listen(source)
        print(audio)
        try:
            text = recogniser.recognize_google(audio)
            textbox.delete(1.0,END)
            textbox.insert(END,text)
            print(text)
        except:
            messagebox.showinfo("ERROR","COULD NOT IDENTIFY SPEECH")

def convert():
    text = textbox.get(1.0,END)
    file = asksaveasfile()
    print(text,file=file)
    


main = Tk()

title = Label(main,text="Speech to text")
title.grid(column=0,row=0,columnspan=3)

record = Button(main,text="Record",command=recording)
record.grid(row=1,column=0)

textbox = Text(main,width=30,height=7)
textbox.grid(row=1,column=1,padx=5,pady=5)

convertb = Button(main,text="Convert",command=convert)
convertb.grid(row=1,column=2)

main.mainloop()