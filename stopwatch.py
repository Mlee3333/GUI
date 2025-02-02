from tkinter import *
from tkinter import messagebox
import time

def zero():
    hours.set("00")
    minutes.set("00")
    seconds.set("00")
    entryH.config(state="normal")
    entryM.config(state="normal")
    entryS.config(state="normal")

def start():
    entryH.config(state="disabled")
    entryM.config(state="disabled")
    entryS.config(state="disabled")
    try:
        hrs = int(hours.get())
        mins = int(minutes.get())
        secs = int(seconds.get())
        timeT = hrs*3600 + mins*60 + secs
        print(timeT)

    except:
        print("Enter the correct values")
        timeT = 0
    
    while timeT > 0:
        mins, secs = divmod(timeT,60)
        hrs, mins = divmod(mins,60)
        hours.set(hrs)
        minutes.set(mins)
        seconds.set(secs)
        main.update()
        time.sleep(1)
        timeT -= 1
        
    messagebox.showinfo("Time is Up","TIME IS UP!")
    zero()

main = Tk()

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

entryH = Entry(main,textvariable=hours)
entryM = Entry(main,textvariable=minutes)
entryS = Entry(main,textvariable=seconds)
entryH.grid(column=1,row=1,padx=10,pady=10)
entryM.grid(column=2,row=1,padx=10,pady=10)
entryS.grid(column=3,row=1,padx=10,pady=10)

button = Button(main,text="Start",command=start)
button.grid(row=2,column=2)
zero()

main.mainloop()