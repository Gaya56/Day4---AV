import datetime
import logging
from ..fabric_real_time_ingest import fetch_webex_data, send_to_event_hub  # Adjust path if needed
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info('WebexIngestionFunction triggered at %s', utc_timestamp)

    # Fetch data from Webex API and send to Event Hub
    data = fetch_webex_data()
    if data:
        send_to_event_hub(data)
        logging.info("Data sent to Event Hub successfully.")
    else:
        logging.warning("No data fetched from Webex API")
