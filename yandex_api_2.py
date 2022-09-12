from pprint import pprint
import requests
URL = 'https://cloud-api.yandex.net/v1/disk/resources'

def token():
    with open('Token_yandex/token_yandex.txt', 'r', encoding='UTF-8') as f:
        TOKEN = str(f.readline())
        return TOKEN

def do_disk(URL):
    TOKEN = token()
    param = {'path': 'FILE'}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    req = requests.get(URL, params=param, headers=headers)
    # pprint(req)
    return req
do_disk(URL)
