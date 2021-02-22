class Lux_Watch:
    _watches_created = 0

    def __init__(self):
        print('__init__ activated')
        Lux_Watch._watches_created += 1
        self.txt = ''

    @classmethod
    def get_number_of_watches_created(cls):
        return cls._watches_created

    @classmethod
    def engraving(cls, txt):
        print('cls activated')
        _watch = cls()
        if cls.validation(txt) == 'Ok for engraving!':
            print(cls.validation(txt))
            _watch.txt = txt
            return _watch
        else:
            print(cls.validation(txt))
            print('No watch created')
        

    @staticmethod
    def validation(txt):
        try: 
            if len(txt) > 40 or not txt.isalnum():
                raise ValueError
        except:
            return 'length or char type incorrect!'
        else:
            return 'Ok for engraving!'

swatch = Lux_Watch()
print('swatch num:', swatch.get_number_of_watches_created())
rollex = Lux_Watch.engraving('Hellodear')
print('Rollex num: ', rollex.get_number_of_watches_created())