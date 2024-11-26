import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='kj',password='kunju123',database='sample')
mycursor=mydb.cursor()
try:
    mycursor.execute('create database sample')
except:
    pass
try:
    mycursor.execute('create table student(admno int,name text,email text)')
except:
        pass

a=int(input("enter limit:"))
for i in range(a):
    admno=int(input("enter admno:"))
    name=input("enter name:")
    email=input("enter email:")
    mycursor.execute('insert into student values(%s,%s,%s)',(admno,name,email))
    mydb.commit()