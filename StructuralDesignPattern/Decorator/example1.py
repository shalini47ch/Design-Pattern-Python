#The decorator design pattern is a structural design pattern that helps to add dynamic behavior without affecting the behavior of existing code

#This is useful when we want to add functionality without modifying the existing code
#Some examples of decorator design pattern coffee toppings
#Text formatization and car customization

#Cake decoration also can use different types of decoration and these are all examples of decorator design pattern

#The various terminologies concerned with decorator design pattern component,concrete component,decorator,concrete decorator,client
#decorator is the one that will add additional functionalities

from abc import ABC,abstractmethod
#this is an abstract class
class Coffee(ABC):
    @abstractmethod 
    def get_cost(self):
        pass
    
    def get_description(self):
        pass
#now first we will create a concrete abstractclass
class PlainCoffee(Coffee):
    def get_cost(self):
        return 2
    
    def get_description(self):
        return "Plain Coffee"

#now the next step is to create coffee decorator
class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self.coffee=coffee
    
    def get_cost(self):
        return self.coffee.get_cost()
    
    def get_description(self):
        return self.coffee.get_description()

#now here we will add concrete decorators 
class Milk(CoffeeDecorator):
    def get_cost(self):
        #here we added extra cost
        return self.coffee.get_cost()+1.99
    
    def get_description(self):
        return self.coffee.get_description()+"-->Milk"

class Sugar(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost()+2.11
    
    def get_description(self):
        return self.coffee.get_description()+"-->Sugar"

coffee=PlainCoffee()
coffee=Milk(coffee)
#here similarly adding decorators like sugar as well
coffee=Sugar(coffee)
print(f"Mix:{coffee.get_description()}-${coffee.get_cost()}")

#here milk and the sugar are examples of decorator design pattern





