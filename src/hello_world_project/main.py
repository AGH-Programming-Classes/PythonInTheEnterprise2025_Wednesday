from hello_world_project.utils import greet_user
from hello_world_project.example_module import add_numbers

def main():
    print("=== Hello World Project ===")

    name = input("Enter your name: ")
    greeting = greet_user(name)
    print(greeting)

    result = add_numbers(10, 5)
    print(f"The result of adding 10 and 5 is {result}.")

if __name__ == "__main__":
    main()
