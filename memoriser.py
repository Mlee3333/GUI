from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile

def save():
    file = asksaveasfile()
    filetext = text.get(0,END)
    for i in filetext:
        print(i.strip(),file=file)
    text.delete(0,END)

def open():
    text.delete(0,END)
    file = askopenfile()
    for i in file:
     text.insert(END,i)

def delete():
    text.config(text.delete(text.curselection()))

def add():
    text.insert(END,entry.get())
    entry.delete(0,END)

main = Tk()

entry = Entry(main,width=50)
entry.grid(row=1,column=1,pady=10)

text = Listbox(main,width=50)
for i in range(0,30):
    text.insert(END,"LIST "+str(i))
text.grid(padx=20,pady=2,row=2,column=1)

savebtn = Button(main,text="SAVE",command=save)
savebtn.grid(padx=30,pady=30,row=3,column=1)

addbtn = Button(main,text="ADD",command=add)
addbtn.grid(padx=30,pady=30,row=1,column=0)

deletebtn = Button(main,text="DELETE",command=delete)
deletebtn.grid(padx=30,pady=30,row=1,column=2)

openbtn = Button(main,text="OPEN",command=open)
openbtn.grid(row=4,column=1)

main.mainloop()