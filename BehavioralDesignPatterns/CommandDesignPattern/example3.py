#Here instead of doing the implementation in concrete command here we will create a separate receiver and perform the greeeting
#receiver
class Greet:
    def spanish(self):
        print("Hola")
    
    def english(self):
        print("Hello")
        
class Command:
    def __init__(self,greeting):
        self._greet=greeting
    
    def execute(self):
        pass
class Hello1(Command):
    def execute(self):
        self._greet.spanish()

#similarly do it for Hello2 command
class Hello2(Command):
    def execute(self):
        self._greet.english()

class Invoker:
    def __init__(self):
        self.commands=[]
    
    def set_command(self,command):
        self.commands.append(command)
    
    def execute_command(self):
        for command in self.commands:
            command.execute()
#now at last we call the client code
greet=Greet()
hello1=Hello1(greet)
hello2=Hello2(greet)
invoker=Invoker()
invoker.set_command(hello1)
invoker.set_command(hello2)
invoker.execute_command()



