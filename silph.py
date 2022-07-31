from http.client import ResponseNotReady
import requests
import json
import aiohttp

slug = input('Slug: ')
url = f'https://silph.gg/api/cup/{slug}/stats'


response = requests.get(url)
print(response.status_code)
with open('./data.json', 'w') as file:
    json.dump(response.json(), file)