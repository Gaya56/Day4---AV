import os
import json
import requests
from azure.eventhub import EventHubProducerClient, EventData

# Load configuration from the JSON file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../../config/webex_ingest_config.json")
with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)

# Webex API and Event Hub configuration
WEBEX_API_URL = config["webex_api"]["base_url"]
WEBEX_API_KEY = config["webex_api"]["api_key"]
EVENT_HUB_CONN_STR = config["event_hub"]["connection_string"]
EVENT_HUB_NAME = config["event_hub"]["name"]

# Fetch data from Webex API
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

# Send data to Event Hub
def send_to_event_hub(data):
    producer = EventHubProducerClient.from_connection_string(conn_str=EVENT_HUB_CONN_STR, eventhub_name=EVENT_HUB_NAME)
    with producer:
        event_data_batch = producer.create_batch()
        for record in data:
            event_data_batch.add(EventData(json.dumps(record)))
        producer.send_batch(event_data_batch)
    print("Data sent to Event Hub")

# Main function to fetch and stream data
def main():
    data = fetch_webex_data()
    if data:
        send_to_event_hub(data)
    else:
        print("No data fetched from Webex API")

# Run the main function
if __name__ == "__main__":
    main()
