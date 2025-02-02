import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "7338748e99651dc79c1041867e34a3e0"

weather_params = {
    "lat": 21.145800,
    "lon": 79.088158,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(response.json())
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hours_data in weather_data["list"]:
    condition_code = (hours_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring a umbrella ")


    #sms send by pgone numne r twillo api