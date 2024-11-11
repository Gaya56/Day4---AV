# Fabric Workspace Scripts

## Files in `scripts/fabric_workspace/`

### `configure_fabric_dataflows.py`
This is likely a Python script for setting up or managing dataflows within Microsoft Fabric.

### `deploy_fabric_infrastructure.sh`
A shell script that should automate the deployment of Fabric resources, such as the workspace, Real-Time Analytics jobs, and related infrastructure.

### `fabric_real_time_analytics_setup.bicep`
A Bicep template file to define and provision Microsoft Fabric Real-Time Analytics components and configurations, including any output routing (to Power BI or Data Activator for alerts).

### `setup_fabric_real_time_analytics.sh`
A shell script (presumably) to deploy the `fabric_real_time_analytics_setup.bicep` file. This file likely handles executing the Bicep template to set up the Real-Time Analytics job.

<<<<<<< HEAD
=======
### `configure_fabric_dataflows.py`

This Python script should:

- Connect to the Fabric workspace and configure any required dataflows.
- Set up parameters to process error messages or other real-time alerts based on your requirements.
>>>>>>> abd0cd9 (commit all changes)
