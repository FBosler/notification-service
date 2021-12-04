import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


def send_sms(msg: str, recipient: str = None) -> None:
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
    client.messages.create(
        body=msg,
        from_=os.getenv("TWILIO_NUMBER"),
        to=recipient,
    )
