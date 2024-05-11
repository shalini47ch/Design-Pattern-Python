
#State design pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes

#The main idea of state design pattern is to encapsulate the behavior of different states in separate classes,this is useful when the behavior of an object depends on changes in its internal state

#Usecases where we can use state design pattern is document processing like editing,reviewing and finalizing

#This design pattern can also be used in traffic light systems to display the different states of light like green,yellow,red

#State pattern can be used in an ATM to handle the different states like idle,card inserted,transaction processing

#Booking system having different states reserved,confirmed,checkin and cancelled

#Network connection like connected,disconnected or error

#here we will have context and state

from abc import ABC,abstractmethod

class State(ABC):
    @abstractmethod
    def do_action(self,context):
        pass

#create two concrete states as StateA,StateB

class StateA(State):
    def do_action(self,context):
        print("State A performing action")
        #here this will call the next state
        context.state=StateB()
        
class StateB(State):
    def do_action(self,context):
        print("State B performing action")
        context.state=StateC()
        
#here StateB is calling the StateC
class StateC(State):
    def do_action(self,context):
        print("State C performing action")
        #here from stateC we can move to stateA again
        context.state=StateA()
    
class Context:
    def __init__(self):
        self.state=StateA()
    def request(self):
        return self.state.do_action(self)
    
context=Context()
context.request() #A will move to stateB and B will move to C and C will move back to A
context.request()
context.request()
context.request()

    
    
    
    





