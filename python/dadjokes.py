import requests

limit = 3
api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'M/Gc0kc1pWefKueDDnw+Xg==wQSdncZeeouQVrBj'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)