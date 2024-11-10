import requests
import time

# Constants for Fabric and Automation setup
FABRIC_BASE_URL = "https://fabric-instance-url"  # Replace with the Fabric URL
API_KEY = "Your-API-Key"  # Replace with the Fabric API Key
ADMIN_EMAIL = "admin@example.com"  # Replace with the email for alerts
AUTOMATION_WEBHOOK_URL = "https://automation-system-url"  # Replace with Automation System URL

# Helper function to send email alerts
def send_email_alert(error_message, retry_count):
    email_payload = {
        "to": ADMIN_EMAIL,
        "subject": f"System Error Alert: Failed after {retry_count} attempts",
        "body": f"The system encountered the following issue: {error_message}. "
                f"Attempts to automatically resolve the issue have failed. Immediate attention is required."
    }
    response = requests.post(f"{FABRIC_BASE_URL}/send-email", headers=headers, json=email_payload)
    if response.status_code == 200:
        print("Alert email sent successfully.")
    else:
        print(f"Failed to send alert email: {response.status_code}")

# Function to trigger the Data Activator automation
def configure_data_activator():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Define the Dataflow configuration
    dataflow_config = {
        "name": "ErrorAlertDataflow",
        "conditions": [
            {"field": "error_code", "operator": "is not null"},
            {"field": "status", "operator": "equals", "value": "disconnected"}
        ],
        "actions": [
            {"type": "webhook", "target": AUTOMATION_WEBHOOK_URL, "retry_attempts": 3},
            {"type": "email", "target": ADMIN_EMAIL}  # Sends final alert if retries fail
        ]
    }

    # Create the dataflow in Microsoft Fabric
    response = requests.post(f"{FABRIC_BASE_URL}/dataflows", headers=headers, json=dataflow_config)
    if response.status_code == 200:
        print("Data Activator configured successfully.")
    else:
        print(f"Failed to configure Data Activator: {response.status_code}")
        return

    # Simulate real-time monitoring for this example
    monitor_and_retry_on_failure()

# Monitoring and Retry Logic
def monitor_and_retry_on_failure():
    retry_attempts = 0
    max_retries = 3

    while retry_attempts < max_retries:
        # Simulate checking system status
        system_status = check_system_status()

        if system_status == "connected":
            print("System is connected. No action needed.")
            return
        else:
            print(f"System is down. Attempting to troubleshoot. Attempt {retry_attempts + 1} of {max_retries}")
            attempt_troubleshoot()

        retry_attempts += 1
        time.sleep(5)  # Wait before next retry attempt

    # If all retries fail, send a final alert
    send_email_alert("System could not be reconnected after multiple attempts.", retry_attempts)

# Placeholder function to simulate system status check
def check_system_status():
    # Here you'd add actual checks for system connectivity
    return "disconnected"

# Placeholder function to simulate troubleshooting attempts
def attempt_troubleshoot():
    # Add code here to try reconnecting or restarting the system
    print("Attempting to troubleshoot (e.g., reconnect or restart)")

# Main execution
if __name__ == "__main__":
    configure_data_activator()
