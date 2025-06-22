import requests 
import pandas as pd
from datetime import datetime , timedelta , timezone
import os

API_KEY = os.getenv("AQI_API_KEY")
CITY = 'Coventry'


def fetch_data():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=51.5074&lon=0.1278&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['list']


def process_data(raw_data):
    rows = []
    for entry in raw_data:
        dt = datetime.fromtimestamp(entry['dt'], tz= timezone.utc)
        pm2_5 = entry['components']['pm2_5']
        pm10 = entry['components']['pm10']
        no2 = entry['components']['no2']
        o3 = entry['components']['o3']
        aqi = entry['main']['aqi']
        rows.append([dt, pm2_5, pm10, no2, o3, aqi])
    df = pd.DataFrame(rows, columns=['datetime', 'pm2_5', 'pm10', 'no2', 'o3', 'aqi'])
    return df


def main():
    raw = fetch_data()
    df = process_data(raw)
    df.to_csv("features/aqi_features.csv", index=False)

if __name__ == "__main__":
    main()