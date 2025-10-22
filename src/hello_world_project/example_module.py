class SimpleCalculator:
    def add_numbers(self, a: float, b: float) -> float:
        return a + b

    def sub_numbers(self, a: float, b:float) -> float:
        return a - b

    def multiply_numbers(self, a: float, b: float) -> float:
        return a * b

    def div_numbers(self, a: float, b: float) -> float:
        if(abs(b)<0.0001):
            return a / b
        else:
            raise Exception

