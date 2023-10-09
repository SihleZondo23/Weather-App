import requests
import json

def get_weather(API_key, Durban):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch weather data.")
        return None

def display_weather(data):
    if data:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("No weather data to display.")

if __name__ == "__main__":
    api_key = "680ac35389cad2db6bf07e2e19aa311d"
    city = input("Enter a city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)
