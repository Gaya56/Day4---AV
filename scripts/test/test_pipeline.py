#***This script will simulate data ingestion to Event Hub, allowing us to test the pipeline end-to-end.
#Explanation:

    #***This script generates sample device data, some with error codes and some without, to simulate both normal and error conditions.
    #***It sends the data to Event Hub, allowing us to test both Stream Analytics and Fabric processing.
#*

import os
import json
import time
from azure.eventhub import EventHubProducerClient, EventData
from datetime import datetime

# Configuration
EVENT_HUB_CONN_STR = os.getenv("EVENT_HUB_CONN_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

# Simulate device data
def generate_test_data():
    # Generate some dummy data with random error codes
    devices = [
        {"device_id": "device1", "status": "active", "city": "Calgary", "error_code": None},
        {"device_id": "device2", "status": "inactive", "city": "Toronto", "error_code": "ERR01"},
        {"device_id": "device3", "status": "active", "city": "Calgary", "error_code": "ERR02"},
    ]
    for device in devices:
        device["last_activity"] = datetime.utcnow().isoformat()
    return devices

# Send data to Event Hub
def send_to_event_hub(data):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONN_STR,
        eventhub_name=EVENT_HUB_NAME
    )
    with producer:
        event_data_batch = producer.create_batch()
        for record in data:
            event_data_batch.add(EventData(json.dumps(record)))
        producer.send_batch(event_data_batch)
    print("Test data sent to Event Hub.")

if __name__ == "__main__":
    # Generate and send test data
    test_data = generate_test_data()
    send_to_event_hub(test_data)
    print("Pipeline test initiated.")
