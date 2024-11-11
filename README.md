Here's the updated diagram, including **Microsoft Fabric** for automation and **Power BI with Control Hub actions**:

                           +-------------------------+
                           |   Cisco Webex Control   |
                           |       Hub API          |
                           +-----------+------------+
                                       |
                                       |
                             [ Ingest Data ]
                                       |
                                       v
                           +-----------+------------+
                           |   Ingestion Script     |
                           | fabric_real_time_ingest|
                           +-----------+------------+
                                       |
                                       | Event Hub Queue
                                       |
                                       v
                           +-----------+------------+
                           |    Azure Event Hub     |
                           +-----------+------------+
                                       |
                               Stream Analytics
                                       |
                                       v
                       +---------------+----------------+
                       |               Power BI         |
                       |       Real-Time Dashboard      |
                       +---------------+----------------+
                                       |
                      [ Manual Command or Alert Trigger ]
                                       |
                                       v
                       +---------------+----------------+
                       |               Azure Function   |
                       | (Triggered by Power BI action  |
                       |   or alert from Data Activator)|
                       +---------------+----------------+
                                       |
                          [Command to Control Hub API]
                                       |
                                       v
                           +-----------+------------+
                           |   Microsoft Fabric      |
                           |  (Data Activator,       |
                           | Automation & Alerts)    |
                           +-----------+------------+
                                       |
                            [Automated Retry & Logging]
                                       |
                                       v
                           +-------------------------+
                           |    Cisco Webex Control   |
                           |       Hub API           |
                           +-------------------------+
```

---

### Flow Explanation

1. **Cisco Webex Control Hub API**:
   - Cisco Webex Control Hub provides real-time telemetry data, such as device status, errors, and metrics, which are periodically fetched by the ingestion script.

2. **Ingestion Script (`fabric_real_time_ingest.py`)**:
   - The ingestion script is responsible for pulling data from the Webex Control Hub API and streaming it to **Azure Event Hub** for processing.
   - It runs locally or can be automated through an **Azure Function** to pull data on a schedule.

3. **Azure Event Hub**:
   - Acts as a real-time message broker, queuing the data from the ingestion script and sending it to downstream services like **Azure Stream Analytics** and **Microsoft Fabric**.

4. **Azure Stream Analytics**:
   - Processes the data in real time, filtering and transforming it as needed.
   - Routes the filtered data to **Power BI** for visualizing live device metrics and error status on a real-time dashboard.

5. **Power BI Real-Time Dashboard**:
   - Displays data in real-time for technicians and administrators to monitor device health and performance.
   - Provides actionable buttons (e.g., Restart, Reconnect) for technicians to send commands back to Webex Control Hub to manage devices.

6. **Azure Function** (triggered by Power BI actions or Data Activator alerts):
   - When a technician selects an action in Power BI, an **Azure Function** is triggered to send a command (e.g., Restart, Reconnect) back to the Webex Control Hub.
   - This function can also be triggered by **Data Activator** in Microsoft Fabric if it detects issues, such as a persistent “disconnected” status.

7. **Microsoft Fabric** (Data Activator & Automation):
   - Monitors the streaming data for specific conditions (e.g., errors, disconnects).
   - If conditions are met, **Data Activator** triggers automated responses, such as sending a reconnect or restart command to the Webex Control Hub.
   - It retries actions (e.g., reconnection) up to a specified number of attempts and logs outcomes.

8. **Control Hub API Command Execution**:
   - Commands from Power BI actions or Data Activator alerts are sent to **Cisco Webex Control Hub API** to attempt a reconnection or troubleshooting on the specified devices.

---

### Summary

This setup provides a complete, real-time solution for monitoring and managing Cisco devices:
- **Real-Time Monitoring** in Power BI: Technicians have a live view of device status and can quickly take action if issues arise.
- **Automated Monitoring and Alerts** via Microsoft Fabric: Fabric’s Data Activator provides automated actions if error conditions are detected.
- **Feedback Loop for Control Commands**: Technicians can manually send control commands, and automated retry attempts are made if issues persist.

Each component works together to provide an end-to-end real-time monitoring and automated response system for managing Cisco devices.
