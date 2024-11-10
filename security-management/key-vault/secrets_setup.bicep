// Define Key Vault
resource keyVault 'Microsoft.KeyVault/vaults@2021-06-01-preview' = {
  name: 'weatherDataKeyVault'
  location: resourceGroup().location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    accessPolicies: []
  }
}

// Secret for Webex API Key
resource webexApiKey 'Microsoft.KeyVault/vaults/secrets@2021-06-01-preview' = {
  parent: keyVault
  name: 'WEBEX_API_KEY'
  properties: {
    value: 'Your-Webex-API-Key' // Replace with actual API key or load via script
  }
}

// Secret for Event Hub Connection String
resource eventHubConnStr 'Microsoft.KeyVault/vaults/secrets@2021-06-01-preview' = {
  parent: keyVault
  name: 'EVENT_HUB_CONN_STR'
  properties: {
    value: 'Your-Event-Hub-Connection-String' // Replace with actual connection string
  }
}
