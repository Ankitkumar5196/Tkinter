import sqlite3
db=sqlite3.connect('Ankit.db')
cr=db.cursor()
cr.execute("insert into login(username,password) values('ankit',1223)")
db.commit()
db.close()