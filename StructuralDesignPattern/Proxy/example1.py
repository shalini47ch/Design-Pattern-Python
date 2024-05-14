#This is a structural design pattern that allows the client to interact with an object indirectly using a proxy object
#The proxy object has the same interface as the original object so the client can use it interchangebily with original object

#This is useful in cases where the access to the real object is controlled or secured

#terminologies subject,realsubject,proxy,client
#subject is the abstract class and real subject is the one that will have all the implementation of the subject,proxy acts as an intermediate and helps the client to interact with subject
from abc import ABC,abstractmethod

class SubjectInterface(ABC):
    @abstractmethod
    def operation(self):
        pass
#now we will create two things one is the real subject and the other is the proxy subject
class RealSubject(SubjectInterface):
    def operation(self):
        print("Perform operation on real subject")

#now similarly create it for proxySubject
class ProxySubject(SubjectInterface):
    def __init__(self,real_subject):
        self.real_subject=real_subject
        
    def operation(self):
        #before performing the real subject operation the proxy can also perform the operation
        print("Perform some operation before real subject")
        self.real_subject.operation()

#now atlast we will write the client code
subject=RealSubject()
proxy=ProxySubject(subject)
proxy.operation()

