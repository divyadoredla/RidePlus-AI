import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("ridepulse.db")

print("=" * 60)
print("RidePulse SQLite Query Examples")
print("=" * 60)

# Query 1: Top 5 revenue hours
print("\n💰 Top 5 Revenue Hours:")
query1 = """
SELECT 
    pickup_hour,
    total_revenue,
    trip_count,
    ROUND(avg_fare, 2) as avg_fare
FROM kpi_hourly
ORDER BY total_revenue DESC
LIMIT 5
"""
result1 = pd.read_sql(query1, conn)
print(result1)

# Query 2: Passenger distribution
print("\n👥 Passenger Distribution:")
query2 = """
SELECT 
    passenger_count,
    trip_count,
    ROUND(total_revenue, 2) as total_revenue,
    ROUND(avg_fare, 2) as avg_fare
FROM kpi_passenger
ORDER BY passenger_count
"""
result2 = pd.read_sql(query2, conn)
print(result2)

# Query 3: Peak vs Off-Peak
print("\n⏰ Peak vs Off-Peak Analysis:")
query3 = """
SELECT 
    CASE 
        WHEN pickup_hour BETWEEN 7 AND 9 THEN 'Morning Peak'
        WHEN pickup_hour BETWEEN 17 AND 19 THEN 'Evening Peak'
        ELSE 'Off-Peak'
    END as time_period,
    SUM(trip_count) as total_trips,
    ROUND(SUM(total_revenue), 2) as total_revenue,
    ROUND(AVG(avg_fare), 2) as avg_fare
FROM kpi_hourly
GROUP BY time_period
ORDER BY total_revenue DESC
"""
result3 = pd.read_sql(query3, conn)
print(result3)

# Query 4: Sample trips
print("\n🚖 Sample Trips:")
query4 = """
SELECT 
    tpep_pickup_datetime,
    passenger_count,
    trip_distance,
    fare_amount,
    total_amount,
    pickup_hour
FROM fact_trips
LIMIT 5
"""
result4 = pd.read_sql(query4, conn)
print(result4)

conn.close()

print("\n" + "=" * 60)
