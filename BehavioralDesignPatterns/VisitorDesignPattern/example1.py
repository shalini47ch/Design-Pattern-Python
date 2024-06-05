#Visitor design pattern is a behavioral design pattern that allows you to separate the structure of the object from its operations
#It helps in providing a clear separation between the object structure and the operations performed on it.

#Real world examples like document processers in which various operations are performed such as spell check,word count
#It promotes various operations like rendering,event handling on various components like buttons,textfields,checkboxes,it can also be used in financial calculations

#Medical record systems can also use the visitor design pattern to perform various operations like data analysis,maintaining patient records

from abc import ABC,abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self,element):
        pass

class Visitor1(Visitor):
    def visit(self,element):
        element.operation1()
    
#similarly do it for visitor2
class Visitor2(Visitor):
    def visit(self,element):
        element.operation2()

#now once this is done we create element
class Element(ABC):
    @abstractmethod
    def accept(self,visitor):
        pass

class ConcreteElementA(Element):
    def accept(self,visitor):
        visitor.visit(self)
    
    def operation1(self):
        print("ConcreteElementA performing operation1")
    
    def operation2(self):
        print("ConcreteElementA performing operation2")
    
#similarly do it for concreteelement2
class ConcreteElementB(Element):
    def accept(self,visitor):
        visitor.visit(self)
    #similarly do it for operation1 and operation2
    def operation1(self):
        print("ConcreteElementB performing operation1")
    
    def operation2(self):
        print("ConcreteElementB performing operation2")

concrete1=ConcreteElementA()
concrete2=ConcreteElementB()

visitor1=Visitor1()
visitor2=Visitor2()

concrete1.accept(visitor1)
concrete2.accept(visitor2)

        

