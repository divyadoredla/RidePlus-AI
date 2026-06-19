import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import PROCESSED_DATA_PATH
from utils.logger import setup_logger

# Setup logger
logger = setup_logger('analytics_engine')

logger.info("Loading processed data...")

try:
    df = pd.read_csv(PROCESSED_DATA_PATH)
    logger.info(f"Loaded {len(df):,} records")

    print("=" * 60)
    print("🚖 RidePulse Analytics Engine")
    print("=" * 60)

    # Basic Metrics
    print("\n📊 Basic Metrics:")
    print(f"Average Fare: ${df['fare_amount'].mean():.2f}")
    print(f"Average Distance: {df['trip_distance'].mean():.2f} miles")
    print(f"Average Speed: {df['average_speed'].mean():.2f} mph")
    print(f"Total Revenue: ${df['total_amount'].sum():,.2f}")
    print(f"Total Trips: {len(df):,}")

    # Revenue by hour
    print("\n💰 Revenue by Hour:")
    revenue_hour = (
        df.groupby("pickup_hour")["total_amount"]
        .sum()
        .sort_values(ascending=False)
    )
    print(revenue_hour.head(10))

    # Trips per hour
    print("\n🚕 Trips per Hour:")
    trips_hour = df.groupby("pickup_hour").size().sort_values(ascending=False)
    print(trips_hour.head(10))

    # Passenger distribution
    print("\n👥 Passenger Distribution:")
    passenger_dist = df["passenger_count"].value_counts().sort_index()
    print(passenger_dist)

    # Peak hours
    print("\n⏰ Top 5 Peak Hours (by trips):")
    top_hours = trips_hour.head(5)
    for hour, count in top_hours.items():
        print(f"  Hour {hour:02d}:00 - {count} trips")

    # Average fare by passenger count
    print("\n💵 Average Fare by Passenger Count:")
    avg_fare_passenger = df.groupby("passenger_count")["fare_amount"].mean().sort_index()
    print(avg_fare_passenger)

    print("\n" + "=" * 60)
    
    logger.info("Analytics completed successfully")

except FileNotFoundError as e:
    logger.error(f"Data file not found: {PROCESSED_DATA_PATH}")
except Exception as e:
    logger.error(f"Error during analysis: {e}")
