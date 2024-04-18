from abc import ABC,abstractmethod

#for the factory method design pattern here we will use it for database connectivity

#mysql,postgres and oracle

#Product
class DatabaseConnection(ABC):
    @abstractmethod 
    def connect(self):
        pass

#ConcreteProduct
class MYSQL(DatabaseConnection):
    def connect(self):
        return "Connected to MYSQL successfully"
    
class PostGreSQL(DatabaseConnection):
    def connect(self):
        return "Connected to PostGreSQL successfully"
    
class Oracle(DatabaseConnection):
    def connect(self):
        return "Connected to Oracle successfully"

#Creator 
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self)->DatabaseConnection:
        pass
#ConcreteCreator  
class MYSQLFactory(DatabaseConnectionFactory):
    def create_connection(self)->DatabaseConnection:
        return MYSQL()

class PostGreSQLFactory(DatabaseConnectionFactory):
    def create_connection(self)->DatabaseConnection:
        return PostGreSQL()

#similarly do it for Oracle
class OracleFactory(DatabaseConnectionFactory):
    def create_connection(self)->DatabaseConnection:
        return Oracle()
#Client
def connection_handler(factory):
    ele=factory.create_connection()
    print(ele.connect())
#do it for mysql oracle and postgresql

mysqlfactory=MYSQLFactory()
connection_handler(mysqlfactory)

#similarly do it for postgresql and oracle

oracle=OracleFactory()
connection_handler(oracle)

postgres=PostGreSQLFactory()
connection_handler(postgres)

#so this is the implementation of factory method design pattern

#In the factory method implementation we need to create the creator and then create the subclasses called as concreteCreators and  then use them in our clien code

#but in case of factory design pattern we dont creator the abstract class called as creator instead we create a class and use dictionary and then directly call the client code

