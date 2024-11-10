### Setting Up Azure Key Vault for Secrets Management

1. Update `secrets_setup.bicep` with your actual API keys and connection strings (or load them later with `az keyvault secret set`).
2. Deploy Key Vault with the following command:

    ```bash
    az deployment group create --resource-group <Your-Resource-Group> --template-file security-management/key-vault/secrets_setup.bicep
    ```