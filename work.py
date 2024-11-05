l=[10,1,3,5,8]
large=l[0]
small=l[0]
for i in l:
    if i > large:
        large=i
    if i<small:
        small=i
print("largest number:",large) 
print("smallest number:",small)   

