**dual-pipeline setup**.

### **Next Steps for the Repository**

To finalize the repo for deployment and usage, we’ll:
1. **Add Scripts for Testing and Deployment**: Ensure scripts for seamless deployment and testing.
2. **Organize Documentation**: Provide clear instructions in the README for setting up, deploying, and running the pipeline.

Let’s tackle these one at a time.

---

### **Step 1: Add Deployment and Testing Scripts**

We’ll create two main scripts in the `scripts/` folder:
1. **deploy_all.sh**: A single script to deploy all Azure resources, including Event Hub, Stream Analytics, and Fabric Real-Time Analytics.
2. **test_pipeline.py**: A Python script to test the pipeline end-to-end, simulating Webex API data ingestion and verifying data flow through Event Hub, Stream Analytics, and Fabric.

---

#### **1.1 Create `deploy_all.sh` in `scripts/`

This script will automate the deployment of Azure resources based on the Bicep templates and configurations in the repo.

Add the following code to `scripts/deploy_all.sh`:

```bash
#!/bin/bash
# Deploy all Azure resources for the dual-pipeline setup

# Set resource group and location
RESOURCE_GROUP="<Your-Resource-Group>"
LOCATION="eastus"  # Update as needed

# Deploy Event Hub Namespace and Event Hub
echo "Deploying Event Hub..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file config/eventhub_setup.bicep

# Deploy Stream Analytics Job for general metrics
echo "Deploying Stream Analytics Job..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file config/stream_analytics_setup.bicep

# Deploy Fabric Real-Time Analytics Job for error monitoring
echo "Deploying Fabric Real-Time Analytics Job..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file config/fabric_real_time_analytics_setup.bicep

# Deploy Azure Key Vault for secrets management
echo "Deploying Azure Key Vault..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file security-management/key-vault/key_vault_setup.bicep

echo "Deployment complete."
```

**Explanation**:
- This script automates the deployment of **Event Hub**, **Stream Analytics**, **Fabric Real-Time Analytics**, and **Key Vault** resources in sequence.
- Replace `<Your-Resource-Group>` with your Azure resource group.

---

#### **1.2 Create `test_pipeline.py` in `scripts/`

This script will simulate data ingestion to Event Hub, allowing us to test the pipeline end-to-end.

Add the following code to `scripts/test_pipeline.py`:

```python
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
```

**Explanation**:
- This script generates sample device data, some with error codes and some without, to simulate both normal and error conditions.
- It sends the data to Event Hub, allowing us to test both Stream Analytics and Fabric processing.

---

### **Step 2: Organize Documentation in the README**

Now, let’s add comprehensive setup and usage instructions to `README.md` to guide users on deploying, testing, and understanding the dual-pipeline setup.

---

#### **Add to `README.md`**

```markdown
# Real-Time Device Monitoring Pipeline with Microsoft Fabric

This repository implements a real-time data pipeline for monitoring Cisco Webex devices, using Azure services and Microsoft Fabric for error detection, automation, and insights.

## Architecture Overview

- **Pipeline 1 (General Metrics)**: Ingests all device metrics and routes to Power BI for full visibility.
- **Pipeline 2 (Error Monitoring and Automation)**: Filters error messages for automation and alerting in Microsoft Fabric.

### Repository Structure

```
azure-weather-pipeline/
│
├── config/                              # Configuration and query files
│   ├── data_transform_query.sql         # Query for Stream Analytics (general metrics)
│   ├── error_monitoring_query.sql       # Query for Fabric Real-Time Analytics (error-only)
│   ├── fabric_real_time_analytics_setup.bicep  # Bicep for Fabric job setup
│   ├── stream_analytics_setup.bicep     # Bicep for Stream Analytics setup
│
├── pipeline/                            # Ingestion scripts
│   ├── ingest/
│   │   ├── fabric_real_time_ingest.py   # Script to ingest data from Webex API to Event Hub
│
├── scripts/                             # Deployment and testing scripts
│   ├── deploy_all.sh                    # Script to deploy all resources
│   ├── test_pipeline.py                 # Script to test pipeline with simulated data
│
└── README.md                            # Documentation for setup and usage
```

### Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone <repo-url>
   cd azure-weather-pipeline
   ```

2. **Set Up Environment Variables**  
   - Configure environment variables for your Azure resources in your local environment:
     ```bash
     export EVENT_HUB_CONN_STR='<your-event-hub-connection-string>'
     export EVENT_HUB_NAME='<your-event-hub-name>'
     export WEBEX_API_KEY='<your-webex-api-key>'
     ```

3. **Deploy Resources with `deploy_all.sh`**  
   - Run the deployment script to set up all Azure resources:
     ```bash
     ./scripts/deploy_all.sh
     ```

4. **Test the Pipeline with `test_pipeline.py`**  
   - Run the test script to simulate data flow through Event Hub:
     ```bash
     python scripts/test_pipeline.py
     ```

5. **View Real-Time Data in Power BI**  
   - Open Power BI and connect to the Stream Analytics and Fabric outputs to see all device metrics and error-specific insights in one dashboard.

### Data Flow Summary

1. **Pipeline 1 (General Metrics)**:  
   Webex API ➔ Event Hub ➔ Stream Analytics ➔ Power BI

2. **Pipeline 2 (Error Monitoring)**:  
   Webex API ➔ Event Hub ➔ Fabric Real-Time Analytics ➔ Data Activator (Alerts and Automation)
```

---

### **Summary**

With these additions, the repository now has:
1. **Deployment automation** via `deploy_all.sh`.
2. **Testing capabilities** with `test_pipeline.py` to simulate end-to-end data flow.
3. **Comprehensive documentation** in `README.md` for easy setup and usage.

Let me know if there’s anything else you’d like to adjust, or if we’re ready to finalize the setup!