import pandas as pd

df = pd.read_csv("data/ridepulse_processed.csv")

# Example analytics
print("Average Fare:", df["fare_amount"].mean())
print("Average Distance:", df["trip_distance"].mean())

revenue_by_hour = df.groupby("pickup_hour")["total_amount"].sum()

print(revenue_by_hour)
