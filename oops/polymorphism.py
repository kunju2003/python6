# method overriding
class school:
    def teacher(self):
        print("teacher_school")
class tution(school):
    def teacher(self):
        super().teacher()
        print("teacher_tution")  
std1=tution()
std1.teacher()        
