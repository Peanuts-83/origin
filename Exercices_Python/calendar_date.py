import calendar, sys
from os import strerror

class WeekdayError(ValueError):
    def __init__(self, day):
        super().__init__()
        self.day = day

class My_Calendar(calendar.Calendar):
    def __init__(self):
        super().__init__()
    
    def count_weekday_in_year(self, year, weekday):
        if weekday < 0 or weekday > 6:
            raise WeekdayError(weekday)
        weekdays = 0
        for month in range(1,13):
            for i in self.monthdays2calendar(year,month):
                #print('\n', i[1])
                if i[weekday][0] != 0:
                    weekdays += 1
        return weekdays

try:
    cal = My_Calendar()
    print(f'Number of {list(calendar.day_name)[0]}\'s in year {2019}: ',cal.count_weekday_in_year(2019, 0))
    print(f'Number of {list(calendar.day_name)[6]}\'s in year {2000}: ',cal.count_weekday_in_year(2000, 6))
except WeekdayError as wd:
    print('Weekday error : day range may be (0-6) // Day entered: ', wd.day)
    sys.exit()


#for weekday in cal.iterweekdays():
#    print(weekday, end=" ")

#print('\n', dir(My_Calendar))

