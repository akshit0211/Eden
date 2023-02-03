from Tkinter import *
import sqlite3
import splash                                                     ####For importing Splash screen
root40 = Tk()
root40.title('Player Information') 
l = sqlite3.Connection('db')                                      ####For Connecting Database
cur = l.cursor()
cur.execute("create table if not exists ent(name varchar(20), age number(10))")
Label(root40,text='Enter Your Details',font = 'times 15',fg = 'red',bg = 'black').grid(row=0,column=0)
Label(root40,text = "Enter Name",font = 'times 15').grid(row=1,column=0)
e1 = Entry(root40)
e1.grid(row = 1,column = 1)
Label(root40,text = "Age",font = 'times 15').grid(row= 2,column=0)
Label(root40,text = 'Press Insert First',font = 'times 15',fg = 'red',bg = 'black').grid(row=3,column=0)
e2 = Entry(root40)
e2.grid(row=2,column=1)

def fun40():
    b = [(e1.get(),e2.get())]
    cur.executemany("insert into ent values(?,?)",b)
    cur.fetchall()
    l.commit()
Button(root40,text = "Insert",command= fun40).grid(row=2,column=2)
Button(root40,text = "Start the game",command = lambda:root40.destroy()).grid(row=3,column=2)
root40.mainloop()


