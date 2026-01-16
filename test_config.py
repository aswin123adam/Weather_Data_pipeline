from src.settings import config

print("Weather API Key:", config.weather_config.api_key[:10] + "xxx" if config.weather_config.api_key else "Not Set")
print("Postgres User:", config.postgres.user)
print("Postgres Host:", config.postgres.host)
print("AWS S3 Bucket:", config.aws.s3_bucket)
print("Cities",config.datapipeline.cities)
print("\n")
print("Config Validation:", config.validate())