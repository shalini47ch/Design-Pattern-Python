from abc import ABC,abstractmethod 

class Logger(ABC): #this is Product
    @abstractmethod
    def log(self,message):
        pass
#now the next step is to create the subclasses of the logger called as ConsoleLogger,FileLogger and DatabaseLogger

class ConsoleLogger(Logger): #these are ConcreteProducts
    def log(self,message):
        #here this log will print the message
        print(f"[Console Logger] {message}")
    
class FileLogger(Logger):
    def log(self,message):
        print(f"[File Logger] {message}")
        
#now similarly creating another class called as DatabaseLogger

class DatabaseLogger(Logger):
    def log(self,message):
        print(f"[Database Logger] {message}")

#now similarly create a factory for this where we will call the consolelogger,databaselogger and filelogger
class LoggerFactory(ABC): #abstract factory class
    @abstractmethod
    def create_logger(self)->Logger:
        pass
#now creating factories for each 
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self)->Logger:
        return ConsoleLogger()
    
#similarly do it for file logger and databaselogger
class FileLoggerFactory(LoggerFactory):
    def create_logger(self)->Logger:
        return FileLogger()
    
class DatabaseLoggerFactory(LoggerFactory):
    def create_logger(self)->Logger:
        return DatabaseLogger()
## at last write the client code and call
def perform_logging(factory,message):
    logger=factory.create_logger()
    logger.log(message)

#doing it for the consolelogger
console=ConsoleLoggerFactory()
perform_logging(console,"This is the console logger")

#similarly do it for fileloggerfactory
filelogger=FileLoggerFactory()
perform_logging(filelogger,"This is the file logger")

#similarly do it for databaselogger
databaselogger=DatabaseLoggerFactory()
perform_logging(databaselogger,"This is the database logger")

#This is also an example of the factory design pattern


    
        


