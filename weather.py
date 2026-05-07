import requests
import sys

def get_coordinates(city, country_code=None):
    
    url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}"
        f"&count=1"
    )

    if country_code:
        url += f"&country_code={country_code}"

    response = requests.get(url)
    data = response.json()

    if "results" not in data:
        print("City not found.")
        sys.exit()

    result = data["results"][0]

    return (
        result["latitude"],
        result["longitude"],
        result["name"],
        result.get("country", "Unknown")
    )

def get_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    return data["current_weather"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 weather.py <city>")
        sys.exit()
    
    city = " ".join(sys.argv[1:])

    latitude, longitude, city_name, country = get_coordinates(city, "CR")
    
    weather = get_weather(latitude, longitude)

    print(f"\n🌍 {city_name}, {country}")
    print(f"🌡 Temperature: {weather['temperature']}°C")
    print(f"💨 Wind Speed: {weather['windspeed']} km/h")
    print(f"🧭 Wind Direction: {weather['winddirection']}°")
    print(f"⏰ Time: {weather['time']}")

if __name__ == "__main__":
    main()