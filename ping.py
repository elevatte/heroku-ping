import os
import time
import requests

URL = os.environ['URL']
TIMEOUT = int(os.environ['TIMEOUT'])

while True:
    res = requests.get(URL)
    print(f'{URL} {res}')
    time.sleep(TIMEOUT)
    