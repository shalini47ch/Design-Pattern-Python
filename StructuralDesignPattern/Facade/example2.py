#Here we will consider the example of a computer system  with subsystems like cpu subsystem,memory subsystem,other subsystems into a facade called as computer
#this is one subsystem
class CPU:
    def freeze(self):
        print("CPU freeze")
    
    def jump(self,position):
        print(f"Jump to a specific position{position}")
        return position
    def execute(self):
        print("Executing the code")
        
#similarly creating another subsystem called as Memory
class Memory:
    def __init__(self):
        self.data={} #here we are declaring a hmap where we will store memory at a specific location
    
    def load(self,data,position):
        print(f"Loading data @{position}")
        self.data[position]=data
    #similarly write a helper function to get the data
    def get_data(self,position):
        print(f"Getting data at {position}")
        return self.data[position]
#now at last we will create the facade called as computer
class Computer:
    #here we will mix the functionalities of both the cpu and the memory subsystems
    def __init__(self):
        self.cpu=CPU()
        self.memory=Memory()
    
    #now there are two options that is run and retrieve
    def run(self,program):
        self.cpu.freeze()
        position=0
        for ele in program:
            self.memory.load(ele,position)
            self.cpu.jump(position)
            self.cpu.execute()
            position+=1
            print()
    #now similarly create one more helper called as retieve
    def retrieve(self,position):
        return self.memory.get_data(position)
#now at last call the client code
computer=Computer()
program=[2342,4553,444,"hello world",25332]
computer.run(program)
computer.retrieve(1)
        
        

