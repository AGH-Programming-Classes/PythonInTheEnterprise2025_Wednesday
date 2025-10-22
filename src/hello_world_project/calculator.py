import time
class TimerDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Starting calculator  operations")
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} executed in {end_time - start_time} seconds")
        return result










# def decorator(fun):
#     def logger(self):
#         print("Starting operations")



@TimerDecorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total