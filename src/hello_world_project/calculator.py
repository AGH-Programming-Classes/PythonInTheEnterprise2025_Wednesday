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

class Calculator:
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






