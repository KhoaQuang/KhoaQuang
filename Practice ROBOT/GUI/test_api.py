import requests

def test_get_api():
    response = requests.get('https://api.example.com/resource')
    assert response.status_code == 200
    assert response.json()['key'] == 'value'

def test_post_api():
    payload = {'key': 'value'}
    response = requests.post('https://api.example.com/resource', json=payload)
    assert response.status_code == 201
    assert response.json()['key'] == 'value'
