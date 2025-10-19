
cities=[("Krakow",30),("Warszawa",25),("Gdansk",20)]

def weather(city_name):
    if not city_name:
        return "Podaj miasto!"
    for name, temp in cities:
        if name.lower() == city_name.lower():
            return f"In {name} is {temp} C "
    return f"Unknown city ({city_name})"


def main():
    print("=== Wheather ===")

    city = input("Enter city: ")
    temperature = weather(city)
    print(temperature)

if __name__ == "__main__":
    main()
