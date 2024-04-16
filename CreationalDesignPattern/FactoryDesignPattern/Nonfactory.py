#this will consist of the code which doesnt have factory implementation and has multiple if else statements
class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type=vehicle_type
        
    def start(self):
        if(self.vehicle_type=="car"):
            print("Starting the car")
        elif(self.vehicle_type=="bike"):
            print("Starting the bike")
        elif(self.vehicle_type=="bicycle"):
            print("Starting the bicycle")
        else:
            print("Invalid vehicle type")
car=Vehicle("car")
car.start()
    
bike=Vehicle("bike")
bike.start()

#Drawbacks:

#1.Here this  code is not a right code implementation as it is violating the single responsibilty principle the vehicle classis handling two things one is the vehicle type andthe other is starting of vehicle.
#2.Sincethe objects are created again and again here it has tight coupling.So every time a new vehicle type is added we have to change the client code which will result in more maintainance and will expose our system to errors
# 3.Abstraction layer is missing so it makes it difficult to add new vehicle types in it
#4.This also has code duplication which violates the DRY Principle
