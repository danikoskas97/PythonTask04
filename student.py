from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, birthdate: str, adress, telephone, email, courses: list, year):
        super().__init__(first_name, last_name, birthdate, adress, telephone, email)
        self.courses = courses
        self.year = year

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses