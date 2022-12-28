import sqlite3

class Images:

    def store_image(image):
        try:
            with open(image, "rb") as f:
                blob_data = f.read()
            return blob_data
        except :
            print("get image error...")

    def get_image(image, filename):
        try:
            with open(image, "wb") as f:
                f.write(image)
            print("image stored as "+ filename)
        except:
            pass

    def connect_db(dbname) :
        print(dbname+ " connected")
        return sqlite3.connect("./"+dbname)
    
    def create_table(dbname):
        db = Images.connect_db(dbname)

        try :
            cur = db.cursor()
            cur.execute('''
                CREATE TABLE imageTable(
                    itemId INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT (20),
                    image BLOB      
                );''')
            print( "table created..")
        except:
            print("Table already exist")
            db.rollback()
        db.close()

    def image_to_db(dbname, name, image):
        images = Images.store_image(image)
        db = Images.connect_db(dbname)
        qry = "insert into imageTable (name, image) VALUES(?,?)"
        try:
            cur = db.cursor()
            cur.execute(qry, (name, images))
            db.commit()

            print("Image added to db..")
        except :
            db.rollback()
        db.close()

    def read_image(dbname, name):
        db = Images.connect_db(dbname)
        qry = "SELECT * FROM imageTable WHERE name=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, (name,))
            print("print...")
            data = cur.fetchall()
            for datas in data:
                print("Id = ", datas[0], "Name =", datas[1])
                name = datas[1]
                image = datas[2]
                print("Storing image to disk")
                path = "./store/"+name+".PNG"
                Images.get_image( image, path)
                print("Image storage successfull...")
        except:
            print("fetch image Error.. ")
            db.rollback()
        db.close()




db = "testimage.db"

# Images.create_table(db)

# Images.image_to_db(db,"Denim", "./3.PNG")

Images.read_image(db, "Denim")

        