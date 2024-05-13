#This is an example of behavioral design pattern that helps us to create separate classes and it encapsulates them and lets the client decide at the run time which functionality they need

#Some common examples of strategy design patterns are sorting algorithms,file compression types,payment processing and routing ,load balancing algorithms,cache management,trading systems
from abc import ABC,abstractmethod
#strategy
class Strategy(ABC):
    @abstractmethod
    def operation(self):
        pass

#concrete strategy
class ConcreteStrategy1(Strategy):
    def operation(self):
        print("Executing concrete strategy 1")
        
class ConcreteStrategy2(Strategy):
    def operation(self):
        print("Executing concrete strategy 2")
#context
class Context:
    def __init__(self,strategy:Strategy):
        self.strategy=strategy
    
    def execute_strategy(self):
        self.strategy.operation()
#client
strategy1=ConcreteStrategy1()
strategy2=ConcreteStrategy2()
context=Context(strategy1)
context.execute_strategy()
context.strategy=strategy2
context.execute_strategy()




