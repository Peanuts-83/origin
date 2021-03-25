

class MetaWidget(type):
    trace_classes = {}
    def __init__(cls, nom, bases, dico):
        type.__init__(cls, nom, bases, dico)
        cls.trace_classes[nom] = cls

class Widget(metaclass=MetaWidget):
    pass

class Button(Widget):
    pass

class Nope(Button):
    pass

print(MetaWidget.trace_classes)