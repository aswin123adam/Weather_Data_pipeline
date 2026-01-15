from extract.weather_extractor import WeatherExtractor

extractor = WeatherExtractor()

# city = "Dublin,IE"
# weather_data = extractor.get_weather(city)
# if weather_data:
#     print(f"Weather data for {city}:")
#     print(weather_data)
# else:
#     print("cannot identify city!")


all_weather_data = extractor.get_weather_for_all_cities()

print(f"Weather Data for all {len(all_weather_data)} cities:\n")

for city, data in all_weather_data.items():
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"{city}: {temp}°C, {description}")