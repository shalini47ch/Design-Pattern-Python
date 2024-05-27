#Observer design pattern is a type of behavioral design pattern that ensures that multiple observers can be notified when the state changes.The main object is called as Observable and the different parts in which it transfers the request is called as observer

#The observable is the main one and the others that are waiting for notification are called observers
#Some real life scenarios where we apply stock market where the stock market is the subject/observable and the investors are the people who will receive the updates/notifications,Weather monitoring systems also follow the observer design pattern,GUI also use the observer design pattern to handle event handling

#Traffic management system where the main control part is the observable and the others receiving the request are observers

#Concrete Observable are the ones that do the implementation of observables
#Concrete Observer are the implementation of observables
#Subscription:When an observer registers to receive notifications and is added to the list
#Unsubscription:When an observer unregisters and doesnt receive any more notification
#here we will create the observer or the subject
class Subject:
    def __init__(self):
        self._observers=[]
    #now there are three functions called as subscribe,unsubscribe and notify
    
    def subscribe(self,observer):
        self._observers.append(observer)
    
    def unsubscribe(self,observer):
        self._observers.remove(observer)
    
    def notify(self,message):
        for observer in self._observers:
            observer.update(message)
#now here we will create a concrete subject

class WeatherStation(Subject):
    def set_weather(self,weather):
        print("Weather station:Setting weather to",weather)
        self.notify(weather)
#now here creating observers and then concrete observers
class Observer:
    #here the observers will have the update method
    def update(self,message):
        pass
#now here we will create ConcreteObservers
class MobileApp(Observer):
    def update(self,message):
        print("Mobile App received ",message)

class DesktopApp(Observer):
    def update(self,message):
        print("Desktop App received",message)
#now at last calling 
weatherstation=WeatherStation()
mobileapp=MobileApp()
desktopapp=DesktopApp()

weatherstation.subscribe(mobileapp)
weatherstation.subscribe(desktopapp)

weatherstation.set_weather("Sunny")

#now lets unsubscribe the desktop app from our observers







