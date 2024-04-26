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

small_housebuilder=HouseBuilder()
small_housebuilder.set_floor(10).set_wall(5).set_roof(8)
smallhouse=small_housebuilder.get_house()
print(smallhouse)

print("*"*40)
#similarly do it for big house
big_housebuilder=HouseBuilder()
big_housebuilder.set_floor(20).set_wall(15).set_roof(10)
bighouse=big_housebuilder.get_house()
print(bighouse)




    

            
    