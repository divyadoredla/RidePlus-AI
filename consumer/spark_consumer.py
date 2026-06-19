import pandas as pd

# Load processed data
df = pd.read_csv("data/ridepulse_processed.csv")

print("=" * 50)
print("RidePulse Analytics Dashboard")
print("=" * 50)

# Basic Statistics
print("\n📊 Basic Statistics:")
print(f"Total Trips: {len(df):,}")
print(f"Average Fare: ${df['fare_amount'].mean():.2f}")
print(f"Average Distance: {df['trip_distance'].mean():.2f} miles")
print(f"Average Trip Duration: {df['trip_duration_minutes'].mean():.2f} minutes")
print(f"Total Revenue: ${df['total_amount'].sum():,.2f}")

# Revenue by Hour
print("\n💰 Revenue by Hour:")
revenue_by_hour = df.groupby("pickup_hour")["total_amount"].sum().sort_values(ascending=False)
print(revenue_by_hour.head(10))

# Trips per Hour
print("\n🚖 Trips per Hour:")
trips_by_hour = df.groupby("pickup_hour").size().sort_values(ascending=False)
print(trips_by_hour.head(10))

# Passenger Distribution
print("\n👥 Passenger Distribution:")
passenger_dist = df["passenger_count"].value_counts().sort_index()
print(passenger_dist)

# Payment Type Analysis
print("\n💳 Payment Type Distribution:")
payment_dist = df.groupby("payment_type")["total_amount"].agg(['count', 'sum', 'mean'])
payment_dist.columns = ['Trips', 'Total Revenue', 'Avg Fare']
print(payment_dist)

# Speed Analysis
print("\n⚡ Average Speed by Hour:")
speed_by_hour = df.groupby("pickup_hour")["average_speed_mph"].mean().sort_values(ascending=False)
print(speed_by_hour.head(10))

print("\n" + "=" * 50)
