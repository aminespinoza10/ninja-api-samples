import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')


limit = 3
api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)