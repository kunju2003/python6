class banking:
    def __init__(self):
        
        self.balance=0
    def register(self):
        self.username=input("enter your username:")
        self.password=(input("enter your password:"))
        self.pin=int(input("enter your pin:"))
        self.name=input("enter name:")
        self.email=input("enter you email:")
        print(f"successfully registered")  
    def login(self):
       name=input("enter your username:")
       if name==self.username:
           password=input("enter your password:")
           if password==self.password:
               print("successfully logged in")
           else:
               print("invalid")   
       else:
           print("invalid username")  
        
         
    def check_balance(self):
        upin=int(input("enter your pin:")) 
        if upin==self.pin:
            print("balance:",str(self.balance)+".00")
        else:
            print("invalid pin")
    def withdraw(self): 
        upin=int(input("enter your pin:"))
        if upin==self.pin:
            wamount=int(input("enter the amount that you need to withdraw:"))
            if wamount<=self.balance:
                self.balance-=wamount
            else:
                print("you do not have enough money")    
        else:
            print("invalid pin")     

    def deposit(self):
        upin=int(input("enter your pin:"))     
        if upin==self.pin:
            damount=int(input("enter the amount that you need to deposit:"))    
            self.balance+=damount 
        else:
            print("invalid pin")            
user=banking()
while True:
    print(""" 
     1.register
     2.login
     3.exit""")   
    choice=int(input("enter your choice:"))   
    if choice==1:
        user.register()
    elif choice==2:
        user.login()
    elif choice==3:
         break
    else:
         print("invalid choice")

while True:
    print("""
    1.balance enquiry
    2.withdraw
    3.deposit
    4.exit""")
    choice=int(input("enter your choice:"))
    if choice==1:
        user.check_balance()
    elif choice==2:
        user.withdraw()
    elif choice==3:
        user.deposit()
    elif choice==4:
        break
    else:
        print("invalid choice")           
                