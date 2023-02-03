from Tkinter import *
root25 = Tk()

Label(root25,text = 'It appears to be',font = 'times 20').grid(row=0,column=0)
Label(root25,text = 'a normal mirror....',font = 'times 20').grid(row=1,column=0)
Label(root25,text = 'Click on the mirror to look closer',font = 'times 20').grid(row=2,column=0)

def close():
    root26 = Tk()
    Label(root26,text = 'Oh!!! No',font = 'times 20').grid(row=0,column=0)
    Label(root26,text = 'Run Run Run',font = 'times 20').grid(row=1,column=0)
    Label(root26,text = 'Ghost is looking at you',font = 'times 20').grid(row=2,column=0)
Button(root25,command = close).grid(row=2,column = 4)
root25.mainloop()
