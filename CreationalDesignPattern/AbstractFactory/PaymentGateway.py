#here also we will first create the abstract factory of the different types of prodicts that we need and will put its implementation and then create an abstractfactory to use them
from abc import ABC,abstractmethod 

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
#now create different methods that you will have
class CreditCard(PaymentMethod):
    def make_payment(self,amount):
        return f"Amount of {amount} paid by Credit Card"
    
#now similarly do it for other payment methods
class DebitCard(PaymentMethod):
    def make_payment(self,amount):
        return f"Amount of {amount} paid by debit card"
    
#do it for UPI And NetBanking
class UPI(PaymentMethod):
    def make_payment(self,amount):
        return f"AMount of {amount} paid by UPI"
    
class NetBanking(PaymentMethod):
    def make_payment(self,amount):
        return f"AMount of {amount} paid by Netbanking"
    
#once all the implementation of PaymentMethod is done now create a factory on the type of countries
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self,payment_method):
        pass
    
class UsPaymentMethod(PaymentFactory):
    def __init__(self):
        self.payments=dict(credit=CreditCard,debit=DebitCard,Upi=UPI,Netbanking=NetBanking)
    
    def create_payment(self,payment_method):
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
        
class CanadaPaymentMethod(PaymentFactory):
    def __init__(self):
        self.payments=dict(credit=CreditCard,debit=DebitCard)
        
    def create_payment(self,payment_method):
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
        
class IndiaPaymentMethod(PaymentFactory):
    def __init__(self):
        self.payments=dict(credit=CreditCard,debit=DebitCard,upi=UPI)
        
    def create_payment(self,payment_method):
        if payment_method in self.payments:
            return self.payments.get(payment_method)()
    
#now create the client method where we will use all these factories
class Client:
    def __init__(self):
        self.factory=None  
    
    def get_factory(self):
        country_factory=dict(us=UsPaymentMethod,india=IndiaPaymentMethod,
                             canada=CanadaPaymentMethod)
        flist=",".join(country_factory)
        while not self.factory:
            #till the factory does not have any value ask the user to enter the payment type they want
            country=input(f"Enter country payment({flist:})")
            if country in country_factory:
                #here we will obtain it from the factory
                self.factory=country_factory.get(country)()
                break 
            #and if it is not the case then print 
            print("You need to enter the following countries ({flist})")
    def make_payment(self, payment_method, amount):
        if not self.factory:
            print("Please select a country factory first.")
            return None

        # Create the payment method based on the selected factory
        payment = self.factory.create_payment(payment_method)
        if payment:
            return payment.make_payment(amount)
        else:
            print("Invalid payment method.")
            return None
        
client = Client()
client.get_factory()

payment_method = input("Enter payment method (credit/debit/upi/netbanking): ")
amount = float(input("Enter payment amount: "))

result = client.make_payment(payment_method.lower(), amount)
if result:
    print(result)
            
            
    
    

