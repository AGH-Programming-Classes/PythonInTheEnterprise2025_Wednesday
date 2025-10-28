from datetime import datetime
def godz_dek(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().strftime('%H:%M:%S')}]")
        return func(*args, **kwargs)
    return wrapper
   
class SimpleCalculator:
    def add_numbers(self, a: float, b: float) -> float:
        return a + b

    def sub_numbers(self, a: float, b:float) -> float:
        return a - b

    def multiply_numbers(self, a: float, b: float) -> float:
        return a * b

    def div_numbers(self, a: float, b: float) -> float:
        if(abs(b)>0.0001):
            return a / b
        else:
            raise Exception
       
class ScientificCalc(SimpleCalculator):
    def power_numbers(self, base, exp):
        return base ** exp
    def sqr_numbers(self, base):
        return base ** 1/2

class FinancialCalc(SimpleCalculator):
    @godz_dek
    def add_numbers(self, a: float, b: float) -> float:
        return a + b
    @godz_dek
    def sub_numbers(self, a: float, b:float) -> float:
        return a - b
    @godz_dek
    def multiply_numbers(self, a: float, b: float) -> float:
        return a * b
    @godz_dek
    def div_numbers(self, a: float, b: float) -> float:
        if(abs(b)>0.0001):
            return a / b
        else:
            raise Exception
    

# def FactoryCalculator(type: str):
#     factory = {"Simple": SimpleCalculator, "Science":ScientificCalc }
#     return factory[type]()