#! usr/bin/python3
from hello_world_project.utils import greet_user
import hello_world_project.example_module 

def main():
    print("=== Hello World Project ===")

    name = input("Enter your name: ")
    greeting = greet_user(name)
    print(greeting)

    result = hello_world_project.example_module.SimpleCalculator().add_numbers(10, 5)
    print(f"The result of adding 10 and 5 is {result}.")

smpcal=
if __name__ == "__main__":
    main()
