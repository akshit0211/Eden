from Tkinter import *
root = Tk()

p = PhotoImage(file = 'letter.gif')
Button(root,image = p).grid(row=0,column=4)

q = PhotoImage(file = 'drawer.gif')
Button(root,image = q).grid(row = 0,column=8)

r = PhotoImage(file = 'lamp.gif')
Button(root,image = r).grid(row=0,column=12)


root.mainloop()
