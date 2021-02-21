import mysql.connector as  mys
mydb=mys.connect(host="localhost",user="root",passwd="admin")
myc = mydb.cursor()
#INSERTION
def insert():
    myc.execute("CREATE DATABASE PHONE DIRECTORY")
    myc.execute("USE PHONE DIRECTORY")
    myc.execute("CREATE TABLE CONTACTS(SNO.int PRIMARY KEY, NAME VARCHAR(20) UNIQUE NOT NULL, PHONE NUMBER int UNIQUE NOT NULL")

    n= int (input("ENTER NUMBER OF CONTACTS TO BE INSERTED:"))
    for i in range(n):
        sno=int(input("ENTER S.NO:"))
        name=input("ENTER NAME OF THE CONTACT:")
        no=int(input("ENTER PHONE NUMBER:"))
        myc.execute("INSERT INTO CONTACTS VALUES ({},'{}',{})format(sno,name,no)")
        mydb.commit()
        print("CONTACTS INSERTED SUCCESSFULLY")

#SEARCHING CONTACT IN TABLE

def search():
    name=input("ENTER NAME OF CONTACTS TO BE SEARCHED:")
    data=myc.fetchall()
    for i in data:
        if i[1]==name:
            print("CONTACT SUCESSFULLY FOUND")


#UPDATING A CONTACT IN TABLE
def update():
    number=int(input("ENTER NUMBER TO BE UPDATED:"))
    name=input("ENTER NAME OF CONTACT:")
    myc.execute("UPDATE CONTACTS SET PHONE NUMBER={} WHERE NAME='{}'format(number,name)")
    mydb.commit()
    print("CONTACT SUCESSFULLY UPDATED")


#DELETING A CONTACT FROM TABLE 
def delete():
    name=input("ENTER NAME OF CONTACT TO BE DELETED:")
    myc.execute("DELETE FROM CONTACTS WHERE NAME='{}format(name)")
    mydb.commit()
    print("CONTACT SUCESSFULLY DELETED")
    
#DISPLAYING CONTENT OF TABLE 
def display():
    print("TABLE AFTER PERFORMING PREVIOUS TASKS")
    myc.execute ("SELECT*FROM CONTACTS")
    for i in myc:
        print(i)
#__main__
ans='y'
while ans.lower()=='y':
    print("MENU AVAILABLE")
    print("ENTER 1 TO INSERT CONTACTS")
    print("ENTER 2 TO SEARCH A CONTACTS")
    print("ENTER 3 TO UPDATE A CONTACT")
    print("ENTER 5 TO DISPLAY THE CONTENT OF THE TABLE")
    print("ENTER 6 TO EXIT")
    n=int(input("ENTER A NUMBER (1-5):"))
    if n==1:
        insert()
        ans=input("DO YOU WANT TO CONTINUE (y/n):")
    elif n==2:
        search()
        ans=input("DO YOU WANT TO CONTINUE(y/n):")
    elif n==3:
        update()
        ans=input("DO YOU WANT TO CONTINUE(y/n):")
    elif n==4:
        delete()
        ans=input("DO YOU WANT TO CONTINUE(y/n):")
    elif n==5:
        display()
        ans=input("DO YOU WANT TO CONTINUE(y/n):")
    elif n==6:
        break
    else:
        print("INVALID CHOICE")
        ans=input("DO YOU WANT TO CONTINUE(y/n):")

print("THANK YOU...")
