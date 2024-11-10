### Setting Up the Stream Analytics Job

The Stream Analytics job is configured to:
- Ingest data from Azure Event Hub.
- Apply transformations (filtering for Calgary, both active and non-active).
- Output the processed data to Power BI for real-time visualization.

#### Steps to Deploy the Stream Analytics Job

1. Ensure you have configured your Event Hub namespace, name, and access policy in `config/stream_analytics_setup.bicep`.
2. Update the Power BI workspace ID in `config/stream_analytics_setup.bicep`.
3. Deploy the Stream Analytics job with the following command:

    ```bash
    az deployment group create --resource-group <Your-Resource-Group> --template-file config/stream_analytics_setup.bicep
    ```
    ### **Summary of What We’ve Done So Far**

    1. **Configured the Query** (`data_transform_query.sql`) to filter data for Calgary devices, both active and non-active.
    2. **Created a Bicep Template** (`stream_analytics_setup.bicep`) to define the Stream Analytics job, input, output, and query settings.

    