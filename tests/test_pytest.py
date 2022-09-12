# import pytest

from main import people, shelf, list, add

document = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
]

directorie = {
    '1': ['2207 876234', '11-2', '5455 028765']
}

def test_people():
    assert people(document, "2207 876234") == "Василий Гупкин"
def test_shelf():
    assert shelf(directorie, "2207 876234") == "1"
def test_list():
    assert list(document) == 'passport "2207 876234" "Василий Гупкин"'
def test_add():
    assert add(document, directorie, '3123', 'dpad', 'fads' ,'1') == document[1]


