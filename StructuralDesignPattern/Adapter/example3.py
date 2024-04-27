#Here  we will create a database adapter

#functionalities are insert,update,delete and select

class MYSQLDatabase: #this isthe adaptee
    def mysql_insert(self,data):
        print(f"Inserting data {data} into mysql database")
    
    def mysql_delete(self,data):
        print(f"deleting data {data} from mysql database")
          
    def mysql_update(self,data):
        print(f"updating data {data} into mysql database")
        
    def mysql_select(self,data):
        print(f"selecting data {data} from mysql database")
        
#similarly do it for PostgreSQL
class PostGreSQLDatabase: #this is also adaptee
    def postgre_insert(self,data):
        print(f"Inserting data {data} into postgre database")
    
    def postgre_delete(self,data):
        print(f"deleting data {data} from postgre database")
          
    def postgre_update(self,data):
        print(f"updating data {data} into postgre database")
        
    def postgre_select(self,data):
        print(f"selecting data {data} from postgre database")
        
#now creating a target class the type of which we need the implementation
class Database:
    def insert(self,data):
        pass
    def delete(self,data):
        pass
    def update(self,data):
        pass
    def select(self,data):
        pass
#at last we will create the adapter using these
class MySQLAdapter(Database):
    def __init__(self,adaptee):
        self.adaptee=adaptee
    
    def insert(self,data):
        self.adaptee.mysql_insert(data)
    
    def update(self,data):
        self.adaptee.mysql_update(data)
    
    def delete(self,data):
        self.adaptee.mysql_delete(data)
        
    def select(self,data):
        self.adaptee.mysql_select(data)
        
#similarly do it for postgresql

class PostGreSQLAdapter(Database):
    def __init__(self,adaptee):
        self.adaptee=adaptee
    
    def insert(self,data):
        self.adaptee.postgre_insert(data)
    
    def update(self,data):
        self.adaptee.postgre_update(data)
    
    def delete(self,data):
        self.adaptee.postgre_delete(data)

    def select(self,data):
        self.adaptee.postgre_select(data)
        
#now atlast create a client class that will use the adapter classes
mysql_adapter=MySQLAdapter(MYSQLDatabase())
mysql_adapter.insert("Record 1")
mysql_adapter.update("Record 1")
mysql_adapter.delete("Record 1")

#similarly do it for postgresqladapter
postgre_adapter=PostGreSQLAdapter(PostGreSQLDatabase())
postgre_adapter.insert("Record 2")
postgre_adapter.update("Record 2")
postgre_adapter.delete("Record 2")



        

    
        
    
    
        
        
    