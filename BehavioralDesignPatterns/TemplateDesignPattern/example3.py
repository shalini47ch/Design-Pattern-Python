from abc import ABC,abstractmethod

class WebApplicationFrameworkTemplate(ABC):
    #this is a template method
    def handle_request(self,request):
        self.authenticate(request)
        self.route_request(request)
        self.execute_business_logic(request)
        self.render_response(request)
    
    def authenticate(self,request):
        print("Authenticate the request")
    
    def route_request(self,request):
        print("Routing the request to the appropriate handler")
    
    @abstractmethod
    def execute_business_logic(self,request):
        pass
    
    def render_response(self,request):
        print("Rendering the response")

#creating two concrete implementation
class DjangoFramework(WebApplicationFrameworkTemplate):
    def execute_business_logic(self,request):
        print("Executing business logic using django")

#similarly do it for flask
class FlaskFramework(WebApplicationFrameworkTemplate):
    def execute_business_logic(self,request):
        print("Executing business logic using flask")

#now here at last we call the client code
djangoframework=DjangoFramework()
djangoframework.handle_request("GET/product")

print("*"*30)

#similarly do it for flask framework
flaskframework=FlaskFramework()
flaskframework.handle_request("POST/login")


    
        