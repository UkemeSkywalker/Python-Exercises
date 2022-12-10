import customtkinter
import tkinter
import sqlite3

global data
data = []

ids = []

app = customtkinter.CTk()


def submit():
    user_input = (textbox.get())
    status = False
    insert_todo(user_input, status)
    print("line 17", ids[-1])

    # c = ids[-1]
    res = customtkinter.CTkLabel(master=app, text=user_input, font=("Calibri Bold", 20), anchor="e")
    res.grid( row=ids, column=0, )
    # c+=1

    
    

    # res = customtkinter.CTkLabel(master=app, text=row, font=("Calibri Bold", 20))
    # res.grid( column=0)

def counter():
    qry = "SELECT oid FROM todo"
    db = sqlite3.connect("./todo.db")

    try:
        cur = db.cursor()
        cur.execute(qry)
        res = cur.fetchall()
        last_id = res[-1]
        return last_id
    except:
       print("get oid error..")
       db.rollback()
    db.close()

    
def display() :
    todos =  get_data()
    last_id = counter()
    _id = last_id[0]
    print("line 50", _id)
    for todo_data in todos :
        res = customtkinter.CTkLabel(master=app, text=todo_data, font=("Calibri Bold", 20), anchor="e")
        res.grid( row=_id, column=0, )
        print("line 33", _id)
        _id += 1
        ids.append(_id)
    print(todos)
    

        

def createDb() :
    db = sqlite3.connect("./todo.db")
    qry = '''CREATE TABLE todo(
        item TEXT (100),
        status BOOL
    )'''
    try:
        cur = db.cursor()
        cur.execute(qry)
        print('table created..')
    except :
        print("create table error..")
        db.rollback()
    db.close()
    

def insert_todo(item, status):
    db = sqlite3.connect("todo.db")
    qry = "INSERT INTO todo (item, status) VALUES(?,?);"
    try:
        cur = db.cursor()
        cur.execute(qry, (item, status))
        db.commit()
        print("New todo added...")
    except:
        print("insert todo error..")
        db.rollback()

    db.close()

def get_data():
    db = sqlite3.connect("todo.db")
    qry = "SELECT * FROM todo;"

    try:
        cur = db.cursor()
        cur.execute(qry)
        print("line 78")
        data = cur.fetchone()
        print(data)
        return data
        
        
    except:
        print("retrive data error...")
        db.rollback()
    db.close()

def delete():
    db = sqlite3.connect("todo.db")
    qry = "DELETE FROM todo WHERE status='0';"

    try:   
        cur = db.cursor()
        cur.execute(qry)
        db.commit()
        print("item deleted...")
    except:
        print("delete error..")
        db.rollback()
    db.close()


# createDb()
# insert_todo("Frontend Manipulation", True)
# get_data()

# data = get_data()
display()
# delete()

counter()


app.geometry("900x500")
app.minsize(450,500)
app.title("Todo App")


app.grid_rowconfigure(0, weight=0)
app.grid_columnconfigure((0, 0), weight=1)

header = customtkinter.CTkLabel(master=app, text="Skywalker Todo App", font=("Arial Bold", 28), justify="center", pady=20)
header.grid(row=0, column=0, columnspan=2)

textbox = customtkinter.CTkEntry(master=app, width=400, height=50)
textbox.grid(row=1, column=0, columnspan=2)

submit_btn = customtkinter.CTkButton(master=app, text="Add Todo", command=submit)
submit_btn.grid(row=2, column=0, pady=20, columnspan=2)

header2 = customtkinter.CTkLabel(master=app, text="Todo List", font=("Arial Bold", 20), justify="center")
header2.grid(row=3, column=0, columnspan=2)

# display()



app.mainloop()