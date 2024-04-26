#in this example we will use the director as well
#here the product is created
class House:
    def __init__(self):
        #it has three parameters
        self.floor=None
        self.wall=None
        self.roof=None
    
    def __str__(self):
        return f"Floor {self.floor} \n "\
             f"Wall {self.wall} \n" \
             f"Roof {self.roof} \n "
             
#here we will now build a builder class
class HouseBuilder:
    def __init__(self):
        self.house=House()
    
    #now there are 3 options setfloor,setwall,setroof 
    def set_floor(self,amount):
        self.house.floor=amount
        return self 
    
    def set_wall(self,amount):
        self.house.wall=amount
        return self 
    def set_roof(self,amount):
        self.house.roof=amount
        return self
    
    def get_house(self):
        return self.house

#Here we will use the HouseBuilder as the abstract class and then build the small and the big houses on it

class SmallHouseBuilder(HouseBuilder):
    def build_floor(self):
        return self.set_floor("Small Floor")
    def build_wall(self):
        return self.set_wall("Small Wall")
    
    def build_roof(self):
        return self.set_roof("Small roof")
    

class BigHouseBuilder(HouseBuilder):
    def build_floor(self):
        return self.set_floor("Big Floor")
    def build_wall(self):
        return self.set_wall("Big Wall")
    
    def build_roof(self):
        return self.set_roof("Big roof")
    
#So this contractor class is the director class which decides the ordering in which our house will be constructed

class Contractor:
    def __init__(self,builder):
        self.builder=builder
        
    def construct_house(self):
        self.builder.build_floor()
        self.builder.build_wall()
        self.builder.build_roof()

if __name__=="__main__":
    #call for both smallhouse builder and bighouse builder
    small_builder=SmallHouseBuilder()
    big_builder=BigHouseBuilder()
    contractor=Contractor(small_builder)
    contractor.construct_house()
    small=small_builder.get_house()
    print("Small house:")
    print(small)
   
    
    
    

        






    

            
    