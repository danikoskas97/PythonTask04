import datetime

from lecturer import Lecturer
from student import Student

student1 = Student("yoad", "gadot", 1233, "Tel-aviv", ("Python", "Java"), 2020)
student2 = Student("Dani", "Koskas", 2313, "Raanana", ("Python", "advanced algorithm"), 2020)
lecturer1 = Lecturer("gab", "rich", 43600, "Eilat", ("Python", "advanced algorithm"), 2020)

student2.get_name()
