from tkinter import *
import tkinter.font as f
import random

score = 0
ans = 0
incorrect = 0

def question():
    global ans
    a = random.randint(0,12)
    b = random.randint(0,12)
    lblQ.config(text=str(a)+" x "+str(b)+" =")
    ans = a*b

def check():
    global score, ans,incorrect
    ent = entAns.get()
    if int(ent) == int(ans):
        lblW.config(text="CORRECT!")
        entAns.delete(0,END)
        score = score + 1
        scoreL2.config(text=score)
        end()
    else:
        lblW.config(text="INCORRECT")
        entAns.delete(0,END)
        incorrect = incorrect + 1
        end()

def end():
    global score,incorrect
    if score >= 10:
        main.destroy()
        print("Well done!")
    elif incorrect >= 5:
        main.destroy()
        print("Game over!")
    else:
        question()


main = Tk()
main.geometry("400x400")
main.title("Multiplication quiz:")
font = f.Font(family="calibri",size=12,)

title = Label(main,text="Multiplication quiz: ",font=font)
title.grid(row=1,column=1,columnspan=2,pady=30)
scoreL1 = Label(main,text="Score: ",font=font)
scoreL1.grid(row=5,column=1)
scoreL2 = Label(main,text=score,font=font)
scoreL2.grid(row=5,column=2)
lblQ = Label(main,font=font)
lblQ.grid(row=2,column=1,padx=15)
entAns = Entry(main,font=font)
entAns.grid(row=2,column=2)
question()
btnSub = Button(main,text="Submit",font=font,command=check)
btnSub.grid(row=3,column=1,pady=30,columnspan=2)
lblW = Label(main,font=font)
lblW.grid(row=4,column=1,columnspan=2)

main.mainloop()