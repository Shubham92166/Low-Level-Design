from abc import ABCMeta, abstractstaticmethod

class personInterface:

    @abstractstaticmethod
    def person_name(metaclass = ABCMeta):
        '''interface method implementation will be in child class'''
    
class student(personInterface):

    def __init__(self):
        self.name = "Default student name"

    def person_name(self):
        print("This is a student")

class teacher(personInterface):
    
    def __init__(self) -> None:
        self.name = "Deafult teacher name"

    def person_name(self):
        print("This is a teacher")


class personFactory:

    @staticmethod
    def build_person(personType):
        if personType == "student":
            return student()
        elif personType == "teacher":
            return teacher()
        print("Invalid person type")
        return -1

if __name__ == "__main__":
    choice = input("Enter the type of person:")
    person = personFactory.build_person(choice)
    person.person_name()
