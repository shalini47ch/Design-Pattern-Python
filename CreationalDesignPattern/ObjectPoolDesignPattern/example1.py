#It is a type of creational design pattern that manages a pool or a cache of reusable objects,it is useful when the cost of object creation is high

#A pool of objects is created by the pool manager,whenever a new object is needed instead of creating it the pool manager chooses it from the pool of objects

#Real life usecases of object pool design pattern includes thread pool,database pool,connection pooling in web servers

#Terminologies for object pool design pattern include ObjectPool,Object,Pool Manager

class Object:
    def __init__(self,id):
        self.id=id
    
    def reset(self):
        pass

#now create another objectPoolManager
class ObjectPoolManager:
    def __init__(self,max_objects):
        self.max_objects=max_objects
        self.available_objects=[]
        self.in_use_objects=[]
        
        for i in range(max_objects):
            self.available_objects.append(Object(i))
    
    def acquire_object(self):
        #here we will first check for available objects
        if self.available_objects:
            obj=self.available_objects.pop()
            self.in_use_objects.append(obj)
            return obj
        else:
            raise Exception("No objects available in the pool")
    
    def release_obj(self,obj):
        obj.reset()
        self.in_use_objects.remove(obj)
        self.available_objects.append(obj)

pool=ObjectPoolManager(5)
obj1=pool.acquire_object()
obj2=pool.acquire_object()
print(obj1.id)
print(obj2.id)
        


    
    
    
    
    
    

