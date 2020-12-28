from time import time

class Temps:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        before = time()
        result = self.function(*args)
        after = time()
        print(f"Your function {self.function()} took {after - before} sec(s) to execute.")
        return result

