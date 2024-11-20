# O365 Compliance Reports

This project provides automated compliance reports for Office 365, including security alerts, sign-in logs, and more. The script retrieves data from Microsoft Azure AD and other sources, processes the information, and sends email notifications for security concerns.

## Features

- Retrieves data from Microsoft Graph API.
- Maps complex app names to simplified versions for easier understanding.
- Sends email notifications for login issues, security alerts, and phishing risks.
- Uses environment variables for credentials to keep sensitive information secure.

## Prerequisites

- Python 3.6+
- Required Python packages:
  - `requests`
  - `pytz`
  - `pandas`
  - `smtplib`
  - `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shivaansh74/O365-Compliance-Reports.git
