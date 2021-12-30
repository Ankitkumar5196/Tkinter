import sqlite3
db=sqlite3.connect('Ankit.db')
x=input("enter name:")
y=input("Enter password:")

cr=db.cursor()
cr.execute("insert into login(username,password) values('"+x+"','"+y+"')")
db.commit()
db.close()