import requests
import tkinter

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

    # Tworzy główne okno aplikacji
    root = tkinter.Tk()

    # Dodaje tytuł oraz wymiary głównego okna (szerokość, wysokość)
    root.title("=== Weather ===")
    root.geometry("300x200")

    # Tworzymy widget label podając nadrzędny element oraz zawartość
    label = tkinter.Label(root, text="Enter city: ")
    # Dodaje element do okna
    label.pack(pady=10)

    entry = tkinter.Entry(root)
    entry.pack(pady=10)


    button = tkinter.Button(root, text="Search", command=lambda:label_result.config(text=f"{weather(entry.get())}"))
    button.pack(pady=10)

    label_result = tkinter.Label(root)
    label_result.pack(pady=10)

    button_quit = tkinter.Button(root, text="Close", command=root.quit)
    button_quit.pack()

    # Uruchamia pętlę zdarzeń
    root.mainloop()

if __name__ == "__main__":
    main()
