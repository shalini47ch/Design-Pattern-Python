#This design pattern is mainly used to separate the traversal logic from the container logic making the code more flexible

#Real word use cases where this can be used are iterating over a database result set,file system,social media streams generally contain a list of posts,menu navigation

#Music playlist management system also uses the iterator design pattern,having different playlists song lists

#Components for iterator design pattern which includes methods like next(),hasNext(),reset(),it provides a common way to iterate over the objects regardless of the container

#ConcreteIterator is the implementation of the iterator

#Aggregate is the one which holds collection of elements,ConcreteAggregater is the implementation of the aggregate

class MyIterator:
    def __init__(self,iterable_data):
        self.iterable=iterable_data
        self.index=0
    
    #each iterator has two functions called as __next__ and __iter__
    def __next__(self):
        #this is same as that if the traversal 
        if(self.has_next()):
            item=self.iterable[self.index]
            self.index+=1
            return item
        else:
            raise StopIteration
        
    #similarly create a helper function to perform has_next()
    def has_next(self):
        return self.index<len(self.iterable)
        
    
    def __iter__(self):
        return self

if __name__=="__main__":
    lst=["Sola","Deji","Maxwell","Simon"]
    iterator=MyIterator(lst)
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.has_next())
    # print(iterator.__iter__())

    
        
        





