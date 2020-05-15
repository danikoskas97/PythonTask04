from employee import Employee


class Lecturer(Employee):
    def __init__(self, first_name, last_name, birthdate: str, adress, telephone, email, base_salary, seniority
                 , hourly_rate, teaches_courses: list):
        super().__init__(first_name, last_name, birthdate, adress, telephone, email, base_salary, seniority)
        self.hourly_rate = hourly_rate
        self.teaches_courses = teaches_courses

    @property
    def teaches_courses(self):
        return self.__teaches_courses

    @teaches_courses.setter
    def teaches_courses(self, teaches_courses):
        self.__teaches_courses = teaches_courses
