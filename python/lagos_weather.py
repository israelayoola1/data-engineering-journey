import csv
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=6.45&longitude=3.39&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Africa/Lagos"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Could not fetch weather data: {e}")
    raise SystemExit(1)

data = response.json()
daily = data["daily"]
rows = []

for i in range(len(daily["time"])):
    row = {
        "date": daily["time"][i],
        "temp_max": daily["temperature_2m_max"][i],
        "temp_min": daily["temperature_2m_min"][i],
        "precipitation": daily["precipitation_sum"][i],
    }
    rows.append(row)

with open("lagos_weather.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "temp_max", "temp_min", "precipitation"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} rows to lagos_weather.csv")