from Tkinter import *
root = Tk()

x = PhotoImage(file = 'door1.gif')
Button(root,text='1',image = x).grid(row=0,column=5)
y = PhotoImage(file = 'door2.gif')
Button(root,image = y).grid(row=0,column=10)
z = PhotoImage(file = 'door3.gif')
Button(root,image = z).grid(row=0,column=15)

def Room():
    room = ""
    while room != "1" and room != "2":
          room = input("Which room will you choose? (1 or 2): ")
    return room
def checkroom(chosenroom):
    print("You entered into the room...")
    print("there are some objects which will give you clue to find that mysterious powerful Apple of Eden...")
    print("check Every object to find some clue...")
    print()
    

Label(root,text = 'Which room do u wanna enter?').grid(row = 5,column = 5)
root.mainloop()
