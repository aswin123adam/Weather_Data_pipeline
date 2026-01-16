import psycopg2
from typing import List, Dict
from config.settings import config

class PostgresLoader:
    def __init__(self):
        self.conn = psycopg2.connect(
            user=config.postgres.user,
            password=config.postgres.password,
            host=config.postgres.host,
            port=config.postgres.port,
            database=config.postgres.database
        )

    def create_table(self):
        create_table_query= """
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            country VARCHAR(10),
            temperature DECIMAL(5,2),
            feels_like DECIMAL(5,2),
            humidity INT,
            pressure INT,
            wind_speed DECIMAL(5,2),
            weather_description VARCHAR(255),
            recorded_at TIMESTAMP
        );
        """
        with self.conn.cursor() as cur:
            cur.execute(create_table_query)
        self.conn.commit()
        print("Table Created Successfully")

    def load(self, records: List[Dict]):
        insert_query = """
        INSERT INTO weather_data (
            city, country, temperature, feels_like, humidity, pressure,
            wind_speed, weather_description, recorded_at
        ) VALUES (
            %(city)s, %(country)s, %(temperature)s, %(feels_like)s,
            %(humidity)s, %(pressure)s, %(wind_speed)s,
            %(weather_description)s, %(recorded_at)s
        );
        """
        with self.conn.cursor() as cur:
            for record in records:
                cur.execute(insert_query, record)
        self.conn.commit()
        print(f"{len(records)} records inserted successfully.")

    def close(self):
        self.conn.close()
        print("Database connection closed.")