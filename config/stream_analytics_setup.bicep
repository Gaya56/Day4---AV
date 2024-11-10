// Stream Analytics Job Definition
resource streamAnalyticsJob 'Microsoft.StreamAnalytics/streamingjobs@2020-03-01' = {
  name: 'webexDataStreamJob'
  location: resourceGroup().location
  properties: {
    sku: {
      name: 'Standard'
    }
    eventsOutOfOrderPolicy: 'Adjust'
    eventsOutOfOrderMaxDelayInSeconds: 60
    outputErrorPolicy: 'Stop'
  }
}

// Event Hub Input for Stream Analytics
resource eventHubInput 'Microsoft.StreamAnalytics/streamingjobs/inputs@2020-03-01' = {
  parent: streamAnalyticsJob
  name: 'inputEventHub'
  properties: {
    type: 'Stream'
    datasource: {
      type: 'Microsoft.ServiceBus/EventHub'
      properties: {
        serviceBusNamespace: 'weatherDataNamespace' // Replace with your Event Hub namespace
        eventHubName: 'weatherDataHub' // Replace with your Event Hub name
        sharedAccessPolicyName: 'RootManageSharedAccessKey' // Replace with your access policy
        sharedAccessPolicyKey: 'Your-Access-Policy-Key' // Use Key Vault in production
        consumerGroupName: '$Default'
      }
    }
    serialization: {
      type: 'Json'
      encoding: 'UTF8'
    }
  }
}

// Power BI Output for Stream Analytics
resource powerBiOutput 'Microsoft.StreamAnalytics/streamingjobs/outputs@2020-03-01' = {
  parent: streamAnalyticsJob
  name: 'outputPowerBI'
  properties: {
    datasource: {
      type: 'PowerBI'
      properties: {
        dataset: 'WebexDeviceMetrics'
        table: 'RealTimeDeviceData'
        groupId: 'Your-Workspace-Group-ID' // Power BI workspace ID
      }
    }
  }
}

// Stream Analytics Query Configuration
resource streamAnalyticsQuery 'Microsoft.StreamAnalytics/streamingjobs/transformations@2020-03-01' = {
  parent: streamAnalyticsJob
  name: 'query'
  properties: {
    streamingUnits: 1
    //query: loadTextContent('./config/data_transform_query.sql')
  }
}
