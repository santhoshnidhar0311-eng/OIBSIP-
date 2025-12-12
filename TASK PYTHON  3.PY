import requests

print("======= Weather Info Tool =======")

api_key = "3e4ddc1c955872270245060f9a95f078"   # your key

city_name = input("Type the city name: ")

link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

try:
    reply = requests.get(link)
    info = reply.json()

    if info.get("cod") != 200:
        print("Could not fetch weather data:", info.get("message"))
    else:
        condition = info["weather"][0]["description"]
        temp_now = info["main"]["temp"]
        feels_like = info["main"]["feels_like"]
        hum = info["main"]["humidity"]

        print("\n--- Weather Details ---")
        print("Location:", city_name)
        print("Weather:", condition.capitalize())
        print("Temperature:", temp_now, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Humidity:", hum, "%")

except Exception as err:
    print("Unexpected error occurred:", err)
