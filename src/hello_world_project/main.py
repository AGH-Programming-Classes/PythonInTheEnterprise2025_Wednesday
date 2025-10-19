import requests

def get_coordinates(city_name):
    url = "https://nominatim.openstreetmap.org/search" #uzywamy darmowego geokodera co zamienia nazwe miasta na jego koordynaty
    
    params = {
        "q": city_name,
        "format": "json" #format w ktorym chcemy uzyskac dane
    }

    try:
        response = requests.get(url, params = params,headers={"User-Agent":"WeatherApp"}) #url, parametry, oraz naglowek (kto wysyla zadanie)
        data = response.json() #data to lista słowników w formacie json

        lat = float(data[0]["lat"]) #konwerujemy dlugosc i szerokosc miasta na floata z pierwszego wyniku zwroconego w data
        lon = float(data[0]["lon"])

        return lat, lon
    
    except requests.RequestException:
        return None

def weather(city_name):
    if not city_name:
        return "Podaj miasto!"

    coordinates = get_coordinates(city_name)

    lat, lon = coordinates

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude":lon,
        "current_weather": True #chcemy aktualna pogode wiec ustawiamy ja na true
    }

    try:
        response = requests.get(url,params=params)
        data = response.json()
        temp = data["current_weather"]["temperature"]
        return f"W {city_name} jest {temp} C."
    
    except requests.RequestException:
        return f"Blad polaczenia"


def main():
    print("=== Weather ===")

    city = input("Enter city: ")
    temperature = weather(city)
    print(temperature)

if __name__ == "__main__":
    main()
