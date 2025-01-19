from tkinter import *

def action():
    text = entry.get()
    label2.config(text=text+" successfully logged in")

main = Tk()
main.geometry("300x300")
main.title("main")
main.config(background="red")
label2 = Label(main)
label2.pack(side="top")
label = Label(main,text="Username")
label.pack(side="left")
entry = Entry(main)
entry.pack(side="right")
button = Button(main,text="Login",command=action)
button.pack(side="bottom")
close = Button(main,text="Close",command=main.destroy)
close.pack(side="bottom")
main.mainloop()