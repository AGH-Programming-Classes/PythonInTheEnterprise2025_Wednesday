import time
class TimerDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Starting calculator  operations")
        start_time = time.time()
        result = self.func(self,*args)
        end_time = time.time()
        print(f"Function {self.func.__name__} executed in {end_time - start_time} seconds")
        return result


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Calculator(metaclass=SingletonMeta):
    def __init__(self):
        pass
    @TimerDecorator
    def add(self,a,b):
        return a+b
    @TimerDecorator
    def subtract(self,a,b):
        return a-b
    @TimerDecorator
    def multiply(self,a,b):
        return a*b
    @TimerDecorator
    def divide(self,a,b):
        if b==0:
            raise ArithmeticError("")
        return a/b



if __name__=="__main__":
    calc = Calculator()
    print(calc.add(1,2))
    calc_1 = Calculator()
    calc_2 = Calculator()
    if id(calc_1) == id(calc_2):
        print("Singleton works.")
    else:
        print("Singleton failed.")







