from datetime import date

from student import Student
from lecturer import Lecturer

student1 = Student('Dani', 'koskas', '1997,6,04', 'Raanana', '0584190758'
                   , 'rahelsc@gmail.com', ['python', 'js'], 2)

student2 = Student('Blaise', 'Matudi', '1979,4,12', 'Paris', '008-3402202'
                   , 'rahelsc@gmail.com', ['python', 'cSharp'], 2)

lecturer1 = Lecturer("James", 'Bond', '1970,7,09', 'Ariel', '012-000007', 'james.bond&gmail.com', '8000',
                     'high'
                     , '200', ['python'])


# question 3 - the ability to update age after creation
def calculate_age(self):
    today = date.today()
    self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                               self.birthdate.day))
    return self.age
