from pprint import pprint
import requests


def do_disk():
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    TOKEN = 'AQAAAABe-PqUAADLWzMn3xXq0kNEoJoNHAbCHgY'
    param = {'path': 'FILE'}
    headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    req = requests.get(URL, params=param, headers=headers)
    return req


do_disk()

