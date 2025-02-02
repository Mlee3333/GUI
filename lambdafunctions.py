'''from tkinter import *

def selection(choice):
    print(choice)

main = Tk()

buttonR = Button(main,text="Rock",command=lambda:selection("Rock"))
buttonP = Button(main,text="Paper",command=lambda:selection("Paper"))
buttonS = Button(main,text="Scissors",command=lambda:selection("Scissors"))
buttonR.grid(row=0,column=0,padx=10,pady=10)
buttonP.grid(row=0,column=1,padx=10,pady=10)
buttonS.grid(row=0,column=2,padx=10,pady=10)

main.mainloop()'''

def sum(a,b):
    return a+b

print(sum(2,9))
lambdasum = lambda a,b:a+b
result = lambdasum(8,1)
print(result)