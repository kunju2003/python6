class atm:
    def __init__(self):
        self.pin=1234
        self.balance=0
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
user=atm()
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
                
      
