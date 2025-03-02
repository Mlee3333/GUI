from tkinter import *

def change():
    main.config(background=colours.get(colours.curselection()))

def delete():
    colours.config(colours.delete(colours.curselection()))

def add():
    colours.insert(END,entry.get())
    entry.delete(0,END)

main = Tk()

entry = Entry(main,width=50)
entry.pack(padx=20,pady=20)

addB = Button(main,text="ADD",width=10,command=add)
addB.pack()

deleteB = Button(main,text="DELETE",width=10,command=delete)
deleteB.pack(padx=20,pady=20)

colours = Listbox(main,width=20)
colours.insert(END,"red","green","blue","yellow","pink","orange","purple")
colours.pack()

changeB = Button(main,text="CHANGE COLOUR",width=20,command=change)
changeB.pack(padx=20,pady=20)

main.mainloop()