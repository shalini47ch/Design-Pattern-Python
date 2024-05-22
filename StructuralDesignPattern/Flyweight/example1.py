#Flyweight design pattern is a structural design pattern that aims to minimize the memory usage of an application by sharing as much data possible between similar objects

#The main idea behind the flyweight design pattern is to create lightweight objects called as flyweight which will have all the logic of code and these can be reused

#By using flyweights we reduce the memory usage and improve the performance of our system as it helps us to prevent usage of redundant code

#Some common examples of flyweight design patterns are text editors in which many characters may share the same font and size so we can create a flyweight and use them

#It is also used in computer games where we have trees and houses that are used throughout the game so we will create one flyweight and it can be reused throughout

#An example of flyweight design pattern is car factory

#this is the flyweight
import random
class Car:
    def __init__(self,make,model,color):
        #here we will not initialize the shipped to it will be initialized at run time
        self.make=make
        self.model=model
        self.color=color
        self.shipped_to=None
    #now create a helper function to get_carinfo
    def get_info(self):
        print(f"Make:{self.make},Model:{self.model}")
        #similarly add it for color and shipped to
        print(f"Color:{self.color},Shipped To:{self.shipped_to}")
        print()
#now here we will create the flyweight factory where the operations will be performed
class CarFactory:
    _cars={} #this is the hmap which will store the creation of different types of cars
    #instead of using the self we can use the class name directly
    @staticmethod
    def create_car(make,model,color):
        if (make,model,color) not in CarFactory._cars:
            #means it is not present in hmap so we will add in the hmap
            car=Car(make,model,color)
            CarFactory._cars[(make,model,color)]=car
        return CarFactory._cars[(make,model,color)]
    
if __name__=="__main__":
    cars=[
        CarFactory.create_car("Toyota","Venza","Red"),
        CarFactory.create_car("Toyota","Corolla","Blue"),
        CarFactory.create_car("Toyota","Camry","Ash"),
        CarFactory.create_car("Toyota","Venza","Red"),
        CarFactory.create_car("Toyota","Corolla","Blue")
   
    ]
    #here create an array for shipped to location
    location=["Nigeria","USA","Germany","France","China"]
    for ele in cars:
        ele.shipped_to=random.choice(location)
        ele.get_info()
    
