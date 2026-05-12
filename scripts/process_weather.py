import json
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
processed_folder = Path("data/processed")

processed_folder.mkdir(exist_ok=True)

files = sorted(raw_folder.glob("weather_*.json"))

if not files:
	raise Exception("No raw weather files found")

latest_file = files[-1]

with open(latest_file) as f:
	data = json.load(f)

weather = data["current_weather"]

row = {
	"temperature": weather["temperature"],
	"windspeed": weather["windspeed"],
	"winddirection": weather["winddirection"],
	"time": weather["time"]
}

csv_file = processed_folder / "weather_history.cvs"

new_df = pd.DataFrame([row])

if csv_file.exists():
	existing_df = pd.read_csv(csv_file)
	combined_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
	combined_df = new_df

combined_df.to_csv(csv_file, index=False)

print(f"Saved processed data to {csv_file}")
