import datetime, time
dt = datetime.datetime.now()
print('#STRFTIME:\ndatetime.datetime.strftime:\n',dt, sep='')
print(dt.strftime('Year: %Y - Month: %B - Day: %A'))
print(dt.strftime('Week of the Year: %U'))
print(dt.strftime('Day of the week: %a (#%d)'))
print(dt.strftime('Num day of the year: %j'))
print(dt.strftime('Num day of week: %w'))
print(dt.strftime('Current time: %X'))
print('Today Midnight:', dt.date(), dt.min.time() )

date_str = 'Jan 1 2014 2:43PM'
date_obj = datetime.datetime.strptime(date_str, '%b %d %Y %I:%M%p')
print('\n','#STRPTIME:\ndatetime.datetime.strptime:\n(interpretat° of str \'Jan 1 2014 2:43PM\'): ', date_obj, sep='')


print('\n#TIMEDELTA\ndatetime.timedelta:\nToday - 5 days:',dt.date() - datetime.timedelta(5))
old_dt = datetime.datetime(2021,2,11)
print('Diff between 2 dates: ',dt.date() - old_dt.date())
current_day_num = dt.strftime('%w')
print('Today:', dt.date(), 'Yesterday:', dt.date() - datetime.timedelta(days=1), 'Tomorrow:', dt.date() + datetime.timedelta(1) )
for x in range(1,6):
    print(dt.date() + datetime.timedelta(x), '/ ', end='')
print('\n','Current time - 5 min: ',(dt - datetime.timedelta(minutes=5)).time(), sep='')
print('Date1 - date2: ', end='')
date1 = datetime.date(1992,1,16); date2 = datetime.date(1991,2,5)
print(date1 - date2)

timestamp = 1284105682
print('\n# TIMESTAMP:\ndatetime.datetime.fromtimestamp:\nUnix timestamp conv°:', datetime.datetime.fromtimestamp(timestamp))


print('\n# ISOCALENDAR:\ndatetime.date(yyyy, mm, dd).isocalendar - return # year, # week, # weekday:',datetime.date(2015,12,5).isocalendar() )
print('  datetime.date(2015 12 05).isocalendar - week of the year:',(datetime.date(2015,12,5).isocalendar()[1]) )
date = datetime.date.fromisocalendar(2015, 50, 1)
print('  datetime.date.fromisocalendar(2015, 50, 1)-(monday of week 50):', date.strftime('%A %d %b %Y'))


print('\nAll sundays of a year:')
def all_sundays(year):
    date = datetime.date(year,1,1)
    date += datetime.timedelta(days = 6 - date.weekday())
    while date.year == year:
        yield date
        date += datetime.timedelta(days=7)
for i in (all_sundays(2015)): print(i, '/ ', end='')

print('\n\nAdd years function:')
def add_years(dt, y):
    try:
        return dt.replace(year = dt.year + y)
    except ValueError:
        return dt + (datetime.date(dt.year + y ,1,1) - datetime.date(dt.year ,1,1))
print('2015-01-01 ->',add_years(datetime.date(2020,2,29), 5))


print('\nGet days between 200-02-28 ans 2001-02-28:')
a = datetime.date(2000,2,28); b = datetime.date(2001,2,28)
print(max(a,b) - min(a,b))


import calendar as cal
print(f'\n\n#ISLEAP:\ncalendar.isleap:\nLeap years: 2021-{cal.isleap(2021)}, 1976-{cal.isleap(1976)}')

print('\n',cal.month(2020,1))
print(cal.weekheader(2))

print('\n# MONTHDAYS2CALENDAR')
c = cal.Calendar()
for data in c.monthdays2calendar(2020,1):
    print(data)

