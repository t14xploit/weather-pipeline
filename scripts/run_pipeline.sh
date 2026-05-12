#!/bin/bash

LOGFILE="logs/pipeline.log"

mkdir -p logs
{

echo "Starting weather pipeline...."
echo "============================"

python scripts/fetch_weather.py
python scripts/process_weather.py

echo "Pipeline finishes successfully"
} >> "$LOGFILE" 2>&1
