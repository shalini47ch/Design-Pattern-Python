#Create separate abstract classes called as Connection and the cursor and then create a factory to use them
from abc import ABC,abstractmethod

class Connection(ABC):
    @abstractmethod 
    
    def connect(self):
        pass
#now creating two subclasses
class MYSQLConnection(Connection):
    def connect(self):
        return "MySql connected successfully"

#similarly do it for PostGreSQL
class PostGreSQL(Connection):
    def connect(self):
        return "PostgreSQL connected successfully"
    
#similarly create for cursor
class Cursor(ABC):
    @abstractmethod
    def execute(self,query):
        pass
class MySQLQuery(Cursor):
    def execute(self,query):
        return f"Executing mysql query {query}"
    
#similarly do it for postgre sql
class PostGreSQLQuery(Cursor):
    def execute(self,query):
        return f"Executing postgres query {query}"

class AbstractFactoryMethod(ABC):
    @abstractmethod 
    def create_connection(self):
        pass
    @abstractmethod 
    def create_cursor(self):
        pass
class MySQLFactoryMethod(AbstractFactoryMethod):
    def create_connection(self):
        return MYSQLConnection()
    
    def create_cursor(self):
        return MySQLQuery()
#similarly create for PostGreSQLFactory

#Abstract factory helps us to group related factories together
class PostGreSQLFactory(AbstractFactoryMethod):
    def create_connection(self):
        return PostGreSQL()
    
    def create_cursor(self):
        return PostGreSQLQuery()

#now once the factories are implemented now the next one is to write the client code 
def client(factory:AbstractFactoryMethod):
    connection = factory.create_connection()
    cursor = factory.create_cursor()
    print(connection.connect())
    print(cursor.execute("SELECT * FROM table_name"))
    print()

print("Do for SQL")
client(MySQLFactoryMethod())
    