import pandas as pd
import json
import time
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import PROCESSED_DATA_PATH, STREAM_DELAY
from utils.logger import setup_logger

# Setup logger
logger = setup_logger('stream_generator')

# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

logger.info("RidePulse - Real-time Trip Event Generator")

try:
    df = pd.read_csv(PROCESSED_DATA_PATH)
    logger.info(f"Total trips to stream: {len(df)}")
    logger.info("Starting stream...")
    
    for idx, row in df.iterrows():
        event = row.to_dict()
        
        print(json.dumps(event, default=str))
        
        # simulate real-time rides
        time.sleep(STREAM_DELAY)
        
        if (idx + 1) % 10 == 0:
            logger.info(f"{idx + 1} trips streamed")

except FileNotFoundError as e:
    logger.error(f"Data file not found: {PROCESSED_DATA_PATH}")
except Exception as e:
    logger.error(f"Error during streaming: {e}")
