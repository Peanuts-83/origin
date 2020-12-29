class generic_obj:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s: %s" % (classname, " ".join(attrs))

    def __repr__(self):
        return ' '.join(['='.join((k,v)) for k,v in self.__dict__.items()])

a = generic_obj(key1='aaa', key2='bbb', key3='jklj')
print(a)
