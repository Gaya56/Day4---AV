 
 The script creates an Event Hubs namespace and an Event Hub within that namespace. The script also outputs the connection strings for the namespace and the Event Hub. 
 Deploy the Bicep script 
 To deploy the Bicep script, use the following command: 
 az deployment group create --resource-group myResourceGroup --template-file event_hub_setup.bicep
 
 The command creates the Event Hubs namespace and Event Hub in the specified resource group. 
 Next steps 
 In this tutorial, you learned how to: 
 Advance to the next tutorial: 
 Create an Azure Function app with Bicep
 
******************************************************************************************************************

param eventHubNamespaceName string = 'myEventHubNamespace'
param eventHubName string = 'myEventHub'
param location string = resourceGroup().location

resource eventHubNamespace 'Microsoft.EventHub/namespaces@2021-06-01-preview' = {
  name: eventHubNamespaceName
  location: location
  sku: {
    name: 'Standard'
    tier: 'Standard'
  }
}

resource eventHub 'Microsoft.EventHub/namespaces/eventhubs@2021-06-01-preview' = {
  name: eventHubName
  parent: eventHubNamespace
  properties: {}
}

output eventHubNamespaceConnectionString string = listKeys(eventHubNamespace.id, 'RootManageSharedAccessKey').primaryConnectionString
output eventHubName string = eventHub.name
output eventHubConnectionString string = listKeys(eventHub.id, 'RootManageSharedAccessKey').primaryConnectionString
