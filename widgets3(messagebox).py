from tkinter import *
from tkinter import messagebox

main = Tk()

messagebox.showinfo("MESSAGE","MESSAGE")
messagebox.showwarning("WARNING","WARNING")
messagebox.showerror("ERROR","ERROR")
print(messagebox.askquestion("QUSETION","Yes or no?"))
print(messagebox.askokcancel("OK CANCEL","OK or cancel?"))
print(messagebox.askyesno("YESNO","Yes or no?"))
print(messagebox.askretrycancel("RETRY CANCEL","Retry or cancel?"))

main.mainloop()