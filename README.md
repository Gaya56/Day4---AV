# Day4---AV

### 1. **Data Ingestion** (from Cisco Webex API to Microsoft Fabric Real-Time Analytics or Azure Event Hub)

- **Cisco Webex API**: Periodically fetches real-time device metrics and status data from Cisco Webex Control Hub for multiple cities.
- **Ingestion Script** (`pipeline/ingest/fabric_real_time_ingest.py`): This Python script, run as an Azure Function or in an automated environment, retrieves data from the Webex API and pushes it to **Microsoft Fabric Real-Time Analytics** or **Azure Event Hub**.
- **Microsoft Fabric Real-Time Analytics** (or Event Hub): This is the entry point for all incoming data, acting as a scalable event stream. If using Fabric, it can immediately pass the data to transformation processes.

**Flow Summary**: Cisco Webex API ➔ `fabric_real_time_ingest.py` ➔ Event Hub / Fabric Real-Time Analytics

### 2. **Data Streaming and Transformation** (Processing Real-Time Data)

- **Microsoft Fabric Real-Time Analytics / Azure Stream Analytics**:
    - If using Fabric, Real-Time Analytics processes data directly, applying SQL-based or Spark-based transformations.
    - If using Azure Stream Analytics with Event Hub, data is routed from Event Hub to Stream Analytics for transformations (e.g., filtering, aggregations, or formatting).
- **Transformation Logic** (`pipeline/transform/fabric_transform.sql`): Defines the transformations applied to the incoming data. This could involve extracting only necessary fields, filtering on specific conditions, or performing aggregations.

**Flow Summary**: Real-Time Analytics / Stream Analytics ➔ `fabric_transform.sql`

### 3. **Data Storage** (Storing Transformed Data)

- **Microsoft Fabric OneLake**: Acts as the centralized data lake to store all processed and historical data. Fabric’s **Lakehouse** or **Warehouse** options enable fast querying and analysis.
- **Azure Data Explorer (optional)**: If needed for specific query and analytics capabilities, data could be stored in **Kusto DB** for further querying and analysis.

**Flow Summary**: Transformed data ➔ Fabric OneLake (Lakehouse/Warehouse) / Azure Data Explorer

### 4. **Visualization and Reporting** (Power BI Real-Time Dashboards)

- **Power BI**:
    - Power BI dashboards and reports pull data directly from Fabric OneLake (or Azure Data Explorer, if in use).
    - Reports for each city are available individually (stored in `output/PowerBI-reports/`), and a consolidated real-time dashboard (in `output/dashboards/`) displays metrics across all cities.
    - Power BI visualizations update in real-time, giving immediate insights into device status, performance, and other metrics for each city.

**Flow Summary**: Fabric OneLake ➔ Power BI reports (`output/PowerBI-reports/`) ➔ Real-Time Dashboard (`output/dashboards/`)

### 5. **Real-Time Alerts and Monitoring** (Microsoft Fabric Data Activator)

- **Microsoft Fabric Data Activator**: Allows you to set up triggers and alerts based on data thresholds or conditions. For example, you might configure alerts for when devices go offline or exceed a certain usage threshold.
- **Notification and Monitoring**: Alerts can be set to send real-time notifications (e.g., email, SMS, or within Power BI) if specific conditions are met, enabling proactive monitoring of devices.

**Flow Summary**: Processed Data ➔ Data Activator ➔ Real-Time Alerts

### Overall Flow Summary

The complete data flow in the pipeline is as follows:

```
Cisco Webex API
   ➔ Ingestion Script (`fabric_real_time_ingest.py`)
   ➔ Event Hub / Microsoft Fabric Real-Time Analytics
   ➔ Stream Analytics / Real-Time Analytics (Transformation)
   ➔ Fabric OneLake (Lakehouse/Warehouse) / Azure Data Explorer
   ➔ Power BI (City Reports and Real-Time Dashboard)
   ➔ Data Activator (Real-Time Alerts)

```

### High-Level Breakdown by Stage:

1. **Ingestion**: Data pulled from Webex API and streamed to Fabric/Stream Analytics.
2. **Transformation**: Data cleaned, filtered, or aggregated in real-time.
3. **Storage**: Processed data stored in Fabric's OneLake or Azure Data Explorer.
4. **Visualization**: Real-time insights via Power BI dashboards for each city and across all cities.
5. **Alerting**: Real-time monitoring and alerts based on predefined data conditions.

Each component in the flow works in tandem to provide a continuous, real-time view of device metrics across multiple cities, ensuring centralized visibility, monitoring, and alerting in one cohesive pipeline. Let me know if you want to start configuring any specific stage!
