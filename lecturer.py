from person import Person

class Lecturer(Person):
    def __init__(self, firstName,lastName,id,adress, year, rate_for_hour):
        super(Lecturer,self).__init__(firstName,lastName,id,adress, year)
        self.__rate_for_hour = rate_for_hour

    def get_rate_for_hour(self):
        return self.__rate_for_hour

    def set_rate_for_hour(self,rate_for_hour):
        self.__rate_for_hour = rate_for_hour


