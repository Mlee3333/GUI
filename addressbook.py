from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
import os

details = {}

def save():
    file = asksaveasfile()
    filetext = details
    print(filetext,file=file)
    reset()

def open():
    global details
    reset()
    entries.delete(0,END)
    file = askopenfile()
    if file:
        details = eval(file.read())
        for i in details:
            entries.insert(END,i)
    else:
        messagebox.showinfo("No file","Please select a valid file")
    title.config(text=os.path.basename(file.name))

def clear():
    nameent.delete(0,END)
    addressent.delete(0,END)
    numberent.delete(0,END)
    emailent.delete(0,END)
    title.config(text="Address Book")

def reset():
    clear()
    entries.delete(0,END)
    details.clear()

def delete():
    entries.config(entries.delete(entries.curselection()))    

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

def click(event):
    window = Toplevel(main)
    index = entries.curselection()
    name = entries.get(index)
    address = details[name][0]
    number = details[name][1]
    email = details[name][2]
    text = "Name: {} \nAddress: {} \nNumber: {} \nEmail: {}".format(name,address,number,email)
    label = Label(window,text=text)
    label.pack()

main = Tk()

title = Label(main,text="ADDRESS BOOK")
title.grid(row=0,column=1,padx=10,pady=10)

entries = Listbox(main,height=15,width=30)
entries.bind("<<ListboxSelect>>",click)
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

deletebtn = Button(main,text="DELETE",command=delete)
deletebtn.grid(row=9,column=1)

savebtn = Button(main,text="SAVE",command=save)
savebtn.grid(row=10,column=1,padx=10,pady=10)

openbtn = Button(main,text="OPEN",command=open)
openbtn.grid(row=0,column=2)

main.mainloop()