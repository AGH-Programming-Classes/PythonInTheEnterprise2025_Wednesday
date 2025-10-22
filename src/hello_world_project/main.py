from utils import greet_user
from calculator_main import CalculatorFabrica

def main():
    print("=== Calculator Project ===")
    type = input("Wybierz typ kalkulatora normal lub business: \n")
    CalculatorFabrica().createCalc(type).calc_main()

if __name__ == "__main__":
    main()
