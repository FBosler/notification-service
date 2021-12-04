import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


def send_sms(msg: str) -> None:
    URL = os.getenv("SLACK_WEBHOOK")
    headers = {"content-type": "application/json"}
    payload = {
        "attachments": [
            {
                "fallback": "Plain-text summary of the attachment.",
                "color": "#fff",
                "title": "🚨 Important notification",
                "text": msg,
                "title_link": f"https://medium.com/@fabianbosler/membership",
                "footer": "Made by Fabian with ❤️",
                "footer_icon": "https://image.flaticon.com/icons/png/512/2097/2097443.png",
                "ts": datetime.utcnow().timestamp(),
            }
        ]
    }
    requests.post(URL, json=payload, headers=headers)
