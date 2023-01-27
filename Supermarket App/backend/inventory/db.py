import sqlite3

class Db :

    def connect_db(dbname) :
        print(dbname+ " connected")
        return sqlite3.connect("./db/"+dbname)
        

    ## create database if it doesnt exist
    def create_db(dbname) :
        try:       
            db = sqlite3.connect("./db/"+dbname)
            print(dbname + " created...")
            return db
        except :
            print("Db " +dbname+ " creation error")
    

    ## Create new table
    def create_table(dbname):
        db = Db.connect_db(dbname)

        try :
            cur = db.cursor()
            cur.execute('''
                CREATE TABLE item(
                    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT (20),
                    description TEXT (100),
                    image TEXT (20),
                    price INTEGER, 
                    tag TEXT (20),
                    category TEXT (30)
                );''')
            print( "table created..")
        except:
            print("Table already exist")
            db.rollback()
        db.close()


    # Insert item to table
    def insert_to_table(dbname, item):
        db = Db.connect_db(dbname)
        qry = "insert into item (name, description, image, price, tag, category) values(?,?,?,?,?,?);"
        try:
            cur=db.cursor()
            cur.execute(qry, item)
            db.commit()
            print ("one record added successfully")
        except:
            print ("error in operation")
            db.rollback()
        db.close()


    # Read all Items from db
    def read_all(dbname) :
        db = Db.connect_db(dbname)
        query = "select oid, name, description, image, price, tag, category from item;"
        try:
            cur = db.cursor()
            cur.execute(query)
            while True:
                data = cur.fetchone()
                if data == None :
                    break
                print("accessing db ...")
                print(data)
        except:
            print("read all from Db Error.. ")
            db.rollback()
        db.close()

    # Read one item
    def read_one(dbname, oid) :
        db = Db.connect_db(dbname)
        query = "select * from item where oid=?;"
        try:
            cur = db.cursor()
            cur.execute(query, (oid,))

            data = cur.fetchone()
            if data == None:
                print("item does not exist on db..")
            else: print(data)
        except:
            print("read one item error... ")
            db.rollback()
        db.close()

    # Read all Tags
    def read_all_tags(dbname):
        db = Db.connect_db(dbname)
        query = "select tag from item;"
        try:
            cur = db.cursor()
            cur.execute(query)
            data = cur.fetchall()
            for datas in data:
                print(datas)
        except:
            print("read all tags Error.. ")
            db.rollback()
        db.close()

    # Read all categories
    def read_all_categories(dbname):
        db = Db.connect_db(dbname)
        query = "select category from item;"
        try:
            cur = db.cursor()
            cur.execute(query)
            data = cur.fetchall()
            for datas in data:
                print(datas)
        except:
            print("read all categories Error.. ")
            db.rollback()
        db.close()


    # Edit One Item
    
    def edit_one_item(dbname, newname, description, image, price, tag, category, oid) :
        db = Db.connect_db(dbname)
        qry = "update item set name=?, description=?, image=?, price=?, tag=?, category=? where oid=?"

        try:
            cur = db.cursor()
            cur.execute(qry,(newname, description, image, price, tag, category, oid))
            db.commit()
            print("item update successful...")
        except:
            print("item update error..")
            db.rollback()
        db.close()
    
    # Edit one Tag
    
    def edit_tag(dbname,newtag, oldtag) :
        db = Db.connect_db(dbname)
        qry = "update item set tag=? where tag=?"

        try:
            cur = db.cursor()
            cur.execute(qry,(newtag, oldtag))
            db.commit()
            print("tag update successful...")
        except:
            print("item update error..")
            db.rollback()
        db.close()
  
    
    # Edit one Category
    
    def edit_category(dbname,new_category, old_category) :
        db = Db.connect_db(dbname)
        qry = "update item set category=? where category=?"

        try:
            cur = db.cursor()
            cur.execute(qry,(new_category, old_category))
            db.commit()
            print("Category update successful...")
        except:
            print("category update error..")
            db.rollback()
        db.close()

    
        
    # Delete Item from db
    def delete(dbname, oid):
        db = Db.connect_db(dbname)
        qry="DELETE from item where oid=?;"

        try:
            cur=db.cursor()
            cur.execute(qry, (oid,))
            db.commit()
            print("record deleted successfully")
        except:
            print("error in operation")
            db.rollback()   
        db.close()

    