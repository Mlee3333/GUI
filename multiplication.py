from tkinter import *
from tkinter.ttk import *

totalA = ""

def generate():
    global totalA
    number = varN.get()
    rangeV = varR.get()
    for i in range(1,rangeV+1):
        mult = str(number)+" X "+str(i)+" = "+str(i*number)+"\n"
        totalA = totalA + mult
    answers.config(text=totalA)

main = Tk()

title = Label(main,text="Multiplication Table:")
title.grid(column=0,row=0,columnspan=3)

label = Label(main,text="Number and Range")
label.grid(row=1,column=0,padx=10,pady=10)

varN = IntVar()
varR = IntVar()
varR.set(10)

combo = Combobox(main,textvariable=varN,values= tuple(range(1,100)))
combo.grid(row=1,column=1,padx=10,pady=10)

rad10 = Radiobutton(main,text="10",value=10,variable=varR)
rad10.grid(row=1,column=2,padx=10,pady=10)

rad20 = Radiobutton(main,text="20",value=20,variable=varR)
rad20.grid(row=2,column=2,padx=10)

rad30 = Radiobutton(main,text="30",value=30,variable=varR)
rad30.grid(row=3,column=2,padx=10,pady=10)

generateB = Button(main,text="Generate",command=generate)
generateB.grid(row=3,column=1)

answers = Label(main)
answers.grid(row=4,column=1)

main.mainloop()