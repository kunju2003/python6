# hierarchical
class school:
    def classes():
        print("class")
class staff(school):
    def subjects():
        print("maths")
class student(school):
    def learning():
        print("english") 
obj=student
obj.learning()  
obj.classes()  
obj1=staff
obj1.classes()
                               