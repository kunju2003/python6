# class sample:
#     def python():
#         print("python")
#     def php():
#         print("PHP")
# std1=sample
# std1.python()     
# std1.php()   


class synnefo:
    def __init__(self):
        self.name=input("enter a name:")
        self.age=input("enter age:")
        self.place=input("enter place:")
    def python(self):
        print(self.name,self.age,self.place)   
    def php(self):
        print(self.name,self.age,self.place)    
std1=synnefo()
std1.python()
std2=synnefo()
std2.php()