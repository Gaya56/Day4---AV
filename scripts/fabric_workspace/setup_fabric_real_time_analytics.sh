#4. setup_fabric_real_time_analytics.sh

#This script should:

 #***Deploy the Bicep template (fabric_real_time_analytics_setup.bicep) to Azure, setting up the Real-Time Analytics workspace and outputs.



#!/bin/bash

RESOURCE_GROUP="your-resource-group"
TEMPLATE_FILE="fabric_real_time_analytics_setup.bicep"

# Deploy the Bicep template
az deployment group create --resource-group $RESOURCE_GROUP --template-file $TEMPLATE_FILE
echo "Fabric Real-Time Analytics job setup completed."
