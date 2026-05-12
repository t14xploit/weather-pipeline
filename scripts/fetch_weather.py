import requests
import json
from datetime import datetime

LATITUDE = 59.3293
LONGITUDE = 18.0686

url = (
f"https://api.open-meteo.com/v1/forecast?"
f"latitude={LATITUDE}&longitude={LONGITUDE}"
f"&current_weather=true"
)

response = requests.get(url)
response.raise_for_status()

data = response.json()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"data/raw/weather_{timestamp}.json"

with open(filename, "w") as f:
	json.dump(data, f, indent=2)

print(f"Saved weather data to {filename}")
