from abc import ABC,abstractmethod 

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass
#now the next step is to create concrete product A and concreteProductB
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

#similarly create another class concreteProductB

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"
#now we will create another abstract class called as creator which will have the factory method to decidewhich subclass to call

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
#now creating concreteCreator for both product A and B
class ConcreteCreatorA(Creator):
    def factory_method(self)->Product:
        return ConcreteProductA()
#similarly do for concreteCreatorB
class ConcreteCreatorB(Creator):
    def factory_method(self)->Product:
        return ConcreteProductB()

#now at last we will write the client code
creator_a=ConcreteCreatorA()
product_a=creator_a.factory_method()
print(product_a.operation())

#similarly do it for productB
creator_b=ConcreteCreatorB()
product_b=creator_b.factory_method()
print(product_b.operation())
