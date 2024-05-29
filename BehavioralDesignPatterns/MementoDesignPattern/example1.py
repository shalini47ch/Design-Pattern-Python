#It is a type of behavioral design pattern that captures an object internal state without violating encapsulation,this encapsulation is achived using access modifiers like public private protected

#It allows an object to be restored to its previous states promoting undo and redo operation

#Some real life scenarios where memento design pattern is used are text editors where they have the undo functionalities in other words the state can be persisited,web form data also uses memento design pattern,document editing applications like google docs,flight booking systems also use the memento design pattern

#Some terminologies related to memento design pattern originator,memento
#Originator is the one whose state is being saved whereas memento is the one which stores the saved state of the originator,memento is read only,Caretaker and then followed by the states

class Editor:
    def __init__(self):
        self.content=""
    
    def add_text(self,text):
        #this function will help us to add text to the content
        self.content+=text
    
    def get_content(self):
        return self.content
    
    #now to store the states of our text editor we will need the memento one is the create memento and the other is the restore_memento
    def create_memento(self):
        return Memento(self.content)
    
    def restore_memento(self,memento):
        self.content=memento.get_saved_content()
        
class Memento:
    def __init__(self,content):
        self.saved_content=content
    
    #now creating a helper function to get the saved memento
    def get_saved_content(self):
        return self.saved_content
#now creating a care taker class to store the list of mementos
class Caretaker:
    def __init__(self):
        self.mementos=[]
    
    def add_memento(self,memento):
        self.mementos.append(memento)
    #to get the lasr state of the memento use the getmemento
    def get_memento(self,index):
        return self.mementos[index]

#here writing the main client code
editor=Editor()
caretaker=Caretaker()
editor.add_text("Hello,")
caretaker.add_memento(editor.create_memento())
print()
editor.add_text("World")
caretaker.add_memento(editor.create_memento())
print()
editor.add_text("Goodbye")
print(editor.get_content())
editor.restore_memento(caretaker.get_memento(1))
print(editor.get_content())





    
    
        