root = Tk()                                                                     ####Game Start
a = PhotoImage(file = 'house.gif')                                              ####House image
Label(root,text = "Welcome To The Eden",font = 'times 25 bold',fg = 'red',bg = 'black').grid(row=1,column=0,columnspan=4)
def fun():
    root1 = Toplevel()
    root1.title("Rooms")
    x = PhotoImage(file = 'door1.gif')                                                        ####Door Image 1
    def fun1():
        root2 = Toplevel()
        root2.title("Room1 Objects")
        p = PhotoImage(file = 'letter.gif')                                                   #####LetterClue Image
        def letterclue():
            root5 = Tk()

            Label(root5,text = 'It is an very old letter.',font = 'times 15 ').grid(row = 0,column = 0)
            Label(root5,text = 'Words are not clearly visible,',font = 'times 15 ').grid(row = 1,column = 0)
            Label(root5,text = 'but there is something written',font = 'times 15 ').grid(row = 2,column = 0)
            Label(root5,text = 'on this letter -> Appears to be.',font = 'times 15 ').grid(row = 3,column = 0)
            Label(root5,text = 'Dear sir,',font = 'times 20',fg = 'dark green').grid(row = 4,column = 0)
            Label(root5,text = 'I am the last one who knows',font = 'times 20',fg = 'dark green').grid(row = 5,column = 0)
            Label(root5,text = 'where that object is hidden',font = 'times 20',fg = 'dark green').grid(row = 6,column = 0)
            Label(root5,text = 'but you need a passcode to enter.',font = 'times 20',fg = 'dark green').grid(row = 7,column = 0)
            Label(root5,text = '(0,0,1,3,1,1,1,1)',font = 'times 15').grid(row = 8,column = 0)
            Label(root5,text = 'There are 8 numbers arrange',font = 'times 15').grid(row = 9,column = 0)
            Label(root5,text = '2 numbers together and add them',font = 'times 15').grid(row = 10,column = 0)
            Label(root5,text = 'starting from left and divide them with 2.',font = 'times 15').grid(row = 11,column = 0)
            Label(root5,text = 'You will get your passcode.',font = 'times 15').grid(row = 12,column = 0)


            def hint():
    
                root6 = Toplevel()
                Label(root6,text = '(0,0) (1,3) (1,1) (1,1)',font = 'times 15',fg = 'dark green').grid(row = 0,column = 0)
                Label(root6,text = '(0+0) = 0/2 = 0',font = 'times 15',fg = 'dark green').grid(row = 1,column = 0)
                Label(root6,text = '(1+3) = 4/2 = 2',font = 'times 15',fg = 'dark green').grid(row = 2,column = 0)
                Label(root6,text = '(1+1) = 2/2 = 1',font = 'times 15',fg = 'dark green').grid(row = 3,column = 0)
                Label(root6,text = '(1+1) = 2/2 = 1',font = 'times 15',fg = 'dark green').grid(row = 4,column = 0)
                Label(root6,text = 'So the Passcode is : 0211',font = 'times 15',fg = 'dark green').grid(row = 6,column = 0)
    
            Button(root5,text = "HINT",width = 10,command = hint).grid(row = 5,column = 2)
            root5.mainloop()
        Button(root2,image = p,command = letterclue).grid(row=0,column=5)
        q = PhotoImage(file = 'drawer.gif')                                                     #####DrawerClue Image
        def drawerclue():
            root7 = Toplevel()
            Label(root7,text = 'You found some pictures in the drawer.',font = 'times 15',fg = 'dark green').grid(row=0,column=0)
            Label(root7,text = 'These Pictures probably belongs to the last',font = 'times 15',fg = 'dark green').grid(row=1,column=0)
            Label(root7,text = 'family who lived here.',font = 'times 15',fg = 'dark green').grid(row=2,column=0)
            Label(root7,text = 'Carefully look into picture 2',font = 'times 15',fg = 'dark green').grid(row=3,column=0)
            Label(root7,text = 'there must be some clue hidden in it.',font = 'times 15',fg = 'dark green').grid(row=4,column=0)
            Label(root7,text = 'Click to zoom it.',font = 'times 15',fg = 'dark green').grid(row=5,column=0)
            s = PhotoImage(file = 'candle.gif')
            e = PhotoImage(file = 'candle3.gif')
            def pic():
                root8 = Toplevel()
                Label(root8,text = 'Carefully look into the picture',font = 'times 15').grid(row=0,column=0)
                Label(root8,text = 'There is a door behind that candle',font = 'times 15').grid(row=1,column=0)
                Label(root8,text = 'but that door is hidden somewhere in the house',font = 'times 15').grid(row=3,column=0)
                Label(root8,text = 'We have to find it.',font = 'times 15').grid(row=4,column=0)
                Label(root8,image = e).grid(row = 5,column = 5)
            Button(root7,image = s,command=pic).grid(row=5,column=4)
            root7.mainloop()
        Button(root2,image = q,command = drawerclue).grid(row = 0,column=10)
        r = PhotoImage(file = 'tv.gif')                                                          ####Tv clue Image
        def tvclue():
            root15 = Toplevel()
            Label(root15,text = 'Look closer there is something',font = 'times 20').grid(row=0,column=0)
            Label(root15,text = 'running on these tv screens.',font = 'times 20').grid(row=1,column=0)
            Label(root15,text = 'These are CCTV tapes!!!',font = 'times 20').grid(row=2,column=0)
            Label(root15,text = 'Move these tapes back to',font = 'times 20').grid(row=3,column=0)
            Label(root15,text = 'find some clues.',font = 'times 20').grid(row=4,column=0)
            f = PhotoImage(file = 'candle3.gif')
            def back():
                root16 = Toplevel()
                Label(root16,text = 'Oh!! No',font = 'times 20').grid(row=0,column=0)
                Label(root16,text = 'that is the same room',font = 'times 20').grid(row=1,column=0)
                Label(root16,text = 'Now it is clear',font = 'times 20').grid(row=2,column=0)
                Label(root16,text = 'that room is same as the one in',font = 'times 20').grid(row=3,column=0)
                Label(root16,text = 'the picture of that candle.',font = 'times 20').grid(row=4,column=0)
                Label(root16,text = 'You must find this room,',font = 'times 20').grid(row=5,column=0)
                Label(root16,text = 'object must be hidden somewhere in the room.',font = 'times 20').grid(row=6,column=0)
                Label(root16,text = 'Now you have the passcode to',font = 'times 20').grid(row=7,column=0)
                Label(root16,text = 'enter into this room find this room...',font = 'times 20').grid(row=8,column=0)
                Label(root16,image = f).grid(row = 5,column = 5)
            Button(root15,text = 'Press to Back tapes',width = 15,command = back).grid(row = 4,column = 4)
            root15.mainloop()
        Button(root2,image = r,command = tvclue).grid(row=0,column=15)
        Label(root2,text = 'You Entered into the Room....',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=10,column=5,columnspan=15)
        Label(root2,text = 'There are some Objects in the Room',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=11,column=5,columnspan=15)
        Label(root2,text = 'Which will give you some clues to find that mysterious powerful Apple of Eden... ',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=12,column=5,columnspan=15)
        Label(root2,text = 'Check every objects to find some clues..',font = 'times 18 ',fg = 'red',bg = 'black').grid(row=13,column=5,columnspan=15)
        root2.mainloop()
    Button(root1,text='1',image = x,command=fun1).grid(row=0,column=5,columnspan=5)
    Label(root1,text = 'Room 1',font = 'times 15 bold',fg = 'red',bg = 'orange').grid(row=1,column=7)
    y = PhotoImage(file = 'door2.gif')                                                        ####Door Image 2
    def fun2():
        root3 = Toplevel()
        root3.title("Room2 Objects")
        s = PhotoImage(file = 'bed.gif')                                                     ####Bed clue Image
        def bedclue():
            root9 = Tk()
            Label(root9,text = 'Click to Go near the bed',font = 'times 20').grid(row=0,column=0)


            def body():
                root10 = Tk ()

                Label(root10,text = 'Oh No!!!',font = 'times 20').grid(row=0,column=0)
                Label(root10,text = 'There is a body behind the bed',font = 'times 20').grid(row=1,column=0)
                Label(root10,text = 'Runaway! Runaway! Someone is murdered here.',font = 'times 20').grid(row=2,column=0)
            Button(root9,command=body).grid(row=1,column=0)
            root9.mainloop()
        Button(root3,image=s,command = bedclue).grid(row=0,column=5)
        t = PhotoImage(file = 'almirah.gif')                                                ####Almirah clue image
        def almirahclue():
            root11 = Tk()
            Label(root11,text = 'There are some clothes here',font = 'times 20').grid(row=0,column=0)
            Label(root11,text = 'Check for some clues',font = 'times 20').grid(row=1,column=0)
            Label(root11,text = 'If you are not able to find',font = 'times 20').grid(row=2,column=0)
            Label(root11,text = 'any clue then proceed to next object',font = 'times 20').grid(row=3,column=0)
            root11.mainloop()
        Button(root3,image=t,command = almirahclue).grid(row=0,column=10)
        u = PhotoImage(file = 'trunk.gif')                                                  ####trunk clue image
        def trunkclue():
            root12 =Tk()
            Label(root12,text = 'There are some clothes',font = 'times 20').grid(row=0,column=0)
            Label(root12,text = 'and look closer there must be something',font = 'times 20').grid(row=1,column=0)
            Label(root12,text = 'which can help you to find some help.',font = 'times 20').grid(row=2,column=0)


            def cell():
                root13 = Tk()
                Label(root13,text = 'Oh! look there is a cell phone',font = 'times 20').grid(row=0,column=0)
                Label(root13,text = 'you can use it to call someone',font = 'times 20').grid(row=1,column=0)
                Label(root13,text = 'to take you from here',font = 'times 20').grid(row=2,column=0)

            Button(root12,command = cell).grid(row=3,column=0)
            root12.mainloop()
        Button(root3,image=u,command = trunkclue).grid(row=0,column=15)
        Label(root3,text = 'You Entered into the Room....',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=10,column=5,columnspan=15)
        Label(root3,text = 'There are some Objects in the Room',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=11,column=5,columnspan=15)
        Label(root3,text = 'Which will give you some clues to find that mysterious powerful Apple of Eden... ',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=12,column=5,columnspan=15)
        Label(root3,text = 'Check every objects to find some clues..',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=13,column=5,columnspan=15)
        root3.mainloop()
    Button(root1,image = y,command=fun2).grid(row=0,column=10,columnspan=5)
    Label(root1,text = 'Room 2',font = 'times 15 bold',fg = 'red',bg = 'orange').grid(row=1,column=12)
    z = PhotoImage(file = 'door3.gif')                                                        ####Door3 Image
    def fun3():
        root4 = Toplevel()
        root4.title("Room3 Objects")
        d = PhotoImage(file = 'bookshelf.gif')                                               ####Bookshelf clue Image
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
        e = PhotoImage(file = 'mirror.gif')                                                    ####Mirror clue Image
        def mirrorclue():
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
        Button(root4,image = e,command = mirrorclue).grid(row=0,column=10)
        f = PhotoImage(file = 'lamp.gif')                                                      ####Lamp clue Image
        def lampclue():
            root35 = Toplevel()
            Label(root35,text = 'It is so dark in here',font = 'times 20').grid(row=0,column=0)
            Label(root35,text = 'Use this lamp to see...',font = 'times 20').grid(row=1,column=0)
            Label(root35,text = 'There it is, that is the same',font = 'times 20').grid(row=2,column=0)
            Label(root35,text = 'Mysterious Room.',font = 'times 20').grid(row=3,column=0)
            Label(root35,text = 'You found it....',font = 'times 20').grid(row=4,column=0)
            Label(root35,text = 'Now click on the image to open this room...',font = 'times 20').grid(row=5,column=0)
            j = PhotoImage(file = 'candle.gif')                                                ####candle clue Image
            def candle():
                root36 = Toplevel()
                Label(root36,text = 'Now you have entered into the room',font = 'times 20').grid(row=0,column=0)
                Label(root36,text = 'To open this door...',font = 'times 20').grid(row=1,column=0)
                Label(root36,text = 'You need a passcode',font = 'times 20').grid(row=2,column=0)
                Label(root36,text = 'Enter the passcode in proper order to open this door',font = 'times 20').grid(row=3,column=0)
                k = PhotoImage(file = 'mdoor.gif')                                            ####Passcode door image
                def mydoor(): 
                    root38 = Toplevel()
                    cur.execute('select * from ent')
                    i = cur.fetchall()
                    u = PhotoImage(file = 'eden.gif')                                         #### mysterious image
                    Label(root38,image = u).grid(row = 0,column = 0,columnspan=4)
                    Label(root38,text = 'You Found it!!!! You are a Winner',font = 'times 15 bold',fg = 'red',bg = 'black').grid(row=1,column=0)
                    Label(root38,text = i).grid(row=2,column=0)
                    root38.mainloop()
                Button(root36,image = k,command = mydoor).grid(row =5,column=0)
                root36.mainloop()
            Button(root35,image = j,command = candle).grid(row=6,column=0)
            root35.mainloop()
        Button(root4,image = f,command = lampclue).grid(row=0,column=15)
        Label(root4,text = 'You Entered into the Room....',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=10,column=5,columnspan=15)
        Label(root4,text = 'There are some Objects in the Room',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=11,column=5,columnspan=15)
        Label(root4,text = 'Which will give you some clues to find that mysterious powerful Apple of Eden... ',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=12,column=5,columnspan=15)
        Label(root4,text = 'Check every objects to find some clues..',font = 'times 15 ',fg = 'red',bg = 'black').grid(row=13,column=5,columnspan=15)
        root4.mainloop()
    Button(root1,image = z,command=fun3).grid(row=0,column=15,columnspan=5)
    Label(root1,text = 'Room 3',font = 'times 15 bold',fg = 'red',bg = 'orange').grid(row=1,column=17)
    Label(root1,text = 'Which Room Do You Wanna Enter?',font = 'times 20 bold').grid(row=15,column=10,columnspan=5)
    root1.mainloop()

Button(root,image = a,command=fun).grid(row=2,column=0)
Label(root,text="The World is about to end. Can you save it?",font = 'times 15 bold').grid(row=20,column=0)
Label(root,text="It can only be saved by an object called Apple of Eden...",font = 'times 15 bold').grid(row=21,column=0)
Label(root,text="Which is hidden somewhere in this House",font = 'times 15 bold').grid(row=22,column=0)
Label(root,text="That object is very powerful.Can you find it?",font = 'times 15 bold').grid(row=23,column=0)




root.mainloop()
