import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
HEADERS = {'Content-Type' : 'application/json'}
TOKEN = '42a0f282026236b2c51265016eba7639'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 4244})
    assert response.status_code == 200


def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 4244})
    assert response.json()['data'][0]['trainer_name'] == 'Маестро'
