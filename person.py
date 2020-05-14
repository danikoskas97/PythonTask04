from datetime import date  # we will use this for date objects


class Person:

    def __init__(self, name: str, surname: str, birth_date: date,
                 address: str,
                 person_id: int,
                 courses: frozenset = (),
                 study_year: int = 0
                 ):
        self.__name = name
        self.__surname = surname
        self.__birth_date = birth_date
        self.__address = address
        # self.__phone = phone
        # self.__email = email
        self.__id = person_id
        self.__courses = courses
        self.__study_year = study_year
        self.__age_date_stored = None
        self.__age = 0
        self.age()

    def __str__(self):
        return f'name: {self.name}; address: {self.__address};'

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if self.__age == 0 \
                or self.__age_date_stored != today \
                or self.__age != age:
            self.__age_date_stored = today
            self.__age = age
        if today < date(today.year, self.birth_date.month, self.birth_date.day):
            age -= 1
        return self.__age

    # just for simplifying the output, in general there should be 2 functions :)
    @property
    def name(self):
        return self.__name + ' ' + self.__surname

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if self.__birth_date != value:
            self.__birth_date = value
            self.age()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def study_year(self):
        return self.__study_year

    @study_year.setter
    def study_year(self, value):
        self.__study_year = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        self.__courses = value

    def print_courses(self):
        ret = ''
        for c in self.__courses:
            ret += c + ', '
        ret.rstrip(', ')
        return f'{ret} in {self.__study_year}'

    # returns dictionary - course: person
    def cmp_own_courses_to_persons(self, persons: frozenset) -> dict:
        d = dict()
        for crs in self.courses:
            for lct in persons:
                common_courses_to_persons = frozenset([crs]) & lct.courses
                if common_courses_to_persons != frozenset():
                    for i in common_courses_to_persons:
                        d[lct] = common_courses_to_persons
        return d

    def who_am_i(self) -> str:
        return "I'm a base :" + str(type(self))