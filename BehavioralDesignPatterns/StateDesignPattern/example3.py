#Example using the light traffic system
#here alao we will have two things one is the state and the other is the context

from abc import ABC,abstractmethod 
#states
class TrafficLightState(ABC):
    @abstractmethod
    def display_light(self):
        pass

    @abstractmethod 
    def change_light(self,traffic_light):
        pass
#now we will have the redlight,greenlight and the yellow light state
class RedState(TrafficLightState):
    def display_light(self):
        return "Red"
    
    def change_light(self,traffic_light):
        print("Change from Red to Green State")
        traffic_light.state=GreenState()
#now similarly create it for greenState
class GreenState(TrafficLightState):
    def display_light(self):
        return "Green"
    def change_light(self,traffic_light):
        print("Change from green to yellow light")
        traffic_light.state=YellowState()
    
class YellowState(TrafficLightState):
    def display_light(self):
        return "Yellow"
    
    def change_light(self,traffic_light):
        print("Change from yellow to red")
        traffic_light.state=RedState()
#here we will create a context

class TrafficLight:
    def __init__(self):
        self.state=RedState()
    
    def display_light(self):
        return self.state.display_light()
    
    def change_light(self):
        self.state.change_light(self)

traffic=TrafficLight()
print(traffic.display_light())
print()
traffic.change_light()
print(traffic.display_light())


        
        