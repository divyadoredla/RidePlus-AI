import pandas as pd

# Load data
df = pd.read_parquet("../yellow_tripdata_2025-01.parquet")

# Remove null values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert datetime columns
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Remove invalid values
df = df[df['fare_amount'] > 0]
df = df[df['trip_distance'] > 0]

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaning completed!")
