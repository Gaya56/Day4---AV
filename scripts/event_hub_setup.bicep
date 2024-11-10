// Parameters for Event Hub namespace and hub
param eventHubNamespaceName string = 'myEventHubNamespace'
param eventHubName string = 'myEventHub'
param location string = resourceGroup().location

// Create Event Hub Namespace
resource eventHubNamespace 'Microsoft.EventHub/namespaces@2021-06-01-preview' = {
  name: eventHubNamespaceName
  location: location
  sku: {
    name: 'Standard'
    tier: 'Standard'
  }
}

// Create Event Hub within the namespace
resource eventHub 'Microsoft.EventHub/namespaces/eventhubs@2021-06-01-preview' = {
  name: eventHubName
  parent: eventHubNamespace
  properties: {}
}

// Output the connection string for ingestion script use
output eventHubNamespaceConnectionString string = listKeys(eventHubNamespace.id, 'RootManageSharedAccessKey').primaryConnectionString
output eventHubName string = eventHub.name
