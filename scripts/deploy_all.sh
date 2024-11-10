#!/bin/bash
# Deploy all Azure resources for the dual-pipeline setup

# Set resource group and location
RESOURCE_GROUP="<Your-Resource-Group>"
LOCATION="eastus"  # Update as needed

# Deploy Event Hub Namespace and Event Hub
echo "Deploying Event Hub..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file config/eventhub_setup.bicep

# Deploy Stream Analytics Job for general metrics
echo "Deploying Stream Analytics Job..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file config/stream_analytics_setup.bicep

# Deploy Fabric Real-Time Analytics Job for error monitoring
echo "Deploying Fabric Real-Time Analytics Job..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file config/fabric_real_time_analytics_setup.bicep

# Deploy Azure Key Vault for secrets management
echo "Deploying Azure Key Vault..."
az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file security-management/key-vault/key_vault_setup.bicep

echo "Deployment complete."
