# O365 Compliance Reports

This project provides automated compliance reports for Office 365, including security alerts, sign-in logs, and more. The script retrieves data from Microsoft Azure AD and other sources, processes the information, and sends email notifications for security concerns such as login issues, phishing risks, and other potential threats.

## Features

- **Data Retrieval from Microsoft Graph API:** Fetches Office 365 and Azure AD data.
- **App Name Mapping:** Maps complex app names to simplified, user-friendly versions for easier understanding.
- **Email Notifications:** Sends alerts for login issues, security concerns, and phishing risks.
- **Environment Variable Support:** Stores credentials and sensitive information securely using environment variables.

## Prerequisites

Before running this script, ensure the following:

- **Python 3.6+** installed on your system.
- The following Python libraries are installed:
  - `requests`
  - `pytz`
  - `pandas`
  - `smtplib`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/shivaansh74/O365-Compliance-Reports.git
    ```

2. Navigate to the repository folder:

    ```bash
    cd O365-Compliance-Reports
    ```

3. Update the environment variables for Azure AD and email credentials by modifying setting them directly in your environment.

   Add the following details to your environment variables:

   **Azure AD credentials:**

    ```bash
    client_id="YOUR CLIENT ID"
    client_secret="YOUR CLIENT SECRET"
    tenant_id="YOUR TENANT ID"
    ```

   **Email credentials:**

    ```bash
    email_sender="YOUREMAIL@EXAMPLE.COM"
    email_password="YOUREMAILPASSWORD"
    email_recipient="RECIPIENTEMAIL@EXAMPLE.COM"
    ```

## Usage

Run the script to start generating compliance reports:

```bash
python o365_compliance_report.py
```

## Notes
Ensure that your Azure AD credentials (client ID, secret, and tenant ID) and email credentials are correctly set in the environment variables.

The script requires an active internet connection and valid access permissions to Microsoft Graph API to fetch data.

## License
This project is licensed under the MIT License.

## Contact
For issues or suggestions, please contact Shivaansh Dhingra at shivi@datafysystems.com.
