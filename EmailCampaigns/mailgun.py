import os
import requests
from dotenv import load_dotenv

load_dotenv()

api=os.getenv('MAILGUN_API_KEY')
print(api)

def send_template_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox2fd4b3e04ee44ce48aaaa23f31a062f8.mailgun.org/messages",
  		auth=("api", api),
        data={"from": "SnapApp <info@snapapp.ai>",
			"to": ["Aaditya Mukherjee <aaditya.mukherjee@bluevector.ai>"],
  			"subject": "Hello Aaditya Mukherjee",
  			# "text": "Congratulations Aaditya Mukherjee, you just sent an email with Mailgun! You are truly awesome!"
			"template": "admin welcome",
			"h:X-Mailgun-Variables": '{"first_name": "John"}'
        })


response = send_template_message()
print(response.status_code, response.text)