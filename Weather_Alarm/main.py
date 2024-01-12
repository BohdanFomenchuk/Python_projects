import requests


api_key = "Your_API_Key"
weather_params = {
    "lat": 50.446336,
    "lon": 30.415258,
    "appid": api_key,
    "cnt": 4
}

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for hour in weather_data["list"]:
    weather_code = (hour["weather"][0]["id"])
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Its better to get an umbrella today")
else:
    print("No need to get an umbrella today")


