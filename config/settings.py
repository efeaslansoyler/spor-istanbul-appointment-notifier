import json
from pathlib import Path

# Load the user details from the root directory
user_file_path = Path(__file__).parent.parent / 'users.json'

with open(user_file_path, 'r') as f:
    data = json.load(f)

users = data['users']
TWILIO_ACCOUNT_SID = data['twilio']['account_sid']
TWILIO_AUTH_TOKEN = data['twilio']['auth_token']
TWILIO_PHONE_NUMBER = data['twilio']['phone_number']