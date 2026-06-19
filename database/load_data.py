import sqlite3
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import DATABASE_PATH, PROCESSED_DATA_PATH, TABLE_FACT_TRIPS, TABLE_KPI_HOURLY, TABLE_KPI_PASSENGER
from utils.logger import setup_logger

# Setup logger
logger = setup_logger('database_loader')

# Connect/Create database
conn = sqlite3.connect(DATABASE_PATH)

logger.info("Loading data into SQLite database...")

# Load data
df = pd.read_csv(PROCESSED_DATA_PATH)
logger.info(f"Loaded {len(df):,} records from CSV")

# Store table
df.to_sql(
    TABLE_FACT_TRIPS,
    conn,
    if_exists="replace",
    index=False
)

logger.info(f"✅ Loaded {len(df):,} trips into {TABLE_FACT_TRIPS} table")

# Create aggregated KPIs table
logger.info("Creating KPI tables...")

# Revenue by hour
revenue_by_hour = df.groupby("pickup_hour").agg({
    "total_amount": "sum",
    "VendorID": "count",
    "fare_amount": "mean",
    "trip_distance": "mean",
    "average_speed": "mean"
}).reset_index()

revenue_by_hour.columns = [
    "pickup_hour", "total_revenue", "trip_count", 
    "avg_fare", "avg_distance", "avg_speed"
]

revenue_by_hour.to_sql(
    TABLE_KPI_HOURLY,
    conn,
    if_exists="replace",
    index=False
)

logger.info(f"✅ Created {TABLE_KPI_HOURLY} table with {len(revenue_by_hour)} records")

# Passenger distribution
passenger_stats = df.groupby("passenger_count").agg({
    "VendorID": "count",
    "total_amount": "sum",
    "fare_amount": "mean"
}).reset_index()

passenger_stats.columns = [
    "passenger_count", "trip_count", "total_revenue", "avg_fare"
]

passenger_stats.to_sql(
    TABLE_KPI_PASSENGER,
    conn,
    if_exists="replace",
    index=False
)

logger.info(f"✅ Created {TABLE_KPI_PASSENGER} table with {len(passenger_stats)} records")

conn.close()

logger.info("🎉 Database setup complete!")
logger.info(f"Database file: {DATABASE_PATH}")
