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