from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def tyre():
        print("tyre")
class bike(vehicle):
    def tyre():
        print(2) 
duke=bike
duke.tyre()                   