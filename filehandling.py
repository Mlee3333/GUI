from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile

def save():
    file = asksaveasfile()
    filetext = text.get(1.0,END)
    print(filetext,file=file)
    text.delete(1.0,END)

def open():
    file = askopenfile(filetypes=[("Python Files","*.py"),("Text Document","*.txt")])
    filetext = file.read()
    text.insert(END,filetext)
    print(filetext)

main = Tk()

openbtn = Button(main,text="OPEN",command=open)
openbtn.pack(padx=30,pady=30)

text = Text(main)
text.pack()

savebtn = Button(main,text="SAVE",command=save)
savebtn.pack(padx=30,pady=30)

main.mainloop()