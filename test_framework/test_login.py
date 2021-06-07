import pytest
import requests

URL = 'https://reqres.in/api/login'


@pytest.mark.parametrize('body', [{'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}])
def test_login_ok(body):
    assert requests.post(URL, json=body).status_code == 200
    assert requests.post(URL, json=body).json()['token']


@pytest.mark.parametrize('body', [{'email': 'eve.holt@reqres.in', 'password': 'abecece'},
                                  {'email': 'eve.holt@reqres.in', 'password': ''},
                                  {'email': 'eve.holt@reqres.in'},
                                  {'email': 'eve.holt@reqres.com', 'password': 'cityslicka'},
                                  {'email': '', 'password': 'cityslicka'},
                                  {'password': 'cityslicka'}])
def test_login_nok(body):
    assert requests.post(URL, json=body).status_code == 400
    assert 'token' not in requests.post(URL, json=body).json()
