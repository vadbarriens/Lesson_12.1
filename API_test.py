import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=Moscow&appid={API_KEY}')

lat = response.json()[0]['lat']
lon = response.json()[0]['lon']

print(lat, lon)

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')

print(response.json())