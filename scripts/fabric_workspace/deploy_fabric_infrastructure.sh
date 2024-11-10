# Notes 2: deploy_fabric_infrastructure.sh
#
# This shell script should:
#
# - Create the Fabric workspace if it doesn't already exist.
# - Deploy necessary resources within the Fabric workspace, such as Real-Time Analytics jobs or data sources.

#!/bin/bash

# Set variables
RESOURCE_GROUP="your-resource-group"
FABRIC_WORKSPACE="your-fabric-workspace"
LOCATION="eastus"

# Create Fabric workspace
az fabric create --name $FABRIC_WORKSPACE --resource-group $RESOURCE_GROUP --location $LOCATION

# Deploy the real-time analytics job
./setup_fabric_real_time_analytics.sh
echo "Fabric infrastructure deployed successfully."
