from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting the car")

class Bike(Vehicle):
    def start(self):
        print("Starting the bike")
        
class Bicycle(Vehicle):
    def start(self):
        print("Starting the bicycle")
        
#now the next step is to createFactory
class VehicleFactory:
    def __init__(self):
        self.factory=dict(car=Car,bike=Bike,bicycle=Bicycle)
        
    def create_vehicle(self,vehicle_type):
        if vehicle_type in self.factory:
            vehicle=self.factory.get(vehicle_type)
            return vehicle()
## client code 

factory=VehicleFactory()
#creating for the car

car=factory.create_vehicle("car")
car.start()

bike=factory.create_vehicle("bike")
bike.start()

bicycle=factory.create_vehicle("bicycle")
bicycle.start()
    
    

    

        
