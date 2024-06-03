#It is a type of behavioral design pattern that provides a skeleton of algorithms in base class that can be implemented by the derived classes

#It can be used in database query execution,in web applications where the base class that represents the request handling mechanism whereas the other implementations like authentication,routing and all are implemented in the subclasses

#Beverage preparation also uses the template design pattern as most of the beverages will have a common structure and only some part of implementation will change

#Network protocol implementation will also use the template design pattern

#abstractclass
#template method
 #abstractmethod these need to be implemented by each and every subclasses
 #hookmethod these are optional

from abc import ABC,abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.initialize()
        self.perform_algorithm()
        self.cleanup()
    
    #we will keep the perfrom algorithm as a abstractmethod which needs to be implemented in each subclass
    def initialize(self):
        print("Initializing the algorithm")
    
    @abstractmethod
    def perform_algorithm(self):
        pass
    
    def cleanup(self):
        print("Cleaning up after the algorithm")

class ConcreteClass1(AbstractClass):
    def perform_algorithm(self):
        print("Performing algorithm for concreteclass 1")
    
class ConcreteClass2(AbstractClass):
    def perform_algorithm(self):
        print("Performing algorithm for concreteclass2")
#now atlast calling the client code

concreteobject1=ConcreteClass1()
concreteobject1.template_method()
print()

concreteobject2=ConcreteClass2()
concreteobject2.template_method()


