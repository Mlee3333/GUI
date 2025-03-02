from tkinter import *
from tkinter.ttk import Progressbar
import time

def collect():
    text = spinbox.get()
    displalbl.config(text=text)


def showprogress():
    progress["value"]=20
    main.update_idletasks()
    time.sleep(1)
    progress["value"]=40
    main.update_idletasks()
    time.sleep(1)
    progress["value"]=60
    main.update_idletasks()
    time.sleep(1)
    progress["value"]=80
    main.update_idletasks()
    time.sleep(1)
    progress["value"]=100
    main.update_idletasks()

main = Tk()

spinbox = Spinbox(main,from_=0,to=30)
spinbox.pack(padx=30,pady=30)

display = Button(main,text="DISPLAY",command=collect)
display.pack()

displalbl = Label(main)
displalbl.pack()

progress = Progressbar(main,mode="indeterminate")
progress.pack()

progressbtn = Button(main,text="SHOW PROGRESS",command=showprogress)
progressbtn.pack()

main.mainloop()