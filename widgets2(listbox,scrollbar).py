from tkinter import *

def select():
    cs = listbox.curselection()
    print(cs)
    for i in cs:
        item = listbox.get(i)
        print(item)

    

main = Tk()

scrollbar = Scrollbar(main)


listbox = Listbox(main,selectmode=MULTIPLE,yscrollcommand=scrollbar.set)
listbox.insert(END,10,34,29,94,1000,206,102,343,4555,74648333,9901,4,77,8,82324,4324,42341)
listbox.pack(pady=30,padx=30,side=RIGHT)
scrollbar.pack(side=LEFT,fill=Y)

btnL = Button(main,text="Select",command=select)
btnL.pack()

scrollbar.config(command=listbox.yview)

main.mainloop()