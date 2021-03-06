from datetime import date
from student import Student
from lecturer import Lecturer

student1 = Student('Dani', 'koskas', '1997,6,04', 'Raanana', '0584190758'
                   , 'koskas.dani@gmail.com', ['python', 'js'], 2)

student2 = Student('Blaise', 'Matudi', '1979,4,12', 'Paris', '008-3402202'
                   , 'blaiseGotHacked@gmail.com', ['python', 'cSharp'], 2)

lecturer1 = Lecturer("James", 'Bond', '1970,7,09', 'Ariel', '012-000007', 'james.bond&gmail.com', '8000',
                     'high'
                     , '200', ['python'])


# Q.2
def check_who_teaches(teacher: Lecturer, s: Student):
    try:
        for i in teacher.teaches_courses:
            for j in s.courses:
                if i == j:
                    print(f'{teacher.fname} teaches {i}')
                    print(f'{s.fname} studies {i}')
    except TypeError:
        print("only recieves a lecturer and a student, please try again")
    except:
        print("bad input, try again")


check_who_teaches(lecturer1, student1)


# Q.3 update age after creation
def calculate_age(self):
    today = date.today()
    self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                               self.birthdate.day))
    return self.age


print(student1.age)
