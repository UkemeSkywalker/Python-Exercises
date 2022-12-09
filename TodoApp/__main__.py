import customtkinter
import tkinter
import sqlite3

global data
data = []



app = customtkinter.CTk()

def submit():
    user_input = (textbox.get())
    status = False
    insert_todo(user_input, status)
    print("line 17", row_id)
    
    res = customtkinter.CTkLabel(master=app, text=user_input, font=("Calibri Bold", 20), anchor="e")
    res.grid( row=row_id, column=0, )
    row_id += 1
    
    

    # res = customtkinter.CTkLabel(master=app, text=row, font=("Calibri Bold", 20))
    # res.grid( column=0)
def display() :

    global row_id
    row_id = 4
    
    todos =  get_data()
    
    for todo_data in todos :
        
        res = customtkinter.CTkLabel(master=app, text=todo_data[0], font=("Calibri Bold", 20), anchor="e")
        res.grid( row=row_id, column=0, )
        print("line 33", row_id)
        row_id += 1
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
    
## change files 


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
    qry = "SELECT * FROM todo"

    try:
        cur = db.cursor()
        cur.execute(qry)
        data = cur.fetchall()
        # print(data)
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