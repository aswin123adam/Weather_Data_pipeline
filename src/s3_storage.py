import os
import json
from datetime import datetime
import boto3
from src.settings import config

class WeatherS3Storage:
    def __init__ (self, storage_path: str = "/tmp/weather_data", use_s3: bool = False):
        self.storage_path = storage_path
        self.use_s3 = use_s3
        os.makedirs(self.storage_path, exist_ok=True)

        if self.use_s3:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=config.aws.access_key,
                aws_secret_access_key=config.aws.secret_key,
                region_name=config.aws.region
            )
            self.s3_bucket = config.aws.s3_bucket
    
    def save_weather_data(self, weather_data: dict) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        filename = f"weather_data_{timestamp}.json"
        file_path = os.path.join(self.storage_path,filename)

        with open(file_path,"w", encoding="utf-8") as f:
            json.dump(weather_data,f,indent=4, ensure_ascii=False)
        if self.use_s3:
            s3_key = f"/raw/weather_data/{filename}"
            self.s3_client.upload_file(file_path,self.s3_bucket,s3_key)
            return f"s3://{self.s3_bucket}/{s3_key }"
        return file_path