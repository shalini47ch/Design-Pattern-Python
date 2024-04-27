class Service:
    def request(self):
        return "Get service from provider"
    
#create an adaptee
class Adaptee:
    #this will have a method different from the target interface and the adapter will use the adaptee that can be used by the client
    def complex_request(self):
        return "Get complex_request from provider"

class Target:
    def request(self):
        pass

#now create adapter that will use adapteee
class Adapter(Target):
    def __init__(self,adaptee):
        self.adaptee=adaptee
    def request(self):
        return self.adaptee.complex_request()

#now at last we call the client code
service=Service()
print(service.request())

adapter=Adapter(Adaptee())
print(adapter.request())




#This is a structural design pattern that allows two incompatible interfaces to interact with each other by creating an intermediate adapter.
#Useful in systems where we have existing code and we cant change it but we need it to interact with new code so in that case you can use adapter design pattern.
#Real world use cases one is the power plug adapters that help in converting interface of electrical device to interface of electrical socket.

#Another example is USB to SerialPort Adapter

#One more example is that of the language translator

#Terminologies

#Target is the interface that the client will use for interaction

#Adaptee is the existing system that needs to adapt to the target to work with it

#Adapter is the class that adapts the adaptee to the target interface 

##Client is the one that will use the target 



