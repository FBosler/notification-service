import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


def send_sms(msg: str, recipient: str = None) -> None:
    twilio_sender_number = os.getenv("TWILIO_NUMBER")
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH")
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=msg,
        from_=twilio_sender_number,
        to=recipient,
    )
