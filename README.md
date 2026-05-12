# Weather Data Pipeline

This project is a simple automated data pipeline that fetches weather data, processes it, and stores it in a structured format. It demonstrates basic backend/data engineering concepts such as automation, scripting, logging, and data handling.

---

## What it does

1. Fetches weather data from a public API
2. Saves raw JSON data locally
3. Processes the data into a CSV format
4. Logs execution results
5. Can be automated using a shell script or cron
6. Can run inside a Docker container

---

## Technologies used

- Python
- Bash
- Linux
- Git
- pandas
- requests
- cron (automation)
- Docker (optional)

---

## Project structure
```
weather-pipeline/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── logs/
│
├── scripts/
│ ├── fetch_weather.py
│ ├── process_weather.py
│ └── run_pipeline.sh
│
├── Dockerfile
├── requirements.txt
└── README.md

```

---


## How to run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Run pipeline manually
```bash
scripts/run_pipeline.sh
```
### 3. (Optional) Run individual steps
``` bash
python scripts/fetch_weather.py
python scripts/process_weather.py

```

## What I learned

How to work with APIs in Python
How to process and structure raw data
How to use Linux scripts for automation
How logging helps debug workflows
How Git is used in real projects
Basic idea of data pipelines used in production systems

## Future improvements

Add database storage (SQLite or PostgreSQL)
Improve logging system
Add unit tests
Containerize with Docker
Schedule with cron for full automation
