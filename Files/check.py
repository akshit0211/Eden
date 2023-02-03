from Tkinter import *
root4 = Toplevel()
d = PhotoImage(file = 'bookshelf.gif')
def bookshelfclue():
    root20 = Tk()
    Label(root20,text = 'Look some books are there...',font = 'times 20').grid(row=0,column=0)
    Label(root20,text = 'Maybe you will find some clues',font = 'times 20').grid(row=1,column=0)
    Label(root20,text = 'in these books',font = 'times 20').grid(row=2,column=0)
    def book():
        root21 = Toplevel()
        Label(root21,text = 'Nothing these books are',font = 'times 20').grid(row=0,column=0)
        Label(root21,text = 'normal books.',font = 'times 20').grid(row=1,column=0)
        Label(root21,text = 'Check other objects for clues..',font = 'times 20').grid(row=2,column=0)
    Button(root20,command = book).grid(row = 1,column = 4)
    root20.mainloop()
Button(root4,image = d,command = bookshelfclue).grid(row=0,column=5)
