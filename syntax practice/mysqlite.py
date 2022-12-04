import sqlite3

db = sqlite3.connect('test.db')

try: 
    cur = db.cursor()
    cur.execute('''
        CREATE TABLE student (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT (20) NOT NULL,
            age INTEGER,
            mark REAL);''')
    db.commit()
    print("Table created...")
except :
    print("Create Table Error")
    db.rollback()

db.close()


db = sqlite3.connect('test.db')
try:
    qry = "insert into student (name, age, mark) values('Ukeme', 20, 20.1)"
    cur = db.cursor()
    cur.execute(qry)
    db.commit()
    print("insert query executed...")
except :
    print("insert error..")
    db.rollback()

db.close()


db=sqlite3.connect('test.db')
sql="SELECT * from student;"
cur=db.cursor()
cur.execute(sql)
while True:
    record=cur.fetchone()
    if record==None:
        break
    print (record)
db.close()