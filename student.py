students_list=[]

def add_student():
    name=input("enter the student's name:")
    age=int(input("enter the student's place:"))
    place=input("enter the student's place:")
    student={'Name':name,'Age':age,'Place':place}
    students_list.append(student)
    print("student{name}added successfully.")

def delete_student():
    name=input("enter the name of the student to delete:")   
    for student in students_list:
        if student['Name'].lower()==name.lower():
            students_list.remove(student)
            print(f"student {name} deleted successfully.")    
            return
        print("student not found")    

def search_student():
    name=input("enter the name of the student to search:")  
    for student in students_list:
        if student['Name'].lower()==name.lower():
            print(f"student found:{student}")
            return
        print("student not found")

def show_all_students():
    if not students_list:
        print("no students in the list.")  
    else:
        print("\nlist of all students:")  
        print("{:<15}{:<10}{:<15}".format("Name","Age","Place"))  
        print("-"*40)   
        for students in students_list:
            print("{:<15}{:<10}{:<15}".format(students['Name'],students['Age'],students['Place']))  
while True:
    print("\nchoose an option:") 
    print("1.Add student")   
    print("2.Delete student")  
    print("3.Search student")  
    print("4.Show all student")
    print("5.Exit")   
    choice=input("enter your choice (1/2/3/4/5):")
    if choice=='1':
        add_student()
    elif choice=='2':
        delete_student()    
    elif choice=='3':
        search_student()
    elif choice=='4':
        show_all_students()     
    elif choice=='5':
        print("exiting the program")
        break    
    else:
        print("invalid choice")          