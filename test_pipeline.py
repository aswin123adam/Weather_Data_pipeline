# from src.weather_extractor import WeatherExtractor
# from src.s3_storage import WeatherS3Storage
# from src.transform_data import WeatherDataTransformer
# from src.postgres_loader import PostgresLoader

# extract_weather = WeatherExtractor()
# s3_storage = WeatherS3Storage()
# transformer = WeatherDataTransformer()


# weather_data = extract_weather.get_weather_for_all_cities()
# print("Weather data Extracted!\n")
# s3_path = s3_storage.save_weather_data(weather_data)
# print(f"Weather data saved to Local and S3 at: {s3_path}")
# transformed_data = transformer.transform_weather_data(weather_data)
# print("Transformed Weather Data is ready to be loaded to Postgres \n")
# # print(transformed_data)

# # Testing PostgresLoader
# loader = PostgresLoader()
# print("Connected to Postgres Successfully")
# loader.create_table()
# print("Table creation verified.")
# loader.load(transformed_data)
# print("Data loaded to PostgreSQL!")
# loader.close()
# print("PostgresLoader connnection terminated successfully.")



from src.weather_extractor import WeatherExtractor
from src.s3_storage import WeatherS3Storage
from src.transform_data import WeatherDataTransformer
from src.postgres_loader import PostgresLoader


def run_pipeline():
    print("="*50)
    print("WEATHER DATA PIPELINE")
    print("="*50)
    
    # Extract
    print("\n[1/4] Extracting weather data...")
    extractor = WeatherExtractor()
    raw_data = extractor.get_weather_for_all_cities()
    print(f"Extracted data for {len(raw_data)} cities")
    
    # Store
    print("\n[2/4] Storing raw data...")
    storage = WeatherS3Storage()
    filepath = storage.save_weather_data(raw_data)
    print(f"Saved to: {filepath}")
    
    # Transform
    print("\n[3/4] Transforming data...")
    transformer = WeatherDataTransformer()
    records = transformer.transform_weather_data(raw_data)
    print(f"Transformed {len(records)} records")
    
    # Load
    print("\n[4/4] Loading to PostgreSQL...")
    loader = PostgresLoader()
    loader.create_table()
    loader.load(records)
    loader.close()
    
    print("\n" + "="*50)
    print("PIPELINE COMPLETE!")
    print("="*50)


if __name__ == "__main__":
    run_pipeline()