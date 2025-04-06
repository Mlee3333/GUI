from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
import os
from time import strftime
from tkinter import font as f
from gtts import gTTS

turn = "X"
win = False

def create(window):
    
    def clicked(button):
        global turn
        if button["text"] == " " and turn == "X":
            button["text"] = turn
            turn = "O"
        elif button["text"] == " " and turn == "O":
            button["text"] = turn
            turn = "X"
        else:
            messagebox.showerror("Student Logger","That box has already been selected!!")
        check()

    tl = Button(window,width=10,height=5,command=lambda:clicked(tl),text=" ")
    tm = Button(window,width=10,height=5,command=lambda:clicked(tm),text=" ")
    tr = Button(window,width=10,height=5,command=lambda:clicked(tr),text=" ")
    ml = Button(window,width=10,height=5,command=lambda:clicked(ml),text=" ")
    mm = Button(window,width=10,height=5,command=lambda:clicked(mm),text=" ")
    mr = Button(window,width=10,height=5,command=lambda:clicked(mr),text=" ")
    bl = Button(window,width=10,height=5,command=lambda:clicked(bl),text=" ")
    bm = Button(window,width=10,height=5,command=lambda:clicked(bm),text=" ")
    br = Button(window,width=10,height=5,command=lambda:clicked(br),text=" ")
    tl.grid(padx=3,pady=3,column=0,row=1)
    tm.grid(padx=3,pady=3,column=1,row=1)
    tr.grid(padx=3,pady=3,column=2,row=1)
    ml.grid(padx=3,pady=3,column=0,row=2)
    mm.grid(padx=3,pady=3,column=1,row=2)
    mr.grid(padx=3,pady=3,column=2,row=2)
    bl.grid(padx=3,pady=3,column=0,row=3)
    bm.grid(padx=3,pady=3,column=1,row=3)
    br.grid(padx=3,pady=3,column=2,row=3)
    def check():
        wins = [[tl,tm,tr],[ml,mm,mr],[bl,bm,br],[tm,mm,bm],[tl,ml,bl],[tr,mr,br],[tl,mm,br],[tr,mm,bl]]   
        global win
        for w in wins:
            if w[0]["text"] == w[1]["text"] == w[2]["text"]:
                if w[0]["text"] != " ":
                    winner = w[0]["text"]
                    win = True
                    messagebox.showinfo("WINNER","Game Over, {} wins the game".format(winner)) 
                    tl.config(state="disabled")
                    tm.config(state="disabled")
                    tr.config(state="disabled")
                    ml.config(state="disabled")
                    mm.config(state="disabled")
                    mr.config(state="disabled")
                    bl.config(state="disabled")
                    bm.config(state="disabled")
                    br.config(state="disabled")


def game():
    global win
    window = Toplevel(main,background="blue")
    font1 = f.Font(family="calibri",weight="bold",size=15)
    label = Label(window,background="blue",foreground="white",font=font1,width=20,text="O and X")
    label.grid(padx=10,pady=10,column=0,columnspan=3,row=0)
    create(window)
    

def tts():
    def convert():
        conversion = gTTS(entry.get(),lang="en")
        conversion.save("logtts.wav")
        os.system("logtts.wav")
    window = Toplevel(main,background="blue")
    font1 = f.Font(family="calibri",weight="bold",size=10)
    label = Label(window,background="blue",foreground="white",font=font1,width=20,text="CONVERT TEXT TO SPEECH")
    label.pack(padx=10,pady=10)
    entry = Entry(window)
    entry.pack(pady=10)
    button = Button(window,text="CONVERT",command=convert)
    button.pack(pady=10)
    

def clock():
    window = Toplevel(main,background="blue")
    font1 = f.Font(family="calibri",weight="bold",size=20)
    clock = Label(window,background="blue",foreground="white",font=font1,width=20)
    clock.pack(padx=10,pady=10)

    def timechange():
        time = strftime(" %H:%M:%S ")
        clock.config(text="TIME: " + time,)
        clock.after(1000,timechange)

    timechange()

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


details = {}

def clear():
    nameent.delete(0,END)
    ident.delete(0,END)
    ment.delete(0,END)
    eent.delete(0,END)
    sent.delete(0,END)

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

def click(event):
    window = Toplevel(main)
    index = entries.curselection()
    name = entries.get(index)
    id = details[name][0]
    maths = details[name][1]
    english = details[name][2]
    science = details[name][3]
    text = "Name: {} \nStudent ID: {} \nMaths score: {} \nEnglish score: {} \nScience score: {}".format(name,id,maths,english,science)
    label = Label(window,text=text)
    label.pack()       

main = Tk()

title = Label(main,text="STUDENT LOG")
title.grid(row=0,column=0,padx=10,pady=10,columnspan=5)

entries = Listbox(main,height=5,width=100)
entries.bind("<<ListboxSelect>>",click)
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
extras = Menu(menubar,tearoff=0)
extras.add_command(label="Game",command=game)
extras.add_command(label="Clock",command=clock)
extras.add_command(label="TTS",command=tts)
menubar.add_cascade(label="Extras",menu=extras)
main.config(menu=menubar)

main.mainloop()