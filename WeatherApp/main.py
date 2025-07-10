import requests
from datetime import datetime

API_KEY = "fe18de3cdfd0e199cb4312206981ff48"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
            sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')

            print(f"\n🌦 Weather in {city.title()}, {data['sys']['country']}:")
            print(f"☁️  Condition: {weather}")
            print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌬 Wind Speed: {wind_speed} m/s")
            print(f"🌅 Sunrise: {sunrise} | 🌇 Sunset: {sunset}")
        else:
            print(f"\nError: {data.get('message', 'Unknown error')}")
            
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork error: {e}")
    except KeyError as e:
        print(f"\nUnexpected data format: Missing {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)