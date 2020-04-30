import datetime
from person import Person


class Employee(Person):
    def __init__(self, firstName, lastName, id, adress, baseSalary: int, seniority: int, year: datetime.date):
        Person.__init__(self, firstName, lastName, id, adress, year)
        self.__baseSalary = baseSalary
        self.__seniority = seniority

    def get_salary(self):
        return self.__baseSalary

    def get_seniority(self):
        return self.__seniority

    def set_seniority(self, seniority):
        self.__seniority = seniority

    def set_salary(self, baseSalary):
        self.__baseSalary = baseSalary
