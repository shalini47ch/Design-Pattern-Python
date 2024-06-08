#here we will first create an interface called as Command
class Command:
    def execute(self):
        pass

#this is a concrete command
class HelloCommand(Command):
    def execute(self):
        print("Hello Command Pattern")

#now here we will create an invoker that helps to invoke the commands

class Invoker:
    def __init__(self):
        self.command=None
    
    #now create two helper functions called as set_command and execute_command
    def set_command(self,command):
        self.command=command
    
    def execute_command(self):
        self.command.execute()

hello_command=HelloCommand()
invoker=Invoker()
invoker.set_command(hello_command)
invoker.execute_command()

        
    
    

