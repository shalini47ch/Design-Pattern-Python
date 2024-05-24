#here we will use the chain of responsibility for handling 3 different types of events like mousevent,clickevent,keypresshandler
from abc import ABC,abstractmethod

class Event:
    def __init__(self,event_type):
        self.event_type=event_type
    
#now here we will create an abstract class called as eventhandler
class EventHandler(ABC):
    def __init__(self,successor=None):
        self.successor=successor
    
    @abstractmethod
    def handle_event(self,event):
        pass

#now here creating for MouseEvent,ClickEvent
class ClickHandler(EventHandler):
    def handle_event(self,event):
        if(event.event_type=="click"):
            print("Click event handled by click handler")
        elif self.successor is not None:
            self.successor.handle_event(event)

class MouseMoveHandler(EventHandler):
    def handle_event(self,event):
        if(event.event_type=="mouse_move"):
            print("Mouse move handled by mouse move handler")
        elif self.successor is not None:
            self.successor.handle_event(event)
#now similalry create one more handler called as KeyPressHandler
class KeyPressHandler(EventHandler):
    def handle_event(self,event):
        if(event.event_type=="key_press"):
            print("Key press handled by keypresshandler")
        elif self.successor is not None:
            self.successor.handle_event(event)
        else:
            print("Click handling event terminated")


clickhandler=ClickHandler()
mousemove=MouseMoveHandler()
keypress=KeyPressHandler()

clickhandler.succesor=mousemove
mousemove.succesor=keypress

events=[Event("click"),
        Event("button_click"),
        Event("key_press"),
        Event("button_click")
]
#iterate through the events
for event in events:
    keypress.handle_event(event)
        

