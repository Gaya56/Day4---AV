// Define the Fabric Real-Time Analytics workspace, dataflows, and any output configurations.


param location string = resourceGroup().location
param fabricWorkspaceName string = 'your-fabric-workspace-name'
param realTimeAnalyticsJobName string = 'fabric-real-time-analytics-job'
param outputPowerBI string = 'OutputPowerBI'  // Alias used in the query
param outputDataActivator string = 'OutputDataActivator'  // Alias for alerts

resource fabricWorkspace 'Microsoft.Fabric/workspaces@2022-04-01-preview' = {
  name: fabricWorkspaceName
  location: location
}

resource realTimeAnalytics 'Microsoft.Fabric/workspaces/realTimeAnalyticsJobs@2022-04-01-preview' = {
  parent: fabricWorkspace
  name: realTimeAnalyticsJobName
  properties: {
    jobProperties: {
      eventHubInput: {
        // Configure event hub inputs here
      }
      outputPowerBI: {
        // Power BI output configuration
      }
      outputDataActivator: {
        // Data Activator for error alerts
      }
    }
  }
}

