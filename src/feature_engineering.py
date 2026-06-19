import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

# Convert datetime columns
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Trip duration in minutes
df['trip_duration'] = (
    df['tpep_dropoff_datetime']
    - df['tpep_pickup_datetime']
).dt.total_seconds() / 60

# Pickup hour
df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour

# Pickup weekday
df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.day_name()

# Average speed
df['average_speed'] = (
    df['trip_distance'] /
    (df['trip_duration'] / 60)
)

# Remove infinite values
df = df[df['average_speed'] != float('inf')]

# Save processed data
df.to_csv("data/ridepulse_processed.csv", index=False)

print("Feature engineering completed!")
