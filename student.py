import datetime
from person import Person


class Student(Person):
    def __init__(self, firstName, lastName, id, adress, courses: str, year):
        super(Student, self).__init__(firstName, lastName, id, adress, year)
        self.__courses = courses
        self.__year = year

    def getCourses(self):
        return self.__courses

    def setCourses(self, courses):
        self.__courses = courses

    def getYear(self):
        return self.__year

    def setYear(self, year):
        self.__year = year








