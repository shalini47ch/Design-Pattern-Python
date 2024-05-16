#Composite design pattern is a structural design pattern that allows clients to treat individual objects uniformly
#It can delegate the tasks to one or more child components and thus they can behave as a single unit

#Some common usecases of composite design patterns include filesystem in which there are files and subdirectories and which can also have files and subdirectories within it,organizational charts also follow the composite design pattern in which the employees act as the leaf nodes,music player may consist of several playlists and songs.
#Menu systems can also use the composite design pattern and can have menus and submenus

#Terminologies Component is the one which is the abstract class,leaf is the one which doesnt have any other children and it is the simple implementation,composite is the complex implementation and the last one is the client
#this is the abstract class whose implementation
class Component:
    def __init__(self,name):
        self.name=name
        
    def operation(self):
        print(f"{self.name}:Performing operation")

#now here we will have two composites means the complex implementation
class Composite:
    def __init__(self,name):
        self.name=name
        self.children=[]
    
    def add(self,component):
        #here we will add a component
        self.children.append(component)

    def remove(self,component):
        self.children.remove(component)
        
    def operation(self):
        print(f"{self.name}:Perform operation")
        for child in self.children:
            child.operation()
#now here writing the client code
leaf1=Component("leaf1")
leaf2=Component("leaf2")
#now here calling for the composite
composite1=Composite("Composite 1")

composite1.add(leaf1)
composite1.add(leaf2)
composite1.operation()

composite2=Composite("Composite 2")
composite2.add(Component("leaf3"))
composite2.add(Component("leaf4"))
composite2.operation()
        

