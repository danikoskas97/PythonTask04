import datetime


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

    def set_adress(self, adress):
        self.__adress = adress


class Employee(Person):
    def __init__(self, firstName: str, lastName: str, id: int, adress: str, baseSalary: int, seniority: int,
                 year: datetime.date):
        super().__init__(self, firstName, lastName, id, adress, year)
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


class Student(Person):
    def __init__(self, firstName, lastName, id, adress, year: datetime.date, courses: str):
        super().__init__(self, firstName, lastName, id, adress, year)
        self.__courses = courses

    def get_courses(self):
        return self.__courses

    @property
    def set_courses(self, courses):
        self.__courses = courses

    def get_year(self):
        return self.__year

    @property
    def set_year(self, year):
        self.__year = year

    def take_courses(self):
        ret = ''
        for course in self.__courses:
            ret += course + ', '
        print(f'{str(self)}\n course in year {self.__year}:\n')


class Lecturer(Person):
    def __init__(self, firstName: str, lastName: str, id: int, adress: str, year: datetime.date, rate_for_hour):
        super().__init__(self, firstName, lastName, id, adress, year)
        self.__rate_for_hour = rate_for_hour

    def get_rate_for_hour(self):
        return self.__rate_for_hour

    def set_rate_for_hour(self, rate_for_hour):
        self.__rate_for_hour = rate_for_hour


student1 = Student(firstName="Yoad", lastName="gadot", id=1233, adress="Tel-aviv", year=2020, courses=("Python", "Java"))
student2 = Student(firstName="Dani", lastName="Koskas", id=2313, adress="Raanana", year=2020, courses=("Python", "advanced algorithm"))
lecturer1 = Lecturer(firstName="gabi", lastName="rich", id=43600, adress="Eilat", year=2020, rate_for_hour=200)
