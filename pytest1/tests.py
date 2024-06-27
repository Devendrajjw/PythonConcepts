import pytest
import requests


def make_request(api_key):
    base_url = "http://api.nasa.gov/neo/rest/v1/neo/2000433"
    response = requests.get(f'{base_url}?api_key={api_key}')
    return response


def test_search_asteriods_with_success():
    api_key = "DEMO_KEY"
    response = make_request(api_key)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data['absolute_magnitude_h'] > 0
