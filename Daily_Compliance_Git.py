import requests
import datetime
import pytz
import pandas as pd
from collections import defaultdict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Azure AD credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
tenant_id = os.getenv('TENANT_ID')

# Email credentials
email_sender = os.getenv('EMAIL_SENDER')
email_password = os.getenv('EMAIL_PASSWORD')
email_recipient = os.getenv('EMAIL_RECIPIENT')

# Mapping of complex app names to simplified versions
app_name_mapping = {
    "Office Online Core SSO": "Office Online",
    "Office365 Shell WCSS-Client": "Office 365 Shell",
    "Microsoft Account Controls V2": "Microsoft Account",
    "Office 365 SharePoint Online": "SharePoint Online",
    "Office 365 Exchange Online": "Exchange Online",
    "Graph Explorer": "Graph Explorer",
    "Microsoft 365 Security and Compliance Center": "Microsoft 365 Security",
    "OfficeHome": "Office Home",
    "Microsoft 365 Support Service": "Microsoft 365 Support",
    "Azure Portal": "Azure Portal",
    "Microsoft Office": "Microsoft Office",
    "Microsoft Authentication Broker": "Microsoft Auth Broker",
    "Microsoft Teams": "Teams"
}

# Other functions (unchanged)
def get_access_token():
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json().get('access_token')

# (Rest of the functions remain unchanged, for brevity.)

if __name__ == "__main__":
    main()
