import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email
        self._age = None
        self.recalculated_age = None

        self.recalculate_age()

    def recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        self.recalculated_age = today

    def age(self):
        if datetime.date.today() < self.recalculated_age:
            self.recalculate_age()
        return self._age

    def __repr__(self):
        return f'{self.name} {self.surname} is aged {self.age()} and leaves {self.address}.'

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print('age:',person.age())
print('cached _age:',person._age)
print(person)