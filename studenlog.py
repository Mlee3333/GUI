from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile

def save():
    file = asksaveasfile()
    filetext = entries.get(0,END)
    for i in filetext:
        print(i.strip(),file=file)
    entries.delete(0,END)

def open():
    entries.delete(0,END)
    file = askopenfile()
    for i in file:
     entries.insert(END,i)

details = {}

def clear():
    nameent.delete(0,END)
    ident.delete(0,END)
    ment.delete(0,END)
    eent.delete(0,END)
    sent.delete(0,END)

def delete():
    entries.config(entries.delete(entries.curselection()))    

def add_update():
    name = nameent.get().strip()
    if name == "":
        messagebox.showinfo("NO ENTRY","Please enter a name")
    else:
        id = ident.get()
        maths = ment.get()
        english = eent.get()
        science = sent.get()
        if name not in details:
            entries.insert(END,name)
        details[name] = [id,maths,english,science]
        clear()
        print(details)

def edit():
    clear()
    key = entries.curselection()
    if key:  
        name = entries.get(key)
        nameent.insert(END,name)
        ident.insert(END,details[name][0])
        ment.insert(END,details[name][1])
        eent.insert(END,details[name][2])
        sent.insert(END,details[name][3])
    else:
        messagebox.showinfo("SELECT ITEM", "Please select an item")

main = Tk()

title = Label(main,text="STUDENT LOG")
title.grid(row=0,column=0,padx=10,pady=10,columnspan=5)

entries = Listbox(main,height=5,width=100)
entries.grid(row=3,column=0,columnspan=5,rowspan=3,padx=10,pady=10)

namelbl = Label(main,text="NAME:")
namelbl.grid(row=1,column=0,padx=10)
nameent = Entry(main)
nameent.grid(row=1,column=1,padx=10)

idlbl = Label(main,text="STUDENT ID:")
idlbl.grid(row=2,column=0,padx=10,pady=10)
ident = Entry(main)
ident.grid(row=2,column=1,padx=10,pady=10)

mlbl = Label(main,text="MATHS %:")
mlbl.grid(row=1,column=2,padx=10)
ment = Entry(main)
ment.grid(row=1,column=3,padx=10)

elbl = Label(main,text="ENGLISH %:")
elbl.grid(row=2,column=2,padx=10,pady=10)
eent = Entry(main)
eent.grid(row=2,column=3,padx=10,pady=10)

slbl = Label(main,text="SCIENCE %:")
slbl.grid(row=1,column=4,padx=10)
sent = Entry(main)
sent.grid(row=1,column=5,padx=10)

addbtn = Button(main,text="ADD/ UPDATE",command=add_update)
addbtn.grid(row=2,column=5,padx=10,pady=10)

editbtn = Button(main,text="EDIT",command=edit)
editbtn.grid(row=3,column=5,padx=10)

deletebtn = Button(main,text="DELETE",command=delete)
deletebtn.grid(row=5,column=5,padx=10)

menubar = Menu(main)
file = Menu(menubar,tearoff=0)
file.add_command(label="Save",command=save)
file.add_command(label="Open",command=open)
menubar.add_cascade(label="File",menu=file)
main.config(menu=menubar)

main.mainloop()