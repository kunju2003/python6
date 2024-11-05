# positional
def std(name,age):
    print(name,age)
std("abhi",24)

# keyword
def std(name,age):
    print(name,age)
std(age=24,name="Hari")    

# arbitary
def std(*arg):
    print(arg)
std('jerrin',24,'trissur')   
std('abhinav','kozhikode') 

# default
def std(name,age,course='python'):
    print(name,age,course)
std('abhinav',23,'java')    
std('adharsh',22)

# arbitary keyword
def std(**arg):
    print(arg)
std(name='vinayak',age=22,place='kozhikode')    
std(name='jayalakshmi',place='mala')    
std(name='abhinesh',age=24,place='trissur')    