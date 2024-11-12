class bank:
    def __init__(self):
        self.pin=1243
    def login(self):
        upin=int(input("enter your pin:"))  
        if upin==self.pin:
            print("successfully logged in")
        else:
            print("invalid pin")   
u1=bank()             
u1.login()