#state draft->review->finalize->publish

#aur aise hi context hai to pehle context banaenge
from abc import ABC,abstractmethod
#this is the abstract class for the state
class DocumentState(ABC):
    @abstractmethod
    def process_document(self,document):
        pass
class DraftState(DocumentState):
    def process_document(self,document):
        print("Processing document in the draft state")
        #this lines helps us to know the next state in which we need to move
        document.state=ReviewState()
    
class ReviewState(DocumentState):
    def process_document(self,document):
        print("Processing document in the review state")
        #this lines helps us to know the next state in which we need to move
        document.state=FinalizeState()
#similarly create the concrete class for the finalize and publish state
class FinalizeState(DocumentState):
    def process_document(self,document):
        print("Processing document in the finalize state")
        document.state=PublishState()
    
#now the last state is the publish state
class PublishState(DocumentState):
    def process_document(self,document):
        print("Document already published")

#here we will first create the context part whose functionality changes according to the state
class Document:
    def __init__(self):
        self.state=DraftState()
    
    def process(self):
        self.state.process_document(self)
document=Document()
document.process()
document.process()
document.process()
document.process()