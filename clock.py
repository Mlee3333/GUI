from tkinter import *
from time import strftime
from tkinter import font as f

def timeF():
    timeN = strftime("%H:%M:%S %Z")
    clock.config(text=timeN)
    clock.after(1000,timeF)

main = Tk()
main.title("Clock")
FONT = f.Font(family="calibri",weight="bold",size=30)
clock = Label(main,font=FONT,background="red",foreground="white")
clock.pack()
timeF()


main.mainloop()