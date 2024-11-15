class school:
    def __init__(self,sname):
        print(sname)
class student(school):
    def __init__(self,sname,location):
        super().__init__(sname)  
        print(location)  
std1=student('GMHS','CALICUT')   
              