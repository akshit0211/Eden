from Tkinter import *
root15 = Tk()

Label(root15,text = 'Look closer there is something',font = 'times 20').grid(row=0,column=0)
Label(root15,text = 'running on these tv screens.',font = 'times 20').grid(row=1,column=0)
Label(root15,text = 'These are CCTV tapes!!!',font = 'times 20').grid(row=2,column=0)
Label(root15,text = 'Move these tapes back to',font = 'times 20').grid(row=3,column=0)
Label(root15,text = 'find some clues.',font = 'times 20').grid(row=4,column=0)


def back():
    from Tkinter import *
    root16 = Tk()

    Label(root16,text = 'Oh!! No',font = 'times 20').grid(row=0,column=0)
    Label(root16,text = 'that is the same room',font = 'times 20').grid(row=1,column=0)
    Label(root16,text = 'Now it is clear',font = 'times 20').grid(row=2,column=0)
    Label(root16,text = 'that room is same as the one in',font = 'times 20').grid(row=3,column=0)
    Label(root16,text = 'the picture of that candle.',font = 'times 20').grid(row=4,column=0)
    Label(root16,text = 'You must find this room,',font = 'times 20').grid(row=5,column=0)
    Label(root16,text = 'object must be hidden somewhere in the room.',font = 'times 20').grid(row=6,column=0)
    Label(root16,text = 'Now you have the passcode to',font = 'times 20').grid(row=7,column=0)
    Label(root16,text = 'enter into this room find this room...',font = 'times 20').grid(row=8,column=0)
Button(root15,command = back).grid(row = 4,column = 4)
root15.mainloop()

    
