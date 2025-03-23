from tkinter import *
from tkinter import messagebox

details = {}

def clear():
    nameent.delete(0,END)
    addressent.delete(0,END)
    numberent.delete(0,END)
    emailent.delete(0,END)

def add_update():
    name = nameent.get().strip()
    if name == "":
        messagebox.showinfo("NO ENTRY","Please enter a name")
    else:
        address = addressent.get()
        number = numberent.get()
        email = emailent.get()
        if name not in details:
            entries.insert(END,name)
        details[name] = [address,number,email]
        clear()
        print(details)

def edit():
    clear()
    key = entries.curselection()
    if key:  
        name = entries.get(key)
        nameent.insert(END,name)
        addressent.insert(END,details[name][0])
        numberent.insert(END,details[name][1])
        emailent.insert(END,details[name][2])
    else:
        messagebox.showinfo("SELECT ITEM", "Please select an item")

main = Tk()

title = Label(main,text="ADDRESS BOOK")
title.grid(row=0,column=1,padx=10,pady=10)

entries = Listbox(main,height=15,width=30)
entries.grid(row=1,column=0,columnspan=2,rowspan=8,padx=10,pady=10)

namelbl = Label(main,text="NAME:")
namelbl.grid(row=1,column=2,padx=10)
nameent = Entry(main)
nameent.grid(row=2,column=2,padx=10,pady=10)

addresslbl = Label(main,text="ADDRESS:")
addresslbl.grid(row=3,column=2,padx=10)
addressent = Entry(main)
addressent.grid(row=4,column=2,padx=10,pady=10)

numberlbl = Label(main,text="MOBILE NUMBER:")
numberlbl.grid(row=5,column=2,padx=10)
numberent = Entry(main)
numberent.grid(row=6,column=2,padx=10,pady=10)

emaillbl = Label(main,text="EMAIL:")
emaillbl.grid(row=7,column=2,padx=10)
emailent = Entry(main)
emailent.grid(row=8,column=2,padx=10,pady=10)

addbtn = Button(main,text="ADD/ UPDATE",command=add_update)
addbtn.grid(row=9,column=2)

editbtn = Button(main,text="EDIT",command=edit)
editbtn.grid(row=9,column=0,padx=10,pady=10)

deletebtn = Button(main,text="DELETE",command=None)
deletebtn.grid(row=9,column=1)

savebtn = Button(main,text="SAVE",command=None)
savebtn.grid(row=10,column=1,padx=10,pady=10)

openbtn = Button(main,text="OPEN",command=None)
openbtn.grid(row=0,column=2)

main.mainloop()