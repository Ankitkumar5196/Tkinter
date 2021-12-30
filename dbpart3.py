import sqlite3
db=sqlite3.connect('Ankit.db')
x="Abhinav"
y="1236"
cr=db.cursor()
cr.execute("insert into login(username,password) values('"+x+"','"+y+"')")
db.commit()
db.close()