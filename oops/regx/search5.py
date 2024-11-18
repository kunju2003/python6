import re
a="Welcomes"
b="Welcomes1"
res1=re.search('[a-z]',a)
res2=re.search('[A-Z]',b)
res3=re.search('[0-9]',b)
res4=re.search('[A-Za-z0-9]',a)
res5=re.search('[A-Z][a-z][0-9]',b)
res6=re.search('[A-Z].{8}',b)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)