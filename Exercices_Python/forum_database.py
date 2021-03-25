import abc, datetime

class Database:
    data = []

    def insert(self, obj):
        self.data.append(obj)
    
    def select(self, cls, **kwargs):
        items = (item for item in self.data
                if isinstance(item, cls) 
                and all(hasattr(item, k) and getattr(item, k) == v for (k, v) in kwargs.items())
                )
        try:
            return next(items)
        except StopIteration:
            raise ValueError('item not found')


class Model(abc.ABC):
    db = Database()

    @abc.abstractmethod
    def __init__(self):
        self.db.insert(self)

    @classmethod
    def get(cls, **kwargs):
        return cls.db.select(cls, **kwargs)

    @property
    def id(self):
        return id(self)


class User(Model):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Post(Model):
    def __init__(self, author, msg):
        super().__init__()
        self.author = author
        self.msg = msg
        self.date = datetime.datetime.now()

    def format(self):
        date = self.date.strftime('le %d/%m/%Y à %H:%M:%S')
        return '<div><span>Par {} {}</span><p>{}</p></div>'.format(self.author.name, date, self.msg)

if __name__ == '__main__':
    tom = User('toto')
    bill = User('billy')
    Post(tom, 'Hello world!')
    Post(bill, 'hello tooooo...!')
    print(Post.get(author = User.get(name='toto')).format())