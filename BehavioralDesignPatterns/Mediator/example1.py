#Mediator design pattern is a behavioral design pattern that promotes loose coupling between objects and acts as a mediator so that two objects can interact indirectly
#It reduces the dependecies and promotes flexibility

#Real life scenarios where mediator design pattern is applied are air traffic control systems where the traffic system acts as a mediator which will receive signals for other aircrafts

#Chat application also follows the mediator design pattern,Smart home application system also uses the mediator design pattern

class AirTrafficControlMediator:
    def __init__(self):
        self.aircrafts=[]
    
    def register_aircrafts(self,aircraft):
        self.aircrafts.append(aircraft)
    #similarly create a helper function to notify aircraft
    def notify_aircraft(self,sender,message):
        #iterate through the given list of aircrafts
        for aircraft in self.aircrafts:
            if(aircraft!=sender):
                aircraft.receive_message(message)

#now here we will implement the aircrafts which will use the mediator
class Aircraft:
    def __init__(self,callsign,mediator):
        self.callsign=callsign
        self.mediator=mediator
    
    def send_message(self,message):
        self.mediator.notify_aircraft(self,message)
    
    def receive_message(self,message):
        print(f"Aircraft {self.callsign} received message:{message}")

mediator=AirTrafficControlMediator()

aircraft1=Aircraft("Flight123",mediator)
aircraft2=Aircraft("Flight234",mediator)
aircraft3=Aircraft("Flight345",mediator)
#here we will register the aircrafts
mediator.register_aircrafts(aircraft1)
mediator.register_aircrafts(aircraft2)
mediator.register_aircrafts(aircraft3)
aircraft1.send_message("Traffic advisory:Descend to 10,000 feet")


        
        
        

