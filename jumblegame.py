from tkinter import *
from tkinter import font as f
import time
import random

animals = {"easy": ["cat", "dog", "bat", "cow", "fox", "rat", "ant", "bee", "pig", "owl"],
    "medium": ["zebra", "horse", "sheep", "monkey", "rabbit", "donkey", "parrot", "panda", "goose", "giraffe"],
    "hard": ["chimpanzee", "rhinoceros", "hippopotamus", "alligator", "crocodile","kangaroo", "porcupine", "orangutan", "armadillo", "chameleon"]}

foods = {"easy": ["milk", "rice", "cake", "egg", "bread", "corn", "apple", "pear", "fish", "salt"],
    "medium": ["banana", "tomato", "cheese", "butter", "onions", "noodle", "pickle", "carrot", "biscuit", "cookie"],"hard": ["spaghetti", "lasagna", "croissant", "mayonnaise", "cappuccino","macaroni", "cucumber", "sauerkraut", "pineapple", "blueberries"]}

randoms = {"easy": ["book", "rain", "tree", "star", "pen", "ball", "cup", "sun", "bed", "door"],
    "medium":["planet", "castle", "rocket", "garden", "window", "tunnel", "bridge", "pirate", "desert", "island"],
    "hard": ["computer", "backpack", "umbrella", "elephant", "mountain","calendar", "airplane", "chocolate", "adventure", "binoculars"]}

allwords = {"animals": animals,"foods": foods,"randoms": randoms}

def jumble(word):
    jumbled = word
    while jumbled == word:
        jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def selectscreen():
    global score,count,word
    choosef.tkraise()   
    score = 0
    count = 0
    word = ""
    scorel.config(text="Score: {}/{}".format(score,count))

def endscreen():
    endingf.tkraise()
    title2 = Label(endingf,bg="blue",fg="white",text="Game over:\nYou scored: {}/{} ".format(score,count),font=font1)
    title2.grid(row=1,column=1,padx=30,pady=30)
    ng2 = Button(endingf,text="New game",font=font1,command=selectscreen)
    ng2.grid(row=2,column=1,padx=10,pady=10)
    
def start():
    global d,c,t
    d = varD.get()
    c = varC.get()
    t = varT.get()
    setup()

def setup():
    global score,count, d,c,t,word, tleft
    if count == 5:
        endscreen()
        return

    word = random.choice(allwords[c][d]).lower()
    tleft = int(t)
    timel.config(text="Timer:\n{}s".format(t))
    jumbled = jumble(word)
    juml.config(text=jumbled)
    guessf.tkraise()
    timing()
   
def timing():
    global count, tleft,current
    if tleft > 0:
        tleft -= 1
        timel.config(text="Timer:\n{}s".format(tleft))
        current = main.after(1000,timing)
    else:
        count += 1
        setup()

def guess():
    global word, score, count, current
    guessW = entry.get().lower()
    if guessW == word:
        score += 1
        entry.config(fg="lime")
    else:
        entry.config(fg="red")
    count += 1
    main.after_cancel(current)
    scorel.config(text="Score: {}/{}".format(score,count))
    def contin():
        entry.delete(0, END)
        entry.config(fg="black")
        setup()
    main.after(500,contin)

def reset():
    global score,count,word
    entry.delete(0,END)
    main.after_cancel(current)
    score = 0
    count = 0
    word = ""
    setup()

def skip():
    global score,count, d,c,word
    entry.delete(0,END)
    word = random.choice(allwords[c][d]).lower()
    jumbled = jumble(word)
    juml.config(text=jumbled)

main = Tk()
font1 = f.Font(family="calibri",weight="bold",size=18)
font2 = f.Font(family="calibri",weight="bold",size=10)

guessf = Frame(main,bg="green")
guessf.grid(row=1,column=1,sticky="nsew")

choosef = Frame(main,bg="light green")
choosef.grid(row=1,column=1,sticky="nsew")

