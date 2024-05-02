#it helps to decouple abstraction and implementation allowing both to vary independently
#and these abstraction and implementation are connected together by bridge pattern,since the abstraction and implementation are separate the code provides more flexibility

#Examples of bridge design pattern is graphic design software where the abstract class is a rectangle and the different types of rectangles are the implementations,video streaming also uses the bridge design pattern
from abc import ABC,abstractmethod 
#here shape is the abstract class
class Shape(ABC):
    def __init__(self,color):
        self.color=color 
    
    @abstractmethod
    def shape_type(self):
        pass
    
    def __str__(self):
        return f"This is a {self.color.name()} {self.shape_type()}"
        

#now creating different types of shapes called as square,rectangle and circle
class Circle(Shape):
    def shape_type(self):
        return "Circle"
    
class Square(Shape):
    def shape_type(self):
        return "Square"

class Rectangle(Shape):
    def shape_type(self):
        return "Rectangle"
    
#create one more abstract class called as color
class Color(ABC):
    @abstractmethod 
    def name(self):
        pass

class Red(Color):
    def name(self):
        return "Red"

class Blue(Color):
    def name(self):
        return "Blue"

class Orange(Color):
    def name(self):
        return "Orange"
    
#here in bridge both implementation and abstraction are different so the code is more maintainable
red=Red()
blue=Blue()
circle=Circle(red)
circle_blue=Circle(blue)
print(circle)
print(circle_blue)
print(Square(Orange()))

    

    


    

        


