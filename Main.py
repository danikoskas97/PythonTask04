import datetime
from person import Person
from lecturer import Lecturer
from student import Student

student1 = Student(firstName="yoad", lastName="gadot", id=1233, adress="Tel-aviv", courses=("Python", "Java"), year=2020)
student2 = Student(firstName="Dani", lastName="Koskas", id=2313, adress="Raanana", courses=("Python", "advanced algorithm"), year=2020)
lecturer1 = Lecturer(firstName="gab", lastName="rich", id=43600, adress="Eilat", rate_for_hour=200, year=2020)

student2.get_name()
