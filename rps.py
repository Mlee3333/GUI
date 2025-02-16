from tkinter import *
from tkinter import messagebox
import random
import tkinter.font as f

scoreP = 0
scoreC = 0

def selectionC():
    choice = random.randint(1,3)
    if choice == 1:
        choice = "Rock"
    elif choice == 2:
        choice = "Paper"
    else:
        choice = "Scissors"
    return choice

def selection(choice):
    global scoreC,scoreP
    choiceC = selectionC()
    choiceP = choice
    if choiceP == choiceC:
        lblRes.config(text="TIE!")
        messagebox.showinfo("Tie!","You selected {} , Computer selected {}".format(choiceP,choiceC))
    elif choiceP == "Rock":
        if choiceC == "Paper":
            lblRes.config(text="LOSS!")
            messagebox.showinfo("You Lose!","You selected {} , Computer selected {}".format(choiceP,choiceC))
            scoreC += 1
        elif choiceC == "Scissors":
            lblRes.config(text="WIN!")
            messagebox.showinfo("You Win!","You selected {} , Computer selected {}".format(choiceP,choiceC))
            scoreP += 1
    elif choiceP == "Paper":
        if choiceC == "Scissors":
            lblRes.config(text="LOSS!")
            messagebox.showinfo("You Lose!","You selected {} , Computer selected {}".format(choiceP,choiceC))
            scoreC += 1
        elif choiceC == "Rock":
            lblRes.config(text="WIN!")
            messagebox.showinfo("You Win!","You selected {} , Computer selected {}".format(choiceP,choiceC))
            scoreP += 1
    elif choiceP == "Scissors":
        if choiceC == "Rock":
            lblRes.config(text="LOSS!")
            messagebox.showinfo("You Lose!","You selected {} , Computer selected {}".format(choiceP,choiceC))
            scoreC += 1
        elif choiceC == "Paper":
            lblRes.config(text="WIN!")
            messagebox.showinfo("You Win!","You selected {} , Computer selected {}".format(choiceP,choiceC))
            scoreP += 1
    
    lblYSC.config(text="Player score: {}".format(scoreP))
    lblCSC.config(text="Computer score: {}".format(scoreC))

main = Tk()

main.title("Rock Paper Scissors")
fontR = f.Font(family="calibri",size=16,weight="bold")
fontT = f.Font(family="calibri",size=20,weight="bold")

buttonR = Button(main,text="Rock",command=lambda:selection("Rock"),font=fontR,foreground="white",background="red")
buttonP = Button(main,text="Paper",command=lambda:selection("Paper"),font=fontR,foreground="white",background="green")
buttonS = Button(main,text="Scissors",command=lambda:selection("Scissors"),font=fontR,foreground="white",background="blue")
buttonR.grid(row=2,column=1,padx=20,pady=10)
buttonP.grid(row=2,column=2,padx=20,pady=10)
buttonS.grid(row=2,column=3,padx=20,pady=10)

lblT = Label(main,text="Rock Paper Scissors: ",font=fontT,foreground="dark blue")
lblT.grid(row=0,column=0,columnspan=4)

lblRes = Label(main,font=fontR,foreground="dark green")
lblRes.grid(row=1,column=1,columnspan=2,padx=30)

lblOpt = Label(main,font=fontR,text="Options:", foreground="purple")
lblOpt.grid(row=2,column=0,padx=10)

lblTSC = Label(main,font=fontR,text="Scores:", foreground="grey")
lblTSC.grid(row=3,column=0,padx=10)

lblYSC = Label(main,font=fontR,text="Player score: 0", foreground="grey")
lblYSC.grid(row=3,column=1,padx=10,columnspan=3)
lblCSC = Label(main,font=fontR,text="Computer score: 0", foreground="grey")
lblCSC.grid(row=4,column=1,padx=10,columnspan=3)

main.mainloop()