import os
import json
from datetime import datetime

class WeatherS3Storage:
    def __init__ (self, storage_path: str = "/tmp/weather_data"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
    
    def save_weather_data(self, weather_data: dict) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        filename = f"weather_data_{timestamp}.json"
        file_path = os.path.join(self.storage_path,filename)

        with open(file_path,"w", encoding="utf-8") as f:
            json.dump(weather_data,f,indent=4, ensure_ascii=False)
        return file_path
