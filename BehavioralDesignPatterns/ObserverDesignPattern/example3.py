#Social Media Notification also used the observer design pattern
from abc import ABC,abstractmethod
class SocialMediaSubject:
    #this is the observable also called as subject
    def __init__(self):
        self._observers=[]
        self._posts=[]
    
    #here we will create two function acting as subscribe and unsubscribe and the last one will be the addpost method 
    
    def attach(self,observer):
        self._observers.append(observer)
    
    def detach(self,observer):
        self._observers.remove(observer)
    
    def add_post(self,post):
        self._posts.append(post)
        self.notify(post)
    
    #create another helper function called as notify
    def notify(self,post):
        for observer in self._observers:
            observer.update(post)
#now here we will create a concrete observable
class Observer(ABC):
    @abstractmethod
    def update(self,post):
        pass
class User(Observer):
    def __init__(self,name):
        self._name=name
    
    def update(self,post):
        print(f"User {self._name}:New post-{post}")
        
socialmedia=SocialMediaSubject()
user1=User("John")
user2=User("Hanna")
user3=User("Doe")

socialmedia.attach(user1)
socialmedia.attach(user2)
socialmedia.attach(user3)
print()
socialmedia.add_post("Hello Everyone")
print()
socialmedia.add_post("I just had a great weekend")
socialmedia.detach(user1)
print()
socialmedia.add_post("exciting news!")

#Observer pattern is used mainly in the situations where we need loose coupling between objects and flexible notification system

        