import os
import requests
import json
from azure.eventhub import EventHubProducerClient, EventData
import logging

# Configurations
WEBEX_API_URL = "https://webexapis.com/v1/devices"
WEBEX_API_KEY = os.getenv("WEBEX_API_KEY")
EVENT_HUB_CONN_STR = os.getenv("EVENT_HUB_CONN_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")
FABRIC_ENABLED = os.getenv("FABRIC_ENABLED", "false").lower() == "true"
FABRIC_ENDPOINT = os.getenv("FABRIC_ENDPOINT")  # Only used if FABRIC_ENABLED is True

# Function to fetch data from the Cisco Webex API
def fetch_webex_data():
    headers = {
        "Authorization": f"Bearer {WEBEX_API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(WEBEX_API_URL, headers=headers)
        response.raise_for_status()
        devices_data = response.json().get("items", [])
        logging.info(f"Fetched {len(devices_data)} records from Webex API.")
        return devices_data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from Webex API: {e}")
        return None

# Function to send data to Azure Event Hub
def send_to_event_hub(data):
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONN_STR,
            eventhub_name=EVENT_HUB_NAME
        )
        with producer:
            event_data_batch = producer.create_batch()
            for record in data:
                event_data_batch.add(EventData(json.dumps(record)))
            producer.send_batch(event_data_batch)
        logging.info("Data sent to Event Hub successfully.")
    except Exception as e:
        logging.error(f"Error sending data to Event Hub: {e}")

# Function to send data to Microsoft Fabric Real-Time Analytics (if available)
def send_to_fabric_real_time_analytics(data):
    if not FABRIC_ENDPOINT:
        logging.error("FABRIC_ENDPOINT is not defined.")
        return

    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(FABRIC_ENDPOINT, json=data, headers=headers)
        if response.status_code == 200:
            logging.info("Data sent to Fabric Real-Time Analytics successfully.")
        else:
            logging.error(f"Failed to send data to Fabric: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending data to Fabric Real-Time Analytics: {e}")

# Main ingestion function to be called by the Azure Function
def main():
    data = fetch_webex_data()
    if data:
        if FABRIC_ENABLED:
            send_to_fabric_real_time_analytics(data)
        else:
            send_to_event_hub(data)
    else:
        logging.warning("No data fetched from Webex API.")
