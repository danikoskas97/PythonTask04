import datetime
from person import Person

class Employee(Person):
    def __init__(self, firstName,lastName, id , adress, baseSalary: int, seniority: int, year:datetime.date):
        super(Employee,self).__init__(firstName,lastName,id,adress)
        self.__baseSalary = baseSalary
        self.__seniority = seniority

    def getSalary(self):
        return self.__baseSalary

    def getSeniority(self):
        return self.__seniority

    def setSeniority(self, seniority):
        self.__seniority = seniority

    def setSalary(self,baseSalary):
        self.__baseSalary = baseSalary