class vehicle:
    def __init__(self,brand):
        self.__brand=brand
        print(self.__brand)
    def  displaybrand(self):
        print(self.__brand) 
    def branding(self):
        return f"the brand is {self.__brand}"       
car=vehicle("Mustang")  
print(car.branding()) 