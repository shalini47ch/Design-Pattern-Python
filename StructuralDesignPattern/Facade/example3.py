#Online store having subsystems like Product,Inventory,Payment and the facade is Online Store

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

#similarly create an inventory
class Inventory:
    def __init__(self):
        self.products=[]
    
    def add_product(self,product):
        self.products.append(product)
    
    def remove_product(self,product):
        self.products.remove(product)
    def get_product(self):
        return self.products
    
class Payment:
    def __init__(self):
        self.total=0
    
    def add_product(self,product):
        self.total+=product.get_price()
    
    def remove_product(self,product):
        self.total-=product.get_price()
        
    def get_total(self):
        return self.total


#this is the facade which will be the single point with all the functionality in one
class OnlineStore:
    def __init__(self):
        self.inventory=Inventory()
        self.payment=Payment()
    
    def add_product_tocart(self,name,price):
        product=Product(name,price)
        self.inventory.add_product(product)
        #similarly add it to the patment as well
        self.payment.add_product(product)
    
    def remove_product_fromcart(self,name):
        products=self.inventory.get_total()
        for product in products:
            if self.product.get_name()==name:
                self.inventory.remove(product)
                self.payment.remove(product)
                break
    
    def checkout(self):
        total=self.payment.get_total()
        print(f"The total amount is {total}")

#client
if __name__=="__main__":
    store=OnlineStore()
    store.add_product_tocart("Shirt",20)
    store.add_product_tocart("Trousers",40)
    store.add_product_tocart("Sneekers",80)
    store.checkout()
    
#This design pattern simplifies a complex system by providing a simple interface
#Improves maintainability but reducing the coupling between the systems by creating a facade
#Loose coupling and abstraction
#Increases reusability

#Disadvantages
#Limits flexibility because if we need to add more fuctionality to our system which are not present in facade so it would be an issue
#The other disadvantage of facade design pattern is that it causes performance issues


    
    
    
    
    
        