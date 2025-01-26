from tkinter import *
import tkinter.font as f
import random
from tkinter import messagebox

score = [0,0]
total = 0
incorrect = 0
players = []
player = 0
rounds = 1
a=0
b=0
c=0

def roll():
    global total, score, rounds, player,a,b,c
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    total = a+b
    score[player] += total
    if a == b:
        total += c
    if total%2 == 0:
        score[player] += 10
    else:
        score[player] -= 5

    if score[player] < 0:
        score[player] = 0
    
    scoreL1.config(text="Score {}: {}".format(players[0],score[0]))
    scoreL2.config(text="Score {}: {}".format(players[1],score[1]))
    roundlbl.config(text="Round: {}".format(rounds))
    roll1.config(text="Roll1: {}".format(a))
    roll2.config(text="Roll2: {}".format(b))

    player += 1
    if player > 1:
        player = 0
        rounds += 1
    if rounds > 5 and player == 0:
        pl1 = score[0]
        pl2 = score[1]
        
        if pl1 == pl2:
            winner = "It's a draw!"
        elif pl1 < pl2:
            winner = "{} Wins!".format(players[1])
        else:
            winner = "{} Wins!".format(players[0])
    
        messagebox.showinfo("Game Over", winner)
        main.destroy()  

def login():
    players.append(entry1.get())
    entry1.delete(0,END)
    entry2.delete(0,END)
    if len(players) == 2:
        start()

def start():
    global player
    frame2.tkraise()


main = Tk()
main.geometry("350x350")
main.title("Dice game:")
font = f.Font(family="calibri",size=15,weight="bold")

frame2 = Frame(main,background="black",width=350,height=350)
frame2.grid(row=0,column=1,rowspan=2,padx=20)
title2 = Label(frame2,text="Dice game: ",font=font,background="black",foreground="white")
title2.grid(row=0,column=1,pady=20,padx=60)
btnRoll = Button(frame2,text="Roll",font=font,command=roll)
btnRoll.grid(row=1,column=1,padx=60,pady=20)

roundlbl = Label(frame2,text="Round: {}".format(rounds),font=font,background="black",foreground="magenta")
roundlbl.grid(row=2,column=1,pady=10)

roll1 = Label(frame2,text="Roll1: {}".format(a),font=font,background="black",foreground="cyan")
roll1.grid(row=4,column=1)
roll2 = Label(frame2,text="Roll2: {}".format(b),font=font,background="black",foreground="yellow")
roll2.grid(row=5,column=1)

scoreL1 = Label(frame2, text="Score P1: {}".format(score[0]))
scoreL1.config(background="black", foreground="white", font=font)
scoreL1.grid(row=6, column=1, padx=10)

scoreL2 = Label(frame2, text="Score P2: {}".format(score[1]))
scoreL2.config(background="black", foreground="white", font=font)
scoreL2.grid(row=7, column=1, padx=100)

frame1 = Frame(main)
frame1.grid(row=0,column=1,rowspan=2,columnspan=2,padx=20)
title = Label(frame1,text="Login: ",font=font)
title.grid(row=0,column=1,columnspan=2,pady=10)
username = Label(frame1, text = "Username: ",font=font)
username.grid(row=1,column=1,pady=10)
pword = Label(frame1, text = "Password: ",font=font)
pword.grid(row=2,column=1,pady=10)
entry1 = Entry(frame1,font=font)
entry1.grid(row=1,column=2,pady=10)
entry2 = Entry(frame1,font=font)
entry2.grid(row=2,column=2,pady=10)
btnSub = Button(frame1,text="Submit",font=font,command=login)
btnSub.grid(row=3,column=1,pady=70,columnspan=2)


main.mainloop()