import datetime
import Person


class Employee:
    def __init__(self, firstName: str, lastName: str, id: str, adress,
                 baseSalary: int, seniority: int):
        super(Employee, self).__init__()
        self.__baseSalary = baseSalary
        self.__seniority = seniority
