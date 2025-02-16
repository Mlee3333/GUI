from tkinter import *
from tkinter.ttk import *

def order():
    type = Varchoice.get()
    size = Varsize.get()
    number = Varnum.get()
    confirmation.config(text="You ordered {} {} {} Pizza(s)".format(number,size,type))


main = Tk()

title = Label(main,text="Welcome to Pizza Hut")
title.grid(column=0,row=0,columnspan=3)

type = Label(main,text="Type of Pizza: ")
type.grid(column=0,row=1,padx=10,pady=10)

choices = ["Margherita","Meat feast","Hawaiian","Chicken and Sweetcorn"]
Varchoice = StringVar()
Varchoice.set(choices[0])
menu = OptionMenu(main,Varchoice,*choices)
menu.grid(row=1,column=1)

num = Label(main,text="Number of Pizzas: ")
num.grid(row=2,column=0,padx=10,pady=10)

Varnum = IntVar()

combo = Combobox(main,textvariable=Varnum,values= tuple(range(1,10)))
combo.grid(row=2,column=1)

size = Label(main,text="Pizza Size: ")
size.grid(row=3,column=0,padx=10,pady=10)

Varsize = StringVar()
Varsize.set("small")

radS = Radiobutton(main,text="Small",value="small",variable=Varsize)
radS.grid(row=3,column=1)

radM = Radiobutton(main,text="Medium",value="medium",variable=Varsize)
radM.grid(row=3,column=2)

radL = Radiobutton(main,text="Large",value="large",variable=Varsize)
radL.grid(row=3,column=3)

orderBtn = Button(main,text="Order",command=order)
orderBtn.grid(row=4,column=1,columnspan=2)

confirmation = Label(main)
confirmation.grid(row=5,column=0,columnspan=4)

main.mainloop()