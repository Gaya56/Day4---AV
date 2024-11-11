import logging
import azure.functions as func
from ..pipeline.ingest.fabric_real_time_ingest import main as run_ingestion

def main(mytimer: func.TimerRequest) -> None:
    logging.info('WebexIngestionFunction triggered')
    run_ingestion()
    logging.info('WebexIngestionFunction completed')