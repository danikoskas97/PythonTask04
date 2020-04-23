import datetime

from person import Person


class Student(Person):
    def __init__(self, courses: str, year: datetime.date):
        self.__courses = courses
        self.year = year


yoad = Student("yoad", "gadot", 1233, "tlv","python", datetime.date(2014, 3, 21))

print(yoad)
