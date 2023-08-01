import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY

def get_weather_data():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Please check your internet connection or API key.")
        return None

def get_weather(date):
    weather_data = get_weather_data()
    if weather_data:
        for forecast in weather_data['list']:
            if date in forecast['dt_txt']:
                return forecast['main']['temp']
        print("Data not found for the given date.")
        return None

def get_wind_speed(date):
    weather_data = get_weather_data()
    if weather_data:
        for forecast in weather_data['list']:
            if date in forecast['dt_txt']:
                return forecast['wind']['speed']
        print("Data not found for the given date.")
        return None

def get_pressure(date):
    weather_data = get_weather_data()
    if weather_data:
        for forecast in weather_data['list']:
            if date in forecast['dt_txt']:
                return forecast['main']['pressure']
        print("Data not found for the given date.")
        return None

def main():
    while True:
        print("\n1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_weather(date)
            if temperature:
                print(f"Temperature on {date}: {temperature} K")

        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")

        elif choice == 0:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
