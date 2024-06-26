#Here we will consider the example of cache proxy what it does is that it checks whether it is already present in the cache if present it doesnt create a new one
from abc import ABC,abstractmethod 

#here we create a subject interface 
class Subject(ABC):
    @abstractmethod
    def request(self,key):
        pass

#here creating a real subject
class RealSubject(Subject):
    def request(self,key):
        print(f"Returning data for the key '{key}'")
        return f"Data for key '{key}'"
#here we will create a separate proxy
class CacheProxy(Subject):
    def __init__(self,real_subject):
        self.real_subject=real_subject
        self.cache={} #this is the hashmap which will help us to check for the data whether it exists or not
    
    def request(self,key):
        if key in self.cache:
            print(f"Returning cache data for the key '{key}'")
            return self.cache[key]
        else:
            data=self.real_subject.request(key)
            self.cache[key]=data
            print(f"Caching data for key '{key}'")
            return data
#client code
cacheproxy=CacheProxy(RealSubject())
#when you run it for the first time it is caching the data and in the next time it is returning the data from the cache
res=cacheproxy.request("key2")
print(res)

#cache proxy helps us to reduce memory usage and speed up the process and reduces the complexity of the code
#It should promote lazy initalization so that we can improve the performance of the website

#Disadvantages of proxy design pattern are that it reduces the performance of the website and will not be suitable for all test cases

#If the proxy is the only way to access the object it will invoke the single point of failure
#The proxy should be able to handle the errors in a way that it is transparent to the client

    
    
    
    