from abc import ABC,abstractmethod

class Subject(ABC):
    @abstractmethod 
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("Processing request of real subject")
#this is the proxy
class ProtectionProxy(Subject):
    def __init__(self,real_subject,access_level):
        self.real_subject=real_subject
        self.access_level=access_level
    
    def request(self):
        if self.access_level=="admin":
            self.real_subject.request()
        else:
            print("Access denied:You dont have the required previledges")
#only the admins can access the request now atlast we will call the client
real_subject=RealSubject()
admin_proxy=ProtectionProxy(real_subject,"admin")
admin_proxy.request()

    
    