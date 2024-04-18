#Example of factory design pattern
#Furnite,Electronics and Decoration
#Here we will have three different types of products

from abc import ABC,abstractmethod

#Product 1
class Furniture(ABC): #This is the Product
    def __init__(self,quantity):
        self.quantity=quantity
    
    @abstractmethod
    def display(self):
        pass

class Chair(Furniture): #this is the concrete product inherited from product
    def display(self):
        return f"{self.quantity} Chair"
    
#similarly do it for Sofa as well
class Sofa(Furniture):
    def display(self):
        return f"{self.quantity} Sofa"


#Similarly create it for Electronics and Decoration

#Product 2
class Electronics(ABC):
    def __init__(self,quantity):
        self.quantity=quantity
    
    @abstractmethod
    def display(self):
        pass

#we will consider Radio and the Television Electronics

class Television(Electronics):
    def display(self):
        return f"{self.quantity} Television"
#similarly do it for Radio 

class Radio(Electronics):  
    def display(self):
        return f"{self.quantity} Radio"
    
    
#now similarly do it for Decoration
#Product 3
class Decoration(ABC):
    def __init__(self,quantity):
        self.quantity=quantity
    
    def display(self):
        pass
        
#create other two concrete Product 
class FlowerVase(Decoration):
    def display(self):
        return f"{self.quantity} FlowerVase"
    
#similarly do it for chandelier
class Chandelier(Decoration):
    def display(self):
        return f"{self.quantity} Chandelier"
    
#Now the next step is to create Housefactory abstract class
class HouseFactory(ABC):
    @abstractmethod 
    def furniture(self):
        pass
    
    @abstractmethod
    def electronics(self):
        pass
    
    @abstractmethod
    def decoration(self):
        pass

#now here create the subclasses
class SmallHouse(HouseFactory):
    def furniture(self):
        return Chair(4)
    
    def electronics(self):
        return Television(1)
    
    def decoration(self):
        return FlowerVase(2)
    
#similarly do it for big house

class BigHouse(HouseFactory):
    def furniture(self):
        return Chair(6)
    
    def electronics(self):
        return Television(2)
    
    def decoration(self):
        return FlowerVase(4)
    

    
#now writing the client code
def client(factory:HouseFactory):
    print("Furniture",factory.furniture().display())
    print("Electronics",factory.electronics().display())
    print("Decoration",factory.decoration().display())
    print()
#now the next is to call for smallhouse big house and so on
print("Small House ******")
client(SmallHouse())


print("Big House ******")
client(BigHouse())
    

        
    

    
    







    

    



