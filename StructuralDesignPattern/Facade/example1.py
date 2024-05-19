#It is a structural design pattern that provides a simple interface to a complex system of code
#The facade is the class that will have all the functionalities in a single class

#The facade design pattern acts as an interface between the client and the subclasses
#Some real world use cases where it is used is Mobile App Development,Media Players,Payment Systems
#The components in facade design pattern includes facade,complex subsystem and then the client

class SubSystemA:
    def operationA1(self):
        print("Subsystem A operation A1")
    
    def operationA2(self):
        print("Subsystem A operation A2")
#similarly do it for subsystemB 
class SubSystemB:
    def operationB1(self):
        print("Subsystem B operation B1")
    
    def operationB2(self):
        print("Subsystem B operation B2")
#now we will create a facade class
#here facade is able to include both subsystemA and subsystemB
class Facade:
    def __init__(self):
        self.subsystemA=SubSystemA()
        self.subsystemB=SubSystemB()
    
    def operation1(self):
        self.subsystemA.operationA1()
        self.subsystemB.operationB1()
    #similarly do it for operation 2
    def operation2(self):
        self.subsystemA.operationA2()
        self.subsystemB.operationB2()
#now the next step is to  use the client code
if __name__=='__main__':
    facade=Facade()
    facade.operation1()
    facade.operation2()





