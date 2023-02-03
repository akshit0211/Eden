from Tkinter import *
root5 = Tk()

Label(root5,text = 'It is an very old letter.',font = 'times 20 bold').grid(row = 0,column = 0)
Label(root5,text = 'Words are not clearly visible,',font = 'times 20 bold').grid(row = 1,column = 0)
Label(root5,text = 'but there is something written',font = 'times 20 bold').grid(row = 2,column = 0)
Label(root5,text = 'on this letter -> Appears to be.',font = 'times 20 bold').grid(row = 3,column = 0)
Label(root5,text = 'Dear sir,',font = 'times 20 bold').grid(row = 4,column = 0)
Label(root5,text = 'I am the last one who knows',font = 'times 20 bold').grid(row = 5,column = 0)
Label(root5,text = 'where that object is hidden',font = 'times 20 bold').grid(row = 6,column = 0)
Label(root5,text = 'but you need a passcode to enter.',font = 'times 20 bold').grid(row = 7,column = 0)
Label(root5,text = '(0,0,1,3,1,1,1,1)',font = 'times 20 bold').grid(row = 8,column = 0)
Label(root5,text = 'There are 8 numbers arrange',font = 'times 20 bold').grid(row = 9,column = 0)
Label(root5,text = '2 numbers together and add them',font = 'times 20 bold').grid(row = 10,column = 0)
Label(root5,text = 'starting from left and divide them with 2.',font = 'times 20 bold').grid(row = 11,column = 0)
Label(root5,text = 'You will get your passcode.',font = 'times 20 bold').grid(row = 12,column = 0)


def hint():
    from Tkinter import *
    root6 = Toplevel()
    Label(root6,text = '(0,0) (1,3) (1,1) (1,1)',font = 'times 20').grid(row = 0,column = 0)
    Label(root6,text = '(0+0) = 0/2 = 0',font = 'times 20').grid(row = 1,column = 0)
    Label(root6,text = '(1+3) = 4/2 = 2',font = 'times 20').grid(row = 2,column = 0)
    Label(root6,text = '(1+1) = 2/2 = 1',font = 'times 20').grid(row = 3,column = 0)
    Label(root6,text = '(1+1) = 2/2 = 1',font = 'times 20').grid(row = 4,column = 0)
    Label(root6,text = 'So the Passcode is : 0211',font = 'times 20').grid(row = 6,column = 0)
    
Button(root5,text = "HINT",command = hint).grid(row = 5,column = 2)


root5.mainloop()



