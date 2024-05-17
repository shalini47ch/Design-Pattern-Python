#here we will create a separate menu item and menu and it will represent a tree like structure and here we will use the composite design pattern
#here the first class will that be of the component
class Menu:
    def __init__(self,name):
        self.name=name
    
    def ls(self):
        print(self.name)

#the other one will be the composite
class MenuItem:
    def __init__(self,name):
        self.name=name
        self.items=[] #this will store the list of items
    
    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self,item):
        self.items.remove(item)
    
    def ls(self):
        print(self.name)
        for item in self.items:
            item.ls()
#create menu items
item1=Menu("item1")
item2=Menu("item2")
item3=Menu("item3")

#now here we create a menulist
menu1=MenuItem("menu1")
menu2=MenuItem("menu2")

menu1.add_item(item1)
menu1.add_item(menu2)
menu2.add_item(item2)
menu2.add_item(item3)
menu1.ls()
        