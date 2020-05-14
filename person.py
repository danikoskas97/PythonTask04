from datetime import date, datetime


class Person:
    def __init__(self, first_name, last_name, birthdate: str, adress, telephone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.adress = adress
        self.telephone = telephone
        self.email = email
        today = date.today() # question 3
        self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                                   self.birthdate.day))

    def __str__(self):
        return f'שמי הפרטי הוא:{self.first_name}' \
               f'-----' \
               f' שם משפחתי הוא: {self.last_name}' \
               f'-----' \
               f' אני גרה ב{self.adress}'

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def birthdate(self):
        return self.__birthdate


    @birthdate.setter
    def birthdate(self, birthdate):
        try:
            year, month, day = map(int, birthdate.split(','))
            self.__birthdate = datetime(year, month, day)
            return self.__birthdate
        except ValueError:
            print("פורמט לא תואם, נסה שוב")