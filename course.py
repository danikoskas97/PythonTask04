from datetime import time


class Course:
    def __init__(self,
                 name: str,
                 length_in_minutes: int,
                 start_time: time,
                 by_weekdays: str,
                 lecturer_id: int = 0):
        self.__name = name
        self.__length_in_minutes = length_in_minutes
        self.__lesson_starts_at = start_time
        self.__by_weekdays = by_weekdays
        self.__lecturer_id = lecturer_id
        self.stam = None

    @property
    def lecturer_id(self):
        return self.__lecturer_id

    @lecturer_id.setter
    def lecturer_id(self, id):
        self.__lecturer_id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        try:
            self.__name = 'course: ' + name
        except:
            self.__name = '-'
