#In the previous example we use Object Adapter now we will use the class Adapter in the object adapter we used the composition whereas in class Adapter we will use multiple inheritance
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
class Adapter(Target,Adaptee):
    def request(self):
        return self.complex_request()

#now at last we call the client code
service=Service()
print(service.request())

adapter=Adapter()
print(adapter.request())
#we will solve it using multiple inheritance
