import csv

class Storage:
    

    def write_data(data):
        f = open("./local_storage.csv", "a", newline='')
        d = csv.writer(f)
        d.writerow(data)

    def read_data():
        file = open("./local_storage.csv", "r", newline='')
        data = csv.reader(file)

        while True :
            try :
                row = next(data)
                print(row)
            except StopIteration:
                break
