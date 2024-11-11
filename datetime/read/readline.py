try:
    f=open('C:/Users/acer/OneDrive/Desktop/python2/datetime/sample.txt','r')
except:
    pass
# readline
    f=open('C:/Users/acer/OneDrive/Desktop/python2/datetime/sample.txt','r')

line=f.readline(7)
print(line)
rline=f.readline()
print(rline)


# readlines
line=f.readlines()
print(line)

for i in line:
    for j in i:
      print(j)

