std=int(input("enter the number of students:"))
l=[]
for i in range(std):
   a=input("enter name:")
   b=int(input("enter age:"))
   c=input("enter place:")
   l.append({'name':a,'age':b,'place':c})
print(l)


