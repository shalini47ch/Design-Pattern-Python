#here instead of the previous example where we used only a single command here we will store a list of commands
#Here this is an example of command design pattern with multiple commands


class Command:
    def execute(self):
        pass
#create two concrete commands HelloCommand1 and HelloCommand2
class Hello1(Command):
    def execute(self):
        print("Hello,command pattern 1")

class Hello2(Command):
    def execute(self):
        print("Hello,command pattern 2")

#similarly implement command3

class Hello3(Command):
    def execute(self):
        print("Hello,command pattern 3")

class Invoker:
    def __init__(self):
        self.commands=[] #this will store a list of commands
    
    def set_command(self,command):
        self.commands.append(command)
    
    def execute_command(self):
        for command in self.commands:
            command.execute()
#CLient
hello1=Hello1()
hello2=Hello2()
hello3=Hello3()
invoker=Invoker()
invoker.set_command(hello1)
invoker.set_command(hello2)
invoker.set_command(hello3)
invoker.execute_command()

