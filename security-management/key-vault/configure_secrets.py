### **Step 2: Script to Load Secrets into Environment Variables**
###*Create `configure_secrets.py` in `security-management/key-vault/`.
###*This Python script will retrieve secrets from Key Vault and load them into environment variables, which can be accessed by the ingestion script.
#### `security-management/key-vault/configure_secrets.py`

import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Set up Key Vault client
key_vault_name = "weatherDataKeyVault"
kv_uri = f"https://{key_vault_name}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=kv_uri, credential=credential)

# Retrieve and set environment variables
def load_secrets():
    webex_api_key = client.get_secret("WEBEX_API_KEY").value
    os.environ["WEBEX_API_KEY"] = webex_api_key

    event_hub_conn_str = client.get_secret("EVENT_HUB_CONN_STR").value
    os.environ["EVENT_HUB_CONN_STR"] = event_hub_conn_str

    print("Secrets loaded into environment variables.")

if __name__ == "__main__":
    load_secrets()
