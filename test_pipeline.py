from extract.weather_extractor import WeatherExtractor
from storage.s3_storage import WeatherS3Storage
from transform.transform_data import WeatherDataTransformer
from loader.postgres_loader import PostgresLoader

extract_weather = WeatherExtractor()
s3_storage = WeatherS3Storage()
transformer = WeatherDataTransformer()


weather_data = extract_weather.get_weather_for_all_cities()
print("Weather data Extracted!\n")
s3_path = s3_storage.save_weather_data(weather_data)
print(f"Weather data saved to Local and S3 at: {s3_path}")
transformed_data = transformer.transform_weather_data(weather_data)
print("Transformed Weather Data is ready to be loaded to Postgres \n")
# print(transformed_data)

# Testing PostgresLoader
loader = PostgresLoader()
print("Connected to Postgres Successfully")
loader.create_table()
print("Table creation verified.")
loader.load(transformed_data)
print("Data loaded to PostgreSQL!")
loader.close()
print("PostgresLoader connnection terminated successfully.")