#! usr/bin/python3
from utils import greet_user
import example_module 

def main():
    print("=== Hello World Project ===")

    name = input("Enter your name: ")
    greeting = greet_user(name)
    print(greeting)

    calc_dict={"b":example_module.SimpleCalculator, "s":example_module.ScientificCalc, "f":example_module.FinancialCalc}
    calc_s= input("Enter b for basic\n, s for scientific\n and f for financial calculator:")
    calc=calc_dict[calc_s]()
    while True:
        if calc_s == "b":
            fun_dict_1={"a":example_module.SimpleCalculator.add_numbers,"s":example_module.SimpleCalculator.sub_numbers,"m":example_module.SimpleCalculator.multiply_numbers,"d":example_module.SimpleCalculator.div_numbers}
            fun_s= input("Enter a for addition, \n s for subtraction, \nm for multiplication, \nd for division")
            fun=fun_dict_1[fun_s]
        elif calc_s == "s":
            fun_dict_2={"a":example_module.ScientificCalc.add_numbers,"s":example_module.ScientificCalc.sub_numbers,"m":example_module.ScientificCalc.multiply_numbers,"d":example_module.ScientificCalc.div_numbers,"p":example_module.ScientificCalc.power_numbers,"q":example_module.ScientificCalc.sqr_numbers}
            fun_s= input("Enter a for addition, \n s for subtraction, \nm for multiplication, \nd for division, \np for power, \nq for square_root ")
            fun=fun_dict_2[fun_s]
        else:
            fun_dict_3={"a":example_module.FinancialCalc.add_numbers,"s":example_module.FinancialCalc.sub_numbers,"m":example_module.FinancialCalc.multiply_numbers,"d":example_module.FinancialCalc.div_numbers}
            fun_s= input("Enter a for addition, \n s for subtraction, \nm for multiplication, \nd for division")
            fun=fun_dict_3[fun_s]
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print(fun(calc,a,b))
    
    result = example_module.SimpleCalculator().add_numbers(10, 5)
    print(f"The result of adding 10 and 5 is {result}.")


if __name__ == "__main__":
    main()
