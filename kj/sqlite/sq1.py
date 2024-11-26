import sqlite3
con=sqlite3.connect("student.db")
try:
    con.execute('create table student(admno int,name text,email text)')
except:
    pass
# con.execute('insert into student values(124,"lilly","li@gmail.com")')
# con.commit()
# admno=int(input("enter admo:"))
# name=input("enter name:")
# email=input("enter email:")
# con.execute('insert into student values(?,?,?)',(admno,name,email))
# con.commit()
# data=con.execute('select * from student where name like "%s_"')
# for i in data:
#     print(i)
try:
    con.execute('create table marks(admno int,malayalam int,hindi int,english int)')
except:
    pass
# con.execute('insert into marks values(123,5,4,10)')
# con.execute('insert into marks values(124,10,10,3)')
# con.commit()
data=con.execute('select student.admno,student.name,marks.malayalam,marks.hindi,marks.english from student join marks on student.admno=marks.admno')
for i in data:
    print(i)