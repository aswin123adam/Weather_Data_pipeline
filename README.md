# 🌦️ Weather Data Pipeline

An end-to-end ETL pipeline that extracts weather data from OpenWeatherMap API, stores raw data in AWS S3, transforms it, and loads it into PostgreSQL for analytics.

## 🏗️ Architecture
```
OpenWeatherMap API → Extract → AWS S3 (Raw) → Transform → PostgreSQL
```

## 🛠️ Tech Stack

- **Python** - Core language
- **PostgreSQL** - Data warehouse
- **AWS S3** - Raw data storage
- **Docker** - Database containerization
- **boto3** - AWS SDK
- **psycopg2** - PostgreSQL adapter

## 📁 Project Structure
```
weather_pipeline/
├── src/
│   ├── __init__.py
│   ├── settings.py
│   ├── weather_extractor.py
│   ├── s3_storage.py
│   ├── transform_data.py
│   └── postgres_loader.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```
There are 2 test files added namely test_config.py and test_pipeline.py (ignore).
Please use them to check your configurations and the status of your pipeline as per requirement.

## ⚙️ Setup

### 1. Clone Repository
```bash
git clone https://github.com/aswin123adam/Weather_Data_pipeline.git
cd weather-pipeline
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 3. Configure Environment

Create `.env` file:
```
OPENWEATHER_API_KEY=your_api_key
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5433
POSTGRES_DB=weather_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=eu-west-1
AWS_S3_BUCKET=your-bucket-name
CITIES=Dublin,IE;Cork,IE;Galway,IE
```

### 4. Start PostgreSQL (Docker)
```bash
docker run --name weather-postgres -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=weather_db -p 5433:5432 -d postgres:15
```

### 5. Run Pipeline
```bash
python main.py
```

## 📊 Sample SQL Analytics
```sql
-- Average temperature per city
SELECT city, ROUND(AVG(temperature)::numeric, 2) as avg_temp 
FROM weather_data 
GROUP BY city 
ORDER BY avg_temp DESC;

-- Weather conditions distribution
SELECT weather_description, COUNT(*) as count 
FROM weather_data 
GROUP BY weather_description 
ORDER BY count DESC;

-- Temperature range per city
SELECT city, 
       MIN(temperature) as min_temp, 
       MAX(temperature) as max_temp
FROM weather_data
GROUP BY city;
```

## 🚀 Future Improvements

- Add Airflow for scheduling
- Create dashboard with Streamlit
- Add data quality checks
- Deploy to AWS EC2

## 📝 License

MIT