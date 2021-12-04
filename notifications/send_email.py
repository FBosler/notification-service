import os
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
PORT = 465


def send_email(msg: str, recipient: str = None) -> None:
    email = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, PORT, context=context) as server:
        server.login(user=email, password=password)

        SUBJECT = "Important Notification"

        BODY = "\r\n".join((f"From: {email}", f"To: {email}", f"Subject: {SUBJECT}", "", msg))
        server.sendmail(email, [recipient or email], BODY)


if __name__ == "__main__":
    send_email("This is a test")
