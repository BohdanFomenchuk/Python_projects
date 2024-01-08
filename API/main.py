import requests

parameters = {
    "lat": 50.433261,
    "lng": 30.426140
}
response = requests.get("https://api.sunrise-sunset.org/json?lat=50.433261&lng=30.426140&formatted=0")
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(':')[0]
sunset = data["results"]["sunset"].split("T")[1].split(':')[0]
print(sunset)
