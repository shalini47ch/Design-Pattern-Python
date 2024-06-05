#Singleton design pattern is a creational design pattern that ensures that a class has only one instance and provides global point of access to it.

#It is used for objects that needs to be shared amongst the entire application

#Real life scenarios where it can be used are database connectivity,configuration settings

#Singleton class can help us to manage the pool of threads where only one instance of the thread pool exists and others

#Singleton,Instance,getInstance,_instance
class Singleton:
    __instance=None
    
    #create a static method that will call the init method of singleton
    @staticmethod
    def getInstance(name):
        
        if Singleton.__instance==None:
            #here since the instance is None so a new instance is created
            Singleton(name)
        return Singleton.__instance
    
    def __init__(self,name):
        self.name=name
        if Singleton.__instance is not None:
            raise Exception("Instance already exists")
        Singleton.__instance=self
        
s1=Singleton.getInstance("Boy")
s2=Singleton.getInstance("Girl")
print(s1,s2)
print(s1 is s2)
print(f"s1:{s1.name} s2:{s2.name}")
#Singleinstance s1 is created and all are referring to the same instance

        