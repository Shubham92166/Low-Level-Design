from abc import abstractstaticmethod, abstractmethod, ABCMeta

class Person_Interface(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def printData():
        '''implementation will be in child class'''
    
class personSingleton(Person_Interface):

    __instance = None

    @staticmethod
    def get_instance():
        if personSingleton.__instance == None:
            personSingleton("Default", 0)

        return personSingleton.__instance
    
    def __init__(self, name, age):
        if self.__instance != None:
            raise Exception("Person class can have only one instance")
        
        self.name = name
        self.age = age
        personSingleton.__instance = self
