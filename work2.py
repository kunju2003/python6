l=['apple','kiwi','orange','watermelon']
large=l[0]
for i in range(len(l)):
    if len(l[i])>len(l):
        large=i
print(l[large])      
