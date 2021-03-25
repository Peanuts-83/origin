from time import time, sleep
from random import randint

class Timer:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):        # *args & **kwargs to anticipate use of any number/kind of arguments with function call
    # __call__ special method meant to be used when function is self-called
        before = time()
        result = self.function(*args, **kwargs)
        after = time()
        print(f"Your function {self.function} took {after - before} sec(s) to execute.")

@Timer          # @Timer decorator to launch class Timer when pause function called
def pause():
    sec = randint(1,3)
    print(f"Faisons une pause de {sec} secondes.")
    sleep(sec)
    print("La pause est finie!")

pause()