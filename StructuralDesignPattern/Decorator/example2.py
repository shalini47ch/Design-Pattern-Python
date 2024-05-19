#This helps us to add additional functionalities during run time without modifying the original object
#Example of creating a shape decorator

#first create an abstract class called as Shape
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

#here now we will create a concrete class
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

#now here we will create decorator
class ShapeDecorator(Shape):
    def __init__(self,shape):
        self.shape=shape
    
    def draw(self):
        return self.shape.draw()
#now here we will create concrete decorators
class RedShapeDecorator(ShapeDecorator):
    def draw(self):
        self.shape.draw()
        self.red_color()
        
    def red_color(self):
        print(f"Painting {self.shape.__class__.__name__} Red")

class BlueShapeDecorator(ShapeDecorator):
    def draw(self):
        self.shape.draw()
        self.blue_color()
    
    def blue_color(self):
        print(f"Printing {self.shape.__class__.__name__} blue")
    
#now here we write the client code
rectangle=Rectangle()
red=RedShapeDecorator(rectangle)
blue=BlueShapeDecorator(rectangle)
rectangle.draw()
print()
red.draw()
print()
blue.draw()
print()
    
        

        