#here in case of factory design pattern we will not create a separate creator instead create a separate class
from abc import ABC,abstractmethod
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
    
#creat a database factory and store the 
class DatabaseFactory:
    #here we will create a dictionary to store the database types
    def __init__(self):
        self.factory=dict(mysql=MYSQL,postgres=PostGreSQL,oracle=Oracle)
    def create_connection(self,db_name):
        if db_name in self.factory:
            connection=self.factory.get(db_name)()
            return connection
db_factory=DatabaseFactory()
mysql=db_factory.create_connection("mysql")
print(mysql.connect())

# #similarly do it for postgres and then oracle 
postgresql=db_factory.create_connection("postgres")
print(postgresql.connect())

oracle=db_factory.create_connection("oracle")
print(oracle.connect())



