from abc import ABC,abstractmethod

class WeatherStation:
    def __init__(self):
        self._observers=[]
        self._weather_data={}
    #now every observable will have three methods called as subscribe,unsubscribe and notify
    def attach(self,observer):
        self._observers.append(observer)
    
    def detach(self,observer):
        self._observers.remove(observer)
    
    def set_weather(self,temperature,pressure,humidity):
        self._weather_data["temperature"]=temperature
        self._weather_data["pressure"]=pressure
        self._weather_data["humidity"]=humidity
        self.notify()
    
    #similarly create a helper function called as notify
    def notify(self):
        for observer in self._observers:
            observer.update(self._weather_data)
            
#Observer 
class Observer(ABC):
    @abstractmethod
    def update(self,weather_data):
        pass
#we will create DisplayDevice and PrintDevice
class DisplayDevice(Observer):
    def __init__(self,name):
        self._name=name
    
    def update(self,weather_data):
       print(f"Sending to{self._name}")
       print(f"{weather_data['temperature']} Humidity: {weather_data['humidity']} Pressure: {weather_data['pressure']}")

      
class PrintDevice(Observer):
    def update(self,weather_data):
        print("Sending data to printer")
        for data in weather_data:
            print(f"{data}:{weather_data[data]}")
        
#here we will use the client code
weather_station=WeatherStation()
display1=DisplayDevice("Living room display")
display2=DisplayDevice("Bed room display")
print1=PrintDevice()
# here we will first attach the 
weather_station.attach(display1)
weather_station.attach(display2)
weather_station.set_weather(25,70,1000)
      

        

        