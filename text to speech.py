from tkinter import *
from gtts import gTTS
import os

def convert():
    conversion = gTTS(entry.get(),lang="hi")
    conversion.save("tts.wav")
    os.system("tts.wav")

main = Tk()

title = Label(main,text="TEXT TO SPEECH CONVERSION")
title.pack(padx=10,pady=10)

entry = Entry(main)
entry.pack(pady=10)

button = Button(main,text="CONVERT",command=convert)
button.pack(pady=10)

main.mainloop()