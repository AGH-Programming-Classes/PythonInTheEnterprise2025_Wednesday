def add_numbers(a: float, b: float) -> float:
    return a + b

def sub_numbers(a: float, b:float) -> float:
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    return a * b

def div_numbers(a: float, b: float) -> float:
    if(abs(b)<0.0001):
        return a / b
    else:
        raise Exception
