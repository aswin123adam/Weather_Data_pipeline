from datetime import datetime
from typing import List, Dict

class WeatherDataTransformer:
    def transform_weather_data(self, raw_data: Dict) -> List[Dict]:

        weather_records = []

        for _, data in raw_data.items():
            weather_record = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'description': data['weather'][0]['description'],
                'recorded_at': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            weather_records.append(weather_record)
        return weather_records