import pandas as pd
import json
import time
from kafka import KafkaProducer

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8')
)

# Read processed dataset
df = pd.read_csv("../data/ridepulse_processed.csv")

# Add trip_id if missing
if "trip_id" not in df.columns:
    df["trip_id"] = range(1, len(df)+1)

print("Starting stream...")

for _, row in df.iterrows():

    event = row.to_dict()

    producer.send(
        "trip_events",
        value=event
    )

    print(f"Sent Trip ID: {event['trip_id']}")

    # simulate real-time rides
    time.sleep(1)

producer.flush()
