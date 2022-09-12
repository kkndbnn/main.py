from pprint import pprint
import requests
URL = 'https://cloud-api.yandex.net/v1/disk/resources'

def token():
    with open('Token_yandex/token_yandex.txt', 'r', encoding='UTF-8') as f:
        TOKEN = str(f.readline())
        return TOKEN

def do_disk(URL):
    TOKEN = token()
    param = {'path': 'FILE', 'overwrite': 'replace'}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    req = requests.put(URL, params=param, headers=headers)
    print(req)
    return req

def ya_path(URL):
    TOKEN = token()
    do_disk(URL)
    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    param = {'path': 'FILE/text.txt', 'overwrite': 'replace'}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    req = requests.get(URL, params=param, headers=headers).json()
    return req
    # pprint(req)

def ya_load(URL):
    req = ya_path(URL)
    URL = req['href']
    f = open('FILE/yandex.txt', 'rb')
    req = requests.put(URL, f)

ya_load(URL)
