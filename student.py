from person import Person


class Student(Person):
    def __init__(self, firstName, lastName, id, adress, courses: str, year):
        Person.__init__(self, firstName, lastName, id, adress, year)
        self.__courses = courses
        self.__year = year

    def get_courses(self):
        return self.__courses

    @property
    def set_courses(self, courses):
        self.__courses = courses

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def take_courses(self):
        ret = ''
        for course in self.__courses:
            ret += course + ', '
        print(f'{str(self)}\n course in year {self.__year}:\n')

    # def takes_courses_from(self, lecturer: frozenset) -> str:













