#This allows a request sent by the client to be received by more than one object.The objects on receiving the requests may either handle it or transfer it to the next object

#Whenever a client sends a request it is received by 1st handler in the chain,the 1st handler decides whether it can handle the request or not if not then it sends to the next one and this process goes on.

#Examples of chain of responsibility principle includes exception handling,middleware,logging system,event handling,and even the example of event bubbling

#Workflow systems also follow the chain of responsibility principle

#Handler,Concrete Handler,Successor,Client,Request.Handler is the abstract class and concrete handler is the concrete class,successor is the one in which the next flow will move

from abc import ABC,abstractmethod

class Handler(ABC):
    def __init__(self,successor=None):
        self.successor=successor
    
    @abstractmethod 
    def request_handler(self,request):
        pass
#now we will create two concrete handlers called as concreteHandler1,concreteHandler2
class ConcreteHandler1(Handler):
    def request_handler(self,request):
        if(request=="A"):
            print(f"{request} is handled at Handler 1")
        elif self.successor is not None:
            print("Handler 1 is not handling this request")
            #now move to the next one
            self.successor.request_handler(request)
#similarly create another concreteHandler2
class ConcreteHandler2(Handler):
    def request_handler(self,request):
        if(request=="B"):
            print(f"{request} is handled at Handler2")
        elif self.successor is not None:
            print("Handler 2 is not handling this request")
            self.successor.request_handler(request)
#similarly create another concreteHandler3

class ConcreteHandler3(Handler):
    def request_handler(self,request):
        if(request=="C"):
            print(f"{request} is handled at Handler3")
        elif self.successor is not None:
            #here move to the next successor
            self.successor.request_handler(request)
        else:
            print("Handler 3 is not handling the request")
            print("Request handling is terminated")
handler1=ConcreteHandler1()
handler2=ConcreteHandler2()
handler3=ConcreteHandler3()

handler1.successor=handler2
handler2.successor=handler3

handler1.request_handler("B")

handler2.request_handler("C")
            




