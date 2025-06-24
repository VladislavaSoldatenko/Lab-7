import requests
import json

key = "18e0457cc19d7f512ca4c07b26405a40"
city_name = "Stavropol"
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
result = json.loads(response.text)
print(f"Сейчас в {city_name} \nтемпература: {result['main']['temp'] - 273.15} \nвлажность: {result['main']['humidity']} \nдавление: {result['main']['pressure']}")