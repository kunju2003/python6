add=lambda a,b:a+b
print(add(5,2))


# built in function
l=[1,2,3,4]
res=map(lambda a:a*a,l)
print(list(res))


l=[1,2,3,4]
def square(x):
    return x*x
res=map(square,l)
print(list(res))