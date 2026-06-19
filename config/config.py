import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database configuration
DATABASE_PATH = os.path.join(BASE_DIR, "ridepulse.db")

# Data paths
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_PATH = os.path.join(BASE_DIR, "..", "yellow_tripdata_2025-01.parquet")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "cleaned_data.csv")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "ridepulse_processed.csv")

# Logging configuration
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "ridepulse.log")

# Dashboard configuration
DASHBOARD_PORT = 8501
DASHBOARD_TITLE = "RidePulse - NYC Taxi Analytics Dashboard"

# Stream configuration
STREAM_DELAY = 1  # seconds between events

# Database table names
TABLE_FACT_TRIPS = "fact_trips"
TABLE_KPI_HOURLY = "kpi_hourly"
TABLE_KPI_PASSENGER = "kpi_passenger"
