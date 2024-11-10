#!/bin/bash
# Create main project folder structure

# 1. Cities folder
mkdir -p cities/city-configs
mkdir -p cities/city-data/city1-data/raw cities/city-data/city1-data/processed
mkdir -p cities/city-data/city2-data/raw cities/city-data/city2-data/processed
# Repeat the above command for all 11 cities or use a loop if needed.

# Create example config files for two cities
touch cities/city-configs/city1-config.json
touch cities/city-configs/city2-config.json

# 2. Pipeline folder
mkdir -p pipeline/ingest
mkdir -p pipeline/transform

# Create placeholder scripts for ingest and transform
touch pipeline/ingest/fabric_real_time_ingest.py
touch pipeline/ingest/blob_storage_ingest.py
touch pipeline/transform/fabric_transform.sql
touch pipeline/transform/fabric_notebook.ipynb

# 3. Output folder
mkdir -p output/PowerBI-reports
mkdir -p output/dashboards

# Create Power BI report templates for two cities and a main dashboard
touch output/PowerBI-reports/city1-report.pbix
touch output/PowerBI-reports/city2-report.pbix
touch output/dashboards/fabric-dashboard.pbix

# 4. Scripts folder
mkdir -p scripts

# Create placeholder deployment and setup scripts
touch scripts/deploy_fabric_infrastructure.sh
touch scripts/setup_fabric_real_time_analytics.sh
touch scripts/configure_fabric_dataflows.py
touch scripts/cost_management.sh

# 5. Security Management folder
mkdir -p security-management/key-vault

# Create Key Vault setup scripts
touch security-management/key-vault/secrets_setup.bicep
touch security-management/key-vault/configure_secrets.py

# 6. README
touch README.md

# Optional: Initialize Git and make the first commit
git init
git add .
git commit -m "Initial commit with directory structure for Azure weather pipeline with Microsoft Fabric integration"
