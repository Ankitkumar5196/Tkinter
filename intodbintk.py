import sqlite3
db=sqlite3.connect('Ankit.db')
cr=db.cursor()
cr.execute("create table login(username text,password integer)")
db.commit()
db.close()