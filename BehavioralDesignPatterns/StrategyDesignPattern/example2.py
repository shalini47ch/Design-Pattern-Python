#here we will apply strategy design pattern in the payment processing code
from abc import ABC,abstractmethod
#this is the strategy
class PaymentStrategy(ABC):
    @abstractmethod 
    def pay(self,amount):
        pass

#now creating two separate concrete strategies 
class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self,card_number,expiry_date,cvv):
        self.card_number=card_number
        self.expiry_date=expiry_date
        self.cvv=cvv
    
    def pay(self,amount):
        print(f"Processing credit card payment of amount {amount} with card number {self.card_number}")

#similarly create another concrete class called as PaypalPaymentStrategy
class PayPalPaymentStrategy(PaymentStrategy):
    def __init__(self,email,password):
        self.email=email
        self.password=password
    
    def pay(self,amount):
        print(f"Processing paypal payment of amount {amount} with email {self.email}")
#now here we will create the context

class PaymentProcesser:
    def __init__(self,payment_strategy):
        self.payment_strategy=payment_strategy
    
    def set_payment_strategy(self,payment_strategy):
        self.payment_strategy=payment_strategy
    
    def make_payment(self,amount):
        self.payment_strategy.pay(amount)
creditcard=CreditCardPaymentStrategy(123,23,345)
paypal=PayPalPaymentStrategy("abc@gmail.com","abc@123")
context=PaymentProcesser(creditcard)
context.make_payment(200)
context.payment_strategy=paypal
context.make_payment(500)



