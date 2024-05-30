#Here we will add the aggregator along with the iterator
#here it has the iterator logic
class MyCollectionIterator:
    def __init__(self,iterable):
        self.iterable=iterable
        self.index=0
    #now create two helper function for this iterator one is the hasnext() and the other is the next() method
    
    def has_next(self):
        return self.index<len(self.iterable)
    
    def __next__(self):
        if(self.has_next()):
            item=self.iterable[self.index]
            self.index+=1
            return item
#this part has the aggregator logic
class MyCollection:
    def __init__(self):
        self.data=[]
    
    def add_item(self,item):
        self.data.append(item)
    
    def create_iterator(self):
        return MyCollectionIterator(self.data)

collection=MyCollection()
collection.add_item("Item1")
collection.add_item("Item2")
collection.add_item("Item3")
iterator=collection.create_iterator()
#now we will iterator through the itertor
while iterator.has_next():
    item=iterator.__next__()
    print(item)



        
        