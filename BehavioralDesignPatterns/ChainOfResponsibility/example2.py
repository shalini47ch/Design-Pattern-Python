class Request:
    def __init__(self,amount):
        self.amount=amount 

class Handler:
    def __init__(self,successor=None):
        self.successor=successor
    
    def handle_request(self,request):
        pass

#we are creating for an organization chart having Manager,Director and CEO
class Manager(Handler):
    def handle_request(self,request):
        if(request.amount<=1000):
            print("Manager approves the request of the amount",request.amount)
        elif(self.successor is not None):
            self.successor.handle_request(request)

class Director(Handler):
    def handle_request(self,request):
        if(request.amount<=10000):
            print("Director approves the request of the amount",request.amount)
        elif(self.successor is not None):
            self.successor.handle_request(request)

class CEO(Handler):
    def handle_request(self,request):
        if(request.amount<=20000):
            print("Ceo approves the request of  the amount",request.amount)
        elif(self.successor is not None):
            self.successor.handle_request(request)
        else:
            print("Request approval limit exceeded")

request=Request(3000)
manager=Manager()
director=Director()
ceo=CEO()

manager.successor=director
manager.director=ceo

manager.handle_request(request)






    

    