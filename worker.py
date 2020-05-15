from person import Person
import datetime  # we will use this for date objects


class Worker(Person):
    def __init__(self, name: str, surname: str, birth_date: datetime.date, address: str, person_id: int):
        super().__init__(name, surname, birth_date, address, person_id)
