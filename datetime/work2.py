# limit=int(input("enter the limit:"))
# f=open('C:/Users/acer/OneDrive/Desktop/python2/datetime/sample.txt','w')
# for i in range(limit):
#          name=input("enter name:")
#          f.write(name+'\n')


f=open('C:/Users/acer/OneDrive/Desktop/python2/datetime/sample.txt','r')
names=f.read(8)
names_remain=f.read()
print(names)
print(names_remain)
print(f.tell())


         