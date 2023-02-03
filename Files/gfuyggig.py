root40 = Tk()
l = sqlite3.Connection('db')
cur = l.cursor()
cur.execute("create table if not exists ent(name varchar(20), age number(10))")
Label(root40,text = "Enter Name").grid(row=0,column=0)
e1 = Entry(root40)
e1.grid(row = 0,column = 1)
Label(root40,text = "age").grid(row= 1,column=0)
e2 = Entry(root40)
e2.grid(row=1,column=1)

def fun40():
    b = [(e1.get(),e2.get())]
    cur.executemany("insert into ent values(?,?)",b)
    cur.fetchall()
    l.commit()
Button(root40,text = "insert",command= fun40).grid(row=2,column=2)
Button(root40,text = "submit",command=fun44 ).grid(row=3,column=2)
root40.mainloop()

