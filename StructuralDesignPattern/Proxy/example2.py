#Example of proxy involves remote proxy these are the ones in which the systems are present in different locations
from abc import ABC,abstractmethod 

class RemoteService(ABC):
    @abstractmethod
    def perform_action(self):
        pass
#this is the realsubject class

class RemoteServiceImplementation(RemoteService):
    def perform_action(self):
        print("Performing the actual action in the remote service")
        
#here we will create a proxy service
class RemoteServiceProxy(RemoteService):
    def __init__(self,remote_service):
        self.remote=remote_service
    
    def perform_action(self):
        print("Proxy:Before performing the action")
        self.remote.perform_action()
        print("Proxy:After performing the action")
remote=RemoteServiceImplementation()
proxy=RemoteServiceProxy(remote)
proxy.perform_action()