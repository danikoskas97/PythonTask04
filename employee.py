from person import Person


class Employee(Person):
    def __init__(self, first_name, last_name, birthdate: str, adress, telephone, email, base_salary, seniority):
        super().__init__(first_name, last_name, birthdate, adress, telephone, email)
        self.base_salary = base_salary
        self.seniority = seniority