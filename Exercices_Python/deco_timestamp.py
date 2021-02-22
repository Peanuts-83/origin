from datetime import datetime

def modifier(func):
    def wrapper(*args):
        args = args + ('Zut ','Déjà! ')
        print(func.__name__,' is the function name activated with ', args)
        print(func(*args)[0].strftime('date from modifier: %A %d %b %Y, %Hh %Mmn %Ssec\n'))
        print(func(*args)[1])
        print(func(*args))
    return wrapper

@ modifier
def time_date(*args):
    timestamp = datetime.now()
    send =''
    for n in args:
        send += (n + timestamp.strftime('%Y-%m-%d %H:%M:%S') + '\n')
    return timestamp , send

print(time_date('Hello ', 'Hi ', 'Bonjour '))