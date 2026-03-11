import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key: str = os.getenv('MAILGUN_API_KEY') or ""
if not api_key:
    raise RuntimeError("MAILGUN_API_KEY environment variable is not set")


def send_template_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2fd4b3e04ee44ce48aaaa23f31a062f8.mailgun.org/messages",
        auth=("api", api_key),
        data={
            "from": "SnapApp <info@snapapp.ai>",
            "to": ["Aaditya Mukherjee <aaditya.mukherjee@bluevector.ai>"],
            "subject": "Hello Aaditya Mukherjee",
            # "text": "Congratulations Aaditya Mukherjee, you just sent an email with Mailgun! You are truly awesome!"
            "template": "admin welcome",
            "h:X-Mailgun-Variables": '{"first_name": "John"}',
        },
    )


try:
    response = send_template_message()
    print(response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print(f"Failed to send email: {e}")