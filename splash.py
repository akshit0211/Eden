from Tkinter import *
root=Tk()
root.title("Project")
root.geometry('500x400')
def sp():
    root.destroy()
lb=Label(root,text='Name - Akshit Sharma\n ER no.- 161B023\n Batch - B1(BX)\n Topic - Text Based Adventurous Game',font = 'times 20',compound='center')
lb.after(3000,sp)
lb.pack()
root.mainloop()
