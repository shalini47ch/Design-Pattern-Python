#here we will create different types of document using the factory design pattern
from abc import ABC,abstractmethod

class Document(ABC): #this is the Product
    @abstractmethod
    def open(self):
        pass
#now create three Document types like PDF ,Word and Html
class WordDocument(Document): #these all are product factories
    def open(self):
        print("opening the word file")
#similarly do it for pdf and for html

class PDFDocument(Document):
    def open(self):
        print("opening the pdf file")
#similarly create it for the html file 

class HTMLDocument(Document):
    def open(self):
        print("Opening the html document")

class DocumentFactory(ABC): #this is the creator
    @abstractmethod
    def create_document(self):
        pass
class WordDocumentFactory(DocumentFactory): #concreteCreatorA
    def create_document(self)->Document:
        return WordDocument()
#similarly create the pdfdocumentFactory and Htmldocumentfactory

class PDFDocumentFactory(DocumentFactory): #concreteCreatorB
    def create_document(self)->Document:
        return PDFDocument()
#similarly create for HTMLDocument factory
class HTMLDocumentFactory(DocumentFactory): #concreteCreatorC
    def create_document(self)->Document:
        return HTMLDocument()

#once the creators are made now the next one is to call the client method
def process_document(factory:Document):
    document=factory.create_document()
    document.open()

word_factory=WordDocumentFactory()
process_document(word_factory)

#similarly do it for pdf file and html file 
pdf_factory=PDFDocumentFactory()
process_document(pdf_factory)

#next do it for htmldocument factory

html_factory=HTMLDocumentFactory()
process_document(html_factory)



    
    
