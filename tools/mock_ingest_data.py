import sys
import random

import requests
import time
from datetime import datetime

API_URL = 'http://127.0.0.1:8000/api/sensors/data'


def get_payload():
    # 20% anomaly
    if random.random() < 0.2:
        temperature = round(random.uniform(40, 100), 2)
        humidity = round(random.uniform(40, 100), 2)
        air_quality = round(random.uniform(40, 100), 2)
        is_anomaly = True
    else:
        temperature = round(random.uniform(20, 30), 2)
        humidity = round(random.uniform(20, 30), 2)
        air_quality = round(random.uniform(20, 30), 2)
        is_anomaly = False

    return is_anomaly, {
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "air_quality": air_quality,
    }


def call_api(api_key):
    try:
        is_anomaly, payload = get_payload()
        response = requests.post(API_URL, headers={'X-Api-Key': api_key}, json=payload)
        print(f'Anomaly: {is_anomaly} Status: {response.status_code}, Response: {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Usage: mock_ingest_data.py <api_key>')
    api_key = sys.argv[1]
    while True:
        call_api(api_key=api_key)
        time.sleep(3)
