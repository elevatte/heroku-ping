import os
import time
import requests

URLS = os.environ.get('URLS')
TIMEOUT = int(os.environ.get('TIMEOUT', 300))

if not URLS:
    raise Exception('URLS env var required')

while True:
    parsed_urls = URLS.split(',')
    for url in parsed_urls:
        res = requests.get(url)
        print(f'{url} {res}')
    time.sleep(TIMEOUT)    