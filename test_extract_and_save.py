from extract.weather_extractor import WeatherExtractor
from storage.s3_storage import WeatherS3Storage

extract_weather = WeatherExtractor()
s3_storage = WeatherS3Storage()

weather_data = extract_weather.get_weather_for_all_cities()
s3_path = s3_storage.save_weather_data(weather_data)

print(f"Weather data for all cities saved to: {s3_path}")