import os 
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import List

load_dotenv()

@dataclass
class WeatherConfig:
    api_key: str
    base_url: str="http://api.openweathermap.org/data/2.5/"

@dataclass
class PostgresConfig:
    user: str
    password: str
    host: str
    port: int
    database: str

@dataclass
class AWSConfig:
    access_key: str
    secret_key: str
    region: str
    s3_bucket: str

@dataclass
class DatapipelineConfig:
    cities: List[str]

class Config:
    def __init__(self):
        self.weather_config = WeatherConfig(
            api_key=os.getenv("OPENWEATHERAPI_KEY","")
        )
        self.postgres = PostgresConfig(
            user=os.getenv("POSTGRES_USER",""),
            password=os.getenv("POSTGRES_PASSWORD",""),
            host=os.getenv("POSTGRES_HOST","localhost"),
            port=int(os.getenv("POSTGRES_PORT","5432")),
            database=os.getenv("POSTGRES_DB","weather_db")
        )
        self.aws = AWSConfig(
            access_key=os.getenv("AWS_ACCESS_KEY",""),
            secret_key=os.getenv("AWS_SECRET_KEY",""),
            region=os.getenv("AWS_REGION",""),
            s3_bucket=os.getenv("AWS_S3_BUCKET","")
        )
        self.datapipeline = DatapipelineConfig(
            cities=os.getenv("CITIES","").split(",")
        )

    def validate(self) -> bool:
        if not self.weather_config.api_key:
            print("ERROR: Weather API key is required.")
            return False
        if not self.postgres.password:
            print("ERROR: Postgres password is required.")
            return False
        return True


config = Config()
