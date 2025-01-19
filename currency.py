from tkinter import *
import tkinter.font as f

def convert():
    dollar = entry.get()
    pound = float(dollar)*0.82
    lblans.config(text=str(dollar)+" dollars = "+str(pound)+" pounds")


main = Tk()
main.geometry("500x500")
font = f.Font(family="calibri",size=12,weight="bold",slant="italic")
frame1 = Frame(main)
frame1.pack()
label1 = Label(frame1,text="Convert dollar $ to pound £: ",font=("calibri",20,"bold"))
label1.grid(row=1,column=1)
frame2 = Frame(main)
frame2.pack(pady=50)
lblenter = Label(frame2,text="Enter currency in dollar $: ",font = font)
lblenter.grid(row=1,column=1)
entry = Entry(frame2)
entry.grid(row=1,column=2,padx=20)
frame3 = Frame(main)
frame3.pack()
lblans = Label(frame3, font = font)
lblans.grid(row=1,column=1)
bconvert = Button(frame3,text="Convert",command=convert, font= font)
bconvert.grid(row=2,column=1,pady=20)

main.mainloop()