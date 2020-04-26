import datetime
from person import Person


class Student(Person):
    def __init__(self, firstName, lastName, id, adress, courses: str, year):
        super(Student, self).__init__(firstName, lastName, id, adress, year)
        self.__courses = courses
        self.__year = year

    def get_courses(self):
        return self.__courses

    def set_courses(self, courses):
        self.__courses = courses

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year








