#here instead of creating separate classeswe can clone the existing classes  
import copy
class Square:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
        
#now we will create a prototype class where we will do the following functionalities
class Prototype:
    #here we will have options like register,unregister,clone 
    def __init__(self):
        self._obj={} #this is a dictionary in which various instances will be stored 
        
    def register_obj(self,name,obj):
        self._obj[name]=obj 
        
    def unregister_obj(self,name):
        del self._obj[name]
    
    def clone(self,name,**attr):
        #here attr will help us to create others
        obj=copy.deepcopy(self._obj.get(name))
        obj.__dict__.update(attr)
        return obj

if __name__=="__main__":
    sq=Square(10,20)
    proto=Prototype()
    #now the register_obj
    proto.register_obj("square",sq)
    #now next create a clone 
    rec=proto.clone("square",x=100,y=200)
    print("SQUARE",sq.__dict__,"RECTANGLE",rec.__dict__)
    bigrec=proto.clone("square",x=400,y=500)
    print("BigRectangle",bigrec.__dict__)