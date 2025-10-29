import requests
import tkinter


# Adapters 
class GeocodingAdapter:
    def get_coordinates(self, city_name):
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": city_name, "format": "json"}
        response = requests.get(url, params=params, headers={"User-Agent": "WeatherApp"})
        data = response.json()
        return float(data[0]["lat"]), float(data[0]["lon"])

class WeatherAPIAdapter:
    def get_temperature(self, lat, lon):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {"latitude": lat, "longitude": lon, "current_weather": True}
        response = requests.get(url, params=params)
        data = response.json()
        return data["current_weather"]["temperature"]
    
#Facade using adapters
class WeatherService:
    def __init__(self):
        self.geo = GeocodingAdapter()
        self.weather = WeatherAPIAdapter()

    def get_weather(self, city_name):
        lat, lon = self.geo.get_coordinates(city_name)
        temp = self.weather.get_temperature(lat, lon)
        return f"W {city_name} jest {temp} °C."


    
# Facade and singleton  
class UI:
    _instance = None
    def __init__(self):
        self.root = tkinter.Tk()
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def create(self, weatherService):

        # Dodaje tytuł oraz wymiary głównego okna (szerokość, wysokość)
        self.root.title("=== Weather ===")
        self.root.geometry("300x200")

        # Tworzymy widget label podając nadrzędny element oraz zawartość
        label = tkinter.Label(self.root, text="Enter city: ")
        # Dodaje element do okna
        label.pack(pady=10)

        entry = tkinter.Entry(self.root)
        entry.pack(pady=10)


        button = tkinter.Button(self.root, text="Search", command=lambda:label_result.config(text=f"{weatherService.get_weather(entry.get())}"))
        button.pack(pady=10)

        label_result = tkinter.Label(self.root)
        label_result.pack(pady=10)

        button_quit = tkinter.Button(self.root, text="Close", command=self.root.quit)
        button_quit.pack()

        # Uruchamia pętlę zdarzeń
        self.root.mainloop()




def main():
    service = WeatherService()

    ui = UI()
    ui.create(service)

if __name__ == "__main__":
    main()
