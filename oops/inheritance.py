# single
class novavi:
    def web_dev():
        print("web_dev")
    def app_dev():
        print("app_dev")
class synnefo(novavi):
    def training():
        print("training")   
staff=synnefo  
staff.web_dev()  
staff.app_dev()
staff.training()

# multiple
class school:
    def teacher():
        print("teacher")
class tution():
    def notes():
        print("notes")   
class student(school,tution):
    def learning():
        print("learning") 
obj=student
obj.teacher() 
obj.notes()
obj1=tution
obj1.notes()                   

# multilevel
class synnefo:
    def python_training():
        print("training")
class staff(synnefo):
    def staff1():
        print("staff")
class student(staff):
    def std():
        print("std")
obj=student
obj.python_training()
obj.staff1()
obj.std()
obj1=staff
obj1.python_training()                      