#Database query execution
from abc import ABC,abstractmethod

class DatabaseQueryExecutionTemplate(ABC):
    #here we will first create a template method
    def execute_query(self,query):
        self.connect_to_database()
        result=self.run_query(query)
        self.process_result(result)
        self.disconnect_from_database()
    
    #only the run query is abstractmethod other all are hook methods what are the default ones 
    
    def connect_to_database(self):
        print("Connecting to the database")
    
    @abstractmethod
    def run_query(self,query):
        pass
    
    #similarly create two helper functions called as process results and disconnecting from database
    def process_result(self,result):
        print("Processing results:",result)
    
    def disconnect_from_database(self):
        print("Disconnecting from database")
    
class MySQLQueryExecution(DatabaseQueryExecutionTemplate):
    
    def run_query(self,query):
        print("Executing MYSQL query:",query)
        return {
            "customerid":12456,
            "name":"Banky",
            "discount":False
        }
    
    def process_result(self,result):
        print("Processing mysql query result:",result)
        
#similarly doing it for PostGresqlexecution

class PostGreQueryExecution(DatabaseQueryExecutionTemplate):
    def run_query(self,query):
        print("Executing PostGre query:",query)
        return {
            "productid":"PIO9",
            "name":"laptop",
            "total":200 
        }
    
    def process_result(self,result):
        print("Processing postgre query result:",result)

mydatabasequery1=MySQLQueryExecution()
mydatabasequery1.execute_query("SELECT * FROM CUSTOMERS")

print("*"*30)
mydatabasequery2=PostGreQueryExecution()
mydatabasequery2.execute_query("SELECT * FROM PRODUCTS")

    
    
    