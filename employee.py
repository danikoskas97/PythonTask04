import datetime
from person import Person

class Employee(Person):
    def __init__(self, baseSalary: int, seniority: int):
        super().__init__(name=firstName)
        self.__baseSalary = baseSalary
        self.__seniority = seniority
