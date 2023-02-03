from Tkinter import *
root12 =Tk()

Label(root12,text = 'There are some clothes',font = 'times 20').grid(row=0,column=0)
Label(root12,text = 'and look closer there must be something',font = 'times 20').grid(row=1,column=0)
Label(root12,text = 'which can help you to find some help.',font = 'times 20').grid(row=2,column=0)


def cell():
    from Tkinter import *
    root13 = Tk()
    Label(root13,text = 'Oh! look there is a cell phone',font = 'times 20').grid(row=0,column=0)
    Label(root13,text = 'you can use it to call someone',font = 'times 20').grid(row=1,column=0)
    Label(root13,text = 'to take you from here',font = 'times 20').grid(row=2,column=0)

Button(root12,command = cell).grid(row=3,column=0)

root12.mainloop()
