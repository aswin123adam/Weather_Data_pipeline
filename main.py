#main orchectration file to run the entire pipeline
from src.weather_extractor import WeatherExtractor
from src.s3_storage import WeatherS3Storage
from src.transform_data import WeatherDataTransformer
from src.postgres_loader import PostgresLoader

def run_pipeline():
    # Initialize components
    extractor = WeatherExtractor()
    s3_storage = WeatherS3Storage(use_s3=True)
    transformer = WeatherDataTransformer()
    loader = PostgresLoader()

    print('='*50)
    print("WEATHER DATA PIPELINE")
    print('='*50)
    # Extract weather data
    print("Extracting weather data... [1/4]")
    weather_data = extractor.get_weather_for_all_cities()
    print("Weather data extracted successfully.")

    # Storage to S3
    print("Storing weather data to S3... [2/4]")
    s3_path = s3_storage.save_weather_data(weather_data)
    print(f"Weather data saved to S3 at: {s3_path}")

    # Transform data
    print("Transforming weather data... [3/4]")
    transformed_data = transformer.transform_weather_data(weather_data)
    print("Weather data transformed and ready for loading into Postgres.")

    # Load data into Postgres
    loader.create_table()
    loader.load(transformed_data)
    print("Transformed data loaded into Postgres. [4/4]")

    # Close Postgres connection
    loader.close()

    print('='*50)
    print("PIPELINE COMPLETED SUCCESSFULLY!!")
    print('='*50)

if __name__ == "__main__":
    run_pipeline()