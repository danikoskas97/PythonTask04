from person import Person
from student import Student
from datetime import date
from course import Course


class Lecturer(Person):
    def __init__(self
                 , name: str
                 , surname: str
                 , birth_date: date
                 , address: str
                 , person_id: int
                 , courses: frozenset
                 , study_year: int
                 , hourly_rate: float
                 ) -> None:
        super().__init__(name, surname, birth_date, address, person_id, courses, study_year)

    @property
    def hourly_rate(self) -> float:
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate: float) -> None:
        self.__hourly_rate = hourly_rate

    def teaches_courses(self, stud: Student):
        return self.__str__() + ' teaches ' + self.print_courses()

    def teaches_students(self, students: frozenset):
        d = self.cmp_own_courses_to_persons(students)
        courses_cnt = len(d)
        ret = f'Lecturer {self.name}\n in year {self.study_year} teaches'
        if courses_cnt == 0:
            return ret + 'no courses.'
        else:
            ret = f'{ret}: '

        for course in d:
            ret += f"\n{str((list(d[course])))} to {course}"
        return ret

    # שתחזיר סטודנטים (שם) לפי הקורס
    def i_teach_courses_as_str(self) -> str:
        pass

    # שתחזיר כל קורסים של המרצה
    def who_takes_my_course_as_str(self, course: Course) -> str:
        pass
