import requests

API_KEY = "f678e91b1dba921a65d38479dc1e389b"  # Replace with your actual key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    # Construct request parameters
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "imperial"  # Options: 'metric' (°C), 'imperial' (°F), or 'standard' (Kelvin)
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx status codes
        
        data = response.json()
        
        # Parse relevant fields from the JSON payload
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()
        wind_speed = data["wind"]["speed"]

        # Display output
        print("\n" + "="*30)
        print(f" Weather Report: {city}, {country}")
        print("="*30)
        print(f"Condition:   {description}")
        print(f"Temperature: {temp}°F (Feels like {feels_like}°F)")
        print(f"Humidity:    {humidity}%")
        print(f"Wind Speed:  {wind_speed} m/s")
        print("="*30 + "\n")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print(f"\n Error: City '{city_name}' not found. Check spelling.")
        elif response.status_code == 401:
            print("\n Error: Invalid API key. Verify your credentials.")
        else:
            print(f"\n Error: Server responded with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"\n Connection error: {e}")

if __name__ == "__main__":
    print("--- CLI Weather App ---")
    while True:
        user_input = input("Enter city name (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Exiting weather app. Goodbye!")
            break
        elif user_input:
            get_weather(user_input)