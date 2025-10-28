#! usr/bin/python3
from utils import greet_user
import example_module 

def main():
    print("=== Hello World Project ===")

    name = input("Enter your name: ")
    greeting = greet_user(name)
    print(greeting)

    result = example_module.SimpleCalculator().add_numbers(10, 5)
    print(f"The result of adding 10 and 5 is {result}.")


if __name__ == "__main__":
    main()
