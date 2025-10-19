from hello_world_project.utils import greet_user
from hello_world_project.example_module import add_numbers


cities=[("Krakow",30),("Warszawa",25),("Gdansk",20)]

def weather(city):
    if not city:
        return f"Podaj miasto!"
    return f"In {city.name} is {city.temperature} "



def main():
    print("=== Hello World Project ===")



    city = input("Enter your name: ")
    temperature = weather(city)
    print(temperature)

    result = add_numbers(10, 5)
    print(f"The result of adding 10 and 5 is {result}.")

if __name__ == "__main__":
    main()