startf = Frame(main,bg="blue")
startf.grid(row=1,column=1,sticky="nsew")

title = Label(startf,bg="blue",fg="white",text="Welcome to the jumbled words game: ",font=font1)
title.grid(row=1,column=1,padx=30,pady=30)

ng = Button(startf,text="New game",font=font1,command=selectscreen)
ng.grid(row=2,column=1,padx=10,pady=10)

title1 = Label(choosef,bg="light green",fg="red",text="Choose your settings: ",font=font1)
title1.grid(row=1,column=2,padx=10,pady=10)

cate = Label(choosef,bg="light green",fg="red",text="Category: ",font=font1)
cate.grid(row=2,column=1,padx=10,pady=10)

varC = StringVar()
varC.set("randoms")

radA = Radiobutton(choosef,text="Animals",value="animals",variable=varC,bg="light green",font=font2)
radA.grid(row=3,column=1)

radF = Radiobutton(choosef,text="Food",value="foods",variable=varC,bg="light green",font=font2)
radF.grid(row=4,column=1)

radR = Radiobutton(choosef,text="Random",value="randoms",variable=varC,bg="light green",font=font2)
radR.grid(row=5,column=1)

diff = Label(choosef,bg="light green",fg="red",text="Difficulty: ",font=font1)
diff.grid(row=2,column=2,padx=10,pady=10)

varD = StringVar()
varD.set("easy")

radE = Radiobutton(choosef,text="Easy",value="easy",variable=varD,bg="light green",font=font2)
radE.grid(row=3,column=2)

radM = Radiobutton(choosef,text="Medium",value="medium",variable=varD,bg="light green",font=font2)
radM.grid(row=4,column=2)

radH = Radiobutton(choosef,text="Hard",value="hard",variable=varD,bg="light green",font=font2)
radH.grid(row=5,column=2)

timer = Label(choosef,bg="light green",fg="red",text="Timer: ",font=font1)
timer.grid(row=2,column=3,padx=10,pady=10)

varT = StringVar()
varT.set("15")

rad10 = Radiobutton(choosef,text="10s",value="10",variable=varT,bg="light green",font=font2)
rad10.grid(row=3,column=3)

rad15 = Radiobutton(choosef,text="15s",value="15",variable=varT,bg="light green",font=font2)
rad15.grid(row=4,column=3)

rad20 = Radiobutton(choosef,text="20s",value="20",variable=varT,bg="light green",font=font2)
rad20.grid(row=5,column=3)

startb = Button(choosef,bg="light green",fg="white",text="Start",font=font2,command=start)
startb.grid(row=6,column=2)

title2 = Label(guessf,bg="green",fg="white",text="Unjumble the words: ",font=font1)
title2.grid(row=1,column=1,padx=10,pady=10)

juml = Label(guessf,bg="white",fg="blue",text="",font=font1,width=15)
juml.grid(row=2,column=1,padx=10,pady=10)

entry = Entry(guessf,font=font1)
entry.grid(row=3,column=1,padx=30,pady=10)

submit = Button(guessf,text="Submit",font=font1,bg="white",fg="blue",command=guess)
submit.grid(row=4,column=1,padx=30,pady=10)

resetbtn = Button(guessf,text="Reset",font=font1,bg="black",fg="red",command=reset)
resetbtn.grid(row=2,column=2,padx=30,pady=10)

skipbtn = Button(guessf,text="Skip",font=font1,bg="black",fg="lime",command=skip)
skipbtn.grid(row=3,column=2,padx=30,pady=10)

scorel = Label(guessf,bg="green",fg="white",text="Score: 0/0",font=font1)
scorel.grid(row=1,column=2,padx=10,pady=10)

timel = Label(guessf,bg="white",fg="blue",text="",font=font1,width=10)
timel.grid(row=4,column=2,padx=10,pady=10)

endingf = Frame(main,bg="blue")
endingf.grid(row=1,column=1,sticky="nsew")

startf.tkraise()
main.mainloop()