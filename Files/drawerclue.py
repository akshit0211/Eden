from Tkinter import *
root7 = Tk()


Label(root7,text = 'You found some pictures in the drawer.',font = 'times 20').grid(row=0,column=0)
Label(root7,text = 'These Pictures probably belongs to the last',font = 'times 20').grid(row=1,column=0)
Label(root7,text = 'family who lived here.',font = 'times 20').grid(row=2,column=0)
Label(root7,text = 'Carefully look into picture 2',font = 'times 20').grid(row=3,column=0)
Label(root7,text = 'there must be some clue hidden in it.',font = 'times 20').grid(row=4,column=0)
Label(root7,text = 'Click to zoom it.',font = 'times 20').grid(row=5,column=0)
Label(root7,text = 'You found some pictures in the drawer.',font = 'times 20').grid(row=6,column=0)


def pic():
    from Tkinter import *
    root8 = Tk()

    Label(root8,text = 'Carefully look into the picture',font = 'times 20').grid(row=0,column=0)
    Label(root8,text = 'There is a door behind that candle',font = 'times 20').grid(row=1,column=0)
    Label(root8,text = 'but that door is hidden somewhere in the house',font = 'times 20').grid(row=3,column=0)
    Label(root8,text = 'We have to find it.',font = 'times 20').grid(row=4,column=0)

Button(root7,command=pic).grid(row=1,column=4)

root7.mainloop()
