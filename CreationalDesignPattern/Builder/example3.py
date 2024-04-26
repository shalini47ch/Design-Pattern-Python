#Here we will create a Sandwich using the builder design pattern
#Here sandwich isthe product and now we will build a builder and add concrete builder and then create a director class that will decide the order in which we will make our sandwich
class Sandwich:
    def __init__(self):
        self._bread=None
        self._potato=None
        self._cheese=None
        self._vegetables=[]
        self._sauces=[]
    
    #now here create a dunder string 
    def __str__(self):
        ingredients="Bread"+self._bread+"|Potato"+self._potato
        if self._cheese:
            ingredients+="|Cheese"+self._cheese
        #now here we will add the vegetables and sandwiches together
        ingredients+="|Vegetables"+",".join(self._vegetables)
        #similarly add the sauces as well
        ingredients+="|Sauces"+",".join(self._sauces)
        return ingredients
#this is basically an abstract class      
class SandwichBuilder:
    def __init__(self):
        self.sandwich=Sandwich()
    #now here we will create different methods for building the sandwich
    
    def add_bread(self):
        pass
    
    def add_potato(self):
        pass
    
    def add_cheese(self):
        pass
    
    def add_vegetables(self):
        pass
    
    def add_sauces(self):
        pass
    def get_sandwich(self):
        return self.sandwich
    
#now we will create different sandwich builders
class ClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread="Milk Bread"
    
    def add_potato(self):
        self.sandwich._potato="Baby Potato"
    
    def add_cheese(self):
        self.sandwich._cheese="Cottage Cheese"
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("tomato")
        self.sandwich._vegetables.append("lettuce")
    #similarly create a function to add the sauces 
    def add_sauces(self):
        self.sandwich._sauces.append("red sauce")
        self.sandwich._sauces.append("white sauce")

class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread="Brown Bread"
    
    def add_potato(self):
        self.sandwich._potato="Big Potato"
    
    def add_vegetables(self):
        self.sandwich._vegetables.append("cabbage")
        self.sandwich._vegetables.apppend("cauliflower")
    
    def add_sauces(self):
        self.sandwich._sauces.append("pink sauce")
        self.sandwich._sauces.append("white sauce")
    

class Waiter:
    def __init__(self):
        self.sandwich_builder=None
        
    def get_builder(self,builder):
        self.sandwich_builder=builder
    
    def create_sandwich(self):
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_potato()
        self.sandwich_builder.add_vegetables()
        self.sandwich_builder.add_sauces()
#now atlast create a main method 
if __name__=="__main__":
    club_builder=ClubSandwichBuilder()
    veggie_builder=VeggieSandwichBuilder()
    waiter=Waiter()
    waiter.get_builder(club_builder)
    waiter.create_sandwich()
    club=club_builder.get_sandwich()
    print("Club sandwich")
    print(club)
    
        
        

    

            