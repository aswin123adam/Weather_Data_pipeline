import requests
from src.settings import config
from typing import Optional

class WeatherExtractor:
    def __init__(self):
        self.api_key = config.weather_config.api_key
        self.base_url = config.weather_config.base_url
    def get_weather(self, city:str) -> Optional[dict]:
        url = f"{self.base_url}weather"

        params = {
            "q":city,
            "appid":self.api_key,
            "units":"metric"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Could not fetch weather data for {city} \n Failed wit status code : {response.status_code} ")
            return None
        
    def get_weather_for_all_cities(self) -> dict:
        weather_data = {}
        for city in config.datapipeline.cities:
            data=self.get_weather(city)
            if data:
                weather_data[city]=data
        return weather_data