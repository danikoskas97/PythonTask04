import datetime
from lecturer import Lecturer
from student import Student

class Person:

    def __init__(self, firstName: str, lastName: str, id: int, adress: str, year: datetime.date):
        self.__name = firstName
        self.__lastName = lastName
        self.__id = id
        self.__adress = adress
        self.__year = year

    def get_name(self):
        return self.__name

    def set_name(self, firstName):
        self.__name = firstName

    def get_last_name(self):
        return self.__lastName

    def set_last_name(self, lastName):
        self.__lastName = lastName

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_adress(self):
        return self.__adress

    def set_adress(self,adress):
        self.__adress = adress


student1 = Student("yoad", "gadot", 1233, "Tel-aviv", ("Python", "Java"), 2020)
sudent2 = Student("Dani","Koskas",2313,"Raanana", ("Python", "advanced algorithme"), 2020)
lecturer1 = Lecturer("gab","rich",43600, "eilat", ("Python", "advanced algorithme"), 2020)

