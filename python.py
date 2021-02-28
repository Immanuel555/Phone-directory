import mysql.connector as  mys
from art import tprint
tprint('P H O N E \nD I R E C T O R Y ', font = 'slant')

mydb = mys.connect(host = "localhost",user = "root")
csr = mydb.cursor()
db_name = 'PHONE_DIRECTORY'

def show_dbs():
    csr.execute('SHOW DATABASES')
    return [x[0] for x in csr.fetchall()]

def db_existance(db_name):
    if db_name.lower() in show_dbs():
            return True
    return False

#Create DBs
def create_db():
    global mydb, csr
    if not db_existance(db_name):
        csr.execute(f"CREATE DATABASE {db_name}")
        csr.execute(f"USE {db_name}")
        csr.execute("CREATE TABLE CONTACTS(SNO INT  AUTO_INCREMENT, NAME VARCHAR(20) UNIQUE NOT NULL, PHONE_NUMBER INT, ADDRESS VARCHAR(50) )")
    
    mydb = mys.connect(host="localhost",user="root", database = db_name)
    csr = mydb.cursor()

#INSERTION
def insert():
    csr.execute(f"USE {db_name}")
    n = int(input("ENTER NUMBER OF CONTACTS TO BE INSERTED:"))
    for i in range(n):
        name = input("ENTER NAME OF THE CONTACT:")
        no = int(input("ENTER PHONE NUMBER:"))
        add = input("ENTER ADDRESS:")
        csr.execute(f"INSERT INTO CONTACTS (NAME, PHONE_NUMBER, ADDRESS) VALUES ('{name}',{no},'{add}')")
        mydb.commit()
        print("CONTACTS INSERTED SUCCESSFULLY")

#SEARCHING CONTACT IN TABLE
def search():
    name = input("ENTER NAME OF CONTACTS TO BE SEARCHED:")
    csr.execute(f'SELECT * FROM CONTACTS WHERE NAME LIKE "%{name}%"')
    data = csr.fetchall()
    for i in data:
        if i[1]==name:
            print("CONTACT SUCESSFULLY FOUND! \nContact:\n")
            print(f"Name: {i[1]} \nNumber: {i[2]} \nAddress: {i[3]}")
            return
        

#UPDATING A CONTACT IN TABLE
def update():
    name = input("ENTER NAME OF THE CONTACT TO BE CHANGED:")
    name1=input("NAME:")
    number = int(input("NUMBER:"))
    add = input("ADDRESS:")
    csr.execute(f'SELECT * FROM CONTACTS WHERE NAME LIKE "%{name}%"')
    data = csr.fetchall()
    for i in data:
        if i[1]==name:
            csr.execute(f"UPDATE CONTACTS SET PHONE_NUMBER={number}, ADDRESS='{add}', NAME='{name1}' WHERE NAME='{name}'")
    mydb.commit()
    print("CONTACT SUCESSFULLY UPDATED")

#DELETING A CONTACT FROM TABLE 
def delete():
    name = input("ENTER CONTACT NAME TO BE DELETED:")
    csr.execute(f"DELETE FROM CONTACTS WHERE NAME='{name}'")
    mydb.commit()
    print("CONTACT SUCESSFULLY DELETED")
    
#DISPLAYING CONTENT OF TABLE
def display():
    csr.execute ("SELECT * FROM CONTACTS")
    for i in csr:
        print(i)

#__main__
def menu():
    print('\n\n\n')
    print("MENU AVAILABLE")
    print('\n')
    print("ENTER 1 TO INSERT CONTACTS")
    print('\n')
    print("ENTER 2 TO SEARCH A CONTACTS")
    print('\n')
    print("ENTER 3 TO CHANGE THE DETAILS OF  A CONTACT")
    print('\n')
    print("ENTER 4 TO DELETE A CONTACT")
    print('\n')
    print("ENTER 5 TO DISPLAY THE CONTENT OF THE TABLE")
    print('\n')
    print("ENTER 0 TO EXIT")

    return int(input("ENTER A NUMBER (1-5):"))


#csr.execute(f'DROP DATABASE {db_name}')
create_db()
while True:
    n = menu()
    print('\n\n')

    if n == 1:
        insert()

    elif n == 2:
        search()

    elif n == 3:
        update()
 
    elif n == 4:
        delete()
 
    elif n == 5:
        display()
 
    elif n == 0:
        break
 
    else:
        print("INVALID CHOICE")


print("THANK YOU...")
