add=lambda a,b:a+b
print(add(5,2))


# built in function

# map
l=[1,2,3,4]
res=map(lambda a:a*a,l)
print(list(res))


l=[1,2,3,4]
def square(x):
    return x*x
res=map(square,l)
print(list(res))

# filter
l=[1,2,3,4,5,6]
even=list(filter(lambda x:x%2==0,l))
print(even)

l=[1,2,3,4,5,6]
def even(x):
    return x%2==0
res=list(filter(even,l))
print(res)

# reduce,# module
from functools import reduce
import loop as lo
l=[1,2,3,4,5]
res=reduce(lambda x,y:x+y,l)
print(res)
lo.fun()
lo.fun1()

from functools import reduce
from loop import *
l=[1,2,3,4,5]
res=reduce(lambda x,y:x+y,l)
print(res)
fun()
fun1()

l=[1,2,3,4,5]
def sum(x,y):
    return x+y
res=reduce(sum,l)
print(res)

l=[1,3,26,15,7,21,5]
res=list(filter(lambda x:x%3==0,l))
print(res)

