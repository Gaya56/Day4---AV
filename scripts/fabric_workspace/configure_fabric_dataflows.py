import requests
import os

# Assume you have Azure authentication setup
def configure_dataflows():
    fabric_url = os.getenv("FABRIC_API_URL")
    auth_token = os.getenv("FABRIC_AUTH_TOKEN")
    
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
    # Configure dataflow with required parameters
    dataflow_payload = {
        # Define dataflow specifics
        "name": "ErrorAnalysisDataflow",
        "parameters": {
            "dataSource": "ErrorMessages",
            "outputTarget": "Data Activator or Power BI"
        }
    }
    
    response = requests.post(f"{fabric_url}/dataflows", headers=headers, json=dataflow_payload)
    if response.status_code == 201:
        print("Dataflow configured successfully")
    else:
        print("Failed to configure dataflow:", response.text)

if __name__ == "__main__":
    configure_dataflows()
