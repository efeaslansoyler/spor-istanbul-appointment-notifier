from twilio.rest import Client
from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from utils.logger import log_with_timestamp

def send_sms(phone_number: str, message: str) -> None:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    log_with_timestamp(f"Sending SMS to {phone_number}: {message}")
    try:
        client.messages.create(to=phone_number, from_=TWILIO_PHONE_NUMBER, body=message)
        log_with_timestamp(f"SMS sent to {phone_number}: {message}")
    except Exception as e:
        log_with_timestamp(f"Failed to send SMS to {phone_number}: {str(e)}")
