
import requests
import json

API_Key = "0dfcb3214e298b88fd4ac978c25e7714"
city_name = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}"
response = requests.get(url)
res = response.json()

if res["cod"] != "404":
    data = res["main"]
    live_temperature = data["temp"]
    live_pressure = data["pressure"]
    desc = res["weather"]
    weather_description = desc[0]["description"]
    print("Temperature (in Kelvin scale): " + str(live_temperature))
    print("Pressure: " + str(live_pressure))
    print("Description: " + str(weather_description))

else:
    print("Please enter a valid city name")