from openai import OpenAI
from datetime import datetime
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "system", "content": "Tu va répondre uniquement en majuscule"},
    {"role": "user", "content": "Who won the world series in 2020?"},
  ]
)
print(response.choices[0].message.content)

print(datetime.now())