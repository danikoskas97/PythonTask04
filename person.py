import datetime

class Person:

    def __init__(self, firstName: str, lastName: str, id: int, adress: str):
        self.__name = firstName
        self.__lastName = lastName
        self.__id = id
        self.__adress = adress


    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name


Person.a = "alex"
Person.a = "gilad"
print(Person.a)
