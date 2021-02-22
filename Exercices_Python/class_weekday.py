class WeekDayError(Exception):
    pass
	

class Weeker:
    __wk = "Mon Thu Wed Thu Fri Sat Sun"

    def __init__(self, day):
        self.__week = [i for i in self.__wk.split()]
        self.__day = day
        if self.__day not in self.__week:
            raise WeekDayError 

    def __str__(self):
        return self.__day

    def add_days(self, n):
        new_day_index = (self.__week.index(self.__day) + n) % 7 + self.__week.index(self.__day)
        self.__day = self.__week[new_day_index]

    def subtract_days(self, n):
        new_day_index = (self.__week.index(self.__day) - n+1) % 7 - self.__week.index(self.__day)
        self.__day = self.__week[new_day_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
