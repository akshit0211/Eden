from Tkinter import *
root9 = Tk()

Label(root9,text = 'Click to Go near the bed',font = 'times 20').grid(row=0,column=0)


def body():
    from Tkinter import *
    root10 = Tk ()

    Label(root10,text = 'Oh No!!!',font = 'times 20').grid(row=0,column=0)
    Label(root10,text = 'There is a body behind the bed',font = 'times 20').grid(row=1,column=0)
    Label(root10,text = 'Runaway! Runaway! Someone is murdered here.',font = 'times 20').grid(row=2,column=0)
Button(root9,command=body).grid(row=1,column=0)

root9.mainloop()
    
