from tkinter import *

main = Tk()

menubar = Menu(main)
file = Menu(menubar,tearoff=0)
file.add_command(label="Save",command=None)
file.add_command(label="New File",command=None)
file.add_command(label="Open",command=None)
file.add_separator()
file.add_command(label="Close",command=None)

edit = Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_command(label="Find")


menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="Edit",menu=edit)
main.config(menu=menubar)

main.mainloop()