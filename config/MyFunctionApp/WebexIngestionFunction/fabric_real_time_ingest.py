import os
import json
import requests
from azure.eventhub import EventHubProducerClient, EventData

# Load configuration from the config file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config/webex_ingest_config.json")
with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)

# Webex API configuration
WEBEX_API_URL = config["webex_api"]["base_url"]
WEBEX_API_KEY = config["webex_api"]["api_key"]

# Event Hub configuration
EVENT_HUB_CONN_STR = config["event_hub"]["connection_string"]
EVENT_HUB_NAME = config["event_hub"]["name"]

# Fabric Real-Time Analytics configuration
FABRIC_ENDPOINT = config["fabric_real_time_analytics"]["endpoint"]

def fetch_webex_data():
    headers = {
        "Authorization": f"Bearer {WEBEX_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(WEBEX_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Failed to retrieve data from Webex API. Status code: {response.status_code}")
        return None

def send_to_event_hub(data):
    producer = EventHubProducerClient.from_connection_string(conn_str=EVENT_HUB_CONN_STR, eventhub_name=EVENT_HUB_NAME)
    with producer:
        event_data_batch = producer.create_batch()
        for record in data:
            event_data_batch.add(EventData(json.dumps(record)))
        producer.send_batch(event_data_batch)
    print("Data sent to Event Hub")

def send_to_fabric_real_time_analytics(data):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(FABRIC_ENDPOINT, json=data, headers=headers)
    if response.status_code == 200:
        print("Data sent to Fabric Real-Time Analytics successfully.")
    else:
        print(f"Failed to send data to Fabric Real-Time Analytics. Status code: {response.status_code}")

def main():
    data = fetch_webex_data()
    if data:
        # Send data to both Event Hub and Fabric Real-Time Analytics
        send_to_event_hub(data)
        send_to_fabric_real_time_analytics(data)
    else:
        print("No data fetched from Webex API")

# Execute the main function
if __name__ == "__main__":
    main()
