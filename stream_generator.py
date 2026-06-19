import pandas as pd
import json
import time

df = pd.read_csv("data/ridepulse_processed.csv")

for _, row in df.iterrows():
    event = row.to_dict()
    
    print(json.dumps(event, default=str))
    
    # simulate real-time rides
    time.sleep(1)
