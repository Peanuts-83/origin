#!/bin/bash python 3.8
# Creation de classe avec passage d'attributs et évaluat°
"""class User:

    def check_pwd(self, password):
        print(password, '-', self.password == password)


tom = User()
tom.id = 1
tom.name = 'tom'
tom.password = 'azerty'
tom.check_pwd('lulu')
tom.check_pwd('azerty')"""


# Le password est privatisé avec _ (reste accessible par obj._attr) ou __ (accessible par obj._Class__attr)
# Module thread/post de forum développé
import datetime

class User1:

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.__password = self.encrypt_pwd(password)

    def encrypt_pwd(self, password):
        pwd = ''.join(chr(ord(x)+1) for x in password)
        return pwd

    def check_pwd(self, new_pass):
        try:
            if self.__password != self.encrypt_pwd(new_pass):
                raise ValueError
        except ValueError:
            return f'{new_pass}: Wrong password!'
        else:
            return f'{new_pass}: Password ok'

    def post(self, msg):
        return Post(self, msg)

    def new_thread(self, title, msg):
        return Thread(title, self, msg)

    def answer_thread(self, thread, msg):
        thread.answer(self, msg)

class Post:
    def __init__(self, author, msg):
        self.author = author
        self.msg = msg
        self.date = datetime.datetime.now()

    def format(self):
        date = self.date.strftime('le %d/%m/%Y à %H:%M:%S')
        return f'<div><span>Par {self.author.name}, {date} <p> {self.msg} </span></div>'

class Thread(Post):
    def __init__(self, title, author, msg):
        super().__init__(author, msg)
        self.title = title
        self.posts = []

    def answer(self, author, msg):
        self.posts.append(Post(author, msg))

    def format(self):
        posts = [f'<title>{self.title}</title>', super().format()]
        posts += [p.format() for p in self.posts]
        return '\n'.join(posts)

if __name__ == '__main__':
    tom = User1(1, 'tomtom', 'qsdfgh')
    bill = User1(2, 'billy', 'azerty')
    print('password check and encryption:\nencrypted password is: ',tom._User1__password)
    print(tom.check_pwd('azerty'))
    print(tom.check_pwd('qsdfgh'))
    print("\nModule forum avec suivi d'un thread entre 2 users:")
    print(tom.post('Bonjour,\n Ceci est un test de post hors thread.').format())
    thread = tom.new_thread('First post', 'Hello everybody!')
    bill.answer_thread(thread, 'Hey you, how are you?')
    print(thread.format())


# Héritage d'une fonction de classe à une sub-classe

class Reversable:
    def reverse(self):
        return self[::-1]

class ReversableStr(Reversable, str):
    pass

class ReversableTuple(Reversable, tuple):
    pass

print('\nfonction reverse appliquée par héritage de classe:')
c = ReversableStr('abc')
print('abc >> ',c.reverse())
print('(1, 2, 3) >>',ReversableTuple((1,2,3)).reverse())
