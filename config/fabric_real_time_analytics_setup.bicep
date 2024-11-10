// Define the Fabric Real-Time Analytics Job
resource fabricRealTimeAnalyticsJob 'Microsoft.Fabric/realtimeanalytics@2022-08-01' = {
  name: 'fabricRealTimeAnalyticsJob'
  location: resourceGroup().location
  properties: {
    inputType: 'EventHub'
    eventHubNamespace: 'City_DataNamespace' // Replace with your Event Hub namespace
    eventHubName: 'City_DataHub' // Replace with your Event Hub name
    consumerGroupName: '$Default' // Use your specific consumer group if applicable
    
    // Define the query to process error messages only
    query: loadTextContent('./config/error_monitoring_query.sql')

    // Define the output to Data Activator
    outputType: 'DataActivator'
    outputConfig: {
      dataActivator: {
        alertName: 'DeviceErrorAlert'  // Name of the alert
        conditions: [
          {
            field: 'error_code',         // Field to monitor for specific errors
            operator: 'NotNull'          // Trigger when 'error_code' is not null
          }
        ]
        actionType: 'Webhook'
        actionConfig: {
          endpoint: 'https://<your-automation-endpoint-url>' // Replace with your endpoint
          method: 'POST'
          headers: {
            "Content-Type": "application/json"
          }
        }
      }
    }
  }
}
