#It is a type of behavioral design pattern that defines a language or grammar and provides a way to execute sentences and expressions of that language
#Real life scenarios of interpreter design pattern includes programming languages like python,ruby which use this pattern to evaluate and execute the code

#They are also used in regular expression matching

#create an interface
class Expression:
    def interpret(self):
        pass

class Number(Expression): #this is a terminal expression
    def __init__(self,value):
        self.value=value
    
    def interpret(self):
        return self.value

#here we will create two non terminal expressions called as Addition and Subtraction

class Addition(Number):
    def __init__(self,expression1,expression2):
        self.expression1=expression1
        self.expression2=expression2
    
    def interpret(self):
        return self.expression1.interpret()+self.expression2.interpret()

class Subtraction(Number):
    def __init__(self,expression1,expression2):
        self.expression1=expression1
        self.expression2=expression2
    
    def interpret(self):
        return self.expression1.interpret()-self.expression2.interpret()

#here we will first perform it for addition
expression=Addition(Number(5),Number(10))
print(expression.interpret())

#similarly do it for subtract operation
expression1=Subtraction(Number(15),Number(6))
print(expression1.interpret())

#we can also solve a complicated expression using this
expression2=Addition(Number(10),
                     Subtraction(Number(12),Number(10)))
print(expression2.interpret())

