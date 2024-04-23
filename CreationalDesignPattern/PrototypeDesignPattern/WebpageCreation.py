#here first create the class of the object to prototype
import copy
class Webpage:
    def __init__(self,header=None,content=None,footer=None):
        #it has three parts header content and footer
        self.header=header
        self.content=content
        self.footer=footer 
    
    def page(self):
        return f"{self.header} {self.content} {self.footer}"

class Prototype:
    def __init__(self):
        self._pages={} #this is the hmap where we will store the dictionary of all the object types
    
    #now there are three helper functions you need to put 
    def register_page(self,name,obj):
        self._pages[name]=obj
    
    #now the next function is to unregister_obj
    def unregister_page(self,name):
        del self._pages[name]
    #this create_page is actually the clone function
    def clone(self,name,**attr):
        #**attr are those which help us to add extra parameters 
        webpages=copy.deepcopy(self._pages.get(name))
        webpages.__dict__.update(attr)
        return webpages
        
if __name__=="__main__":
    proto=Prototype()
    wb=Webpage(header="<div>Header component </div>",content="<div>Content Component",footer="<div>Footer Component</div>")
    proto.register_page("webpage",wb)
    modified=proto.clone("webpage",content="<div>Modified Content</div>")
    print("Original page",wb.page())
    print("Modified page",modified.page())
    
    
    