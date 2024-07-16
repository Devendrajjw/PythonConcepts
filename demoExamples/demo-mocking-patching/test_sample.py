
import pytest

import requests

def get_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}" )
    return response.json()


def test_get_user_success(mocker):
    user_id = 1
    mock_response = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    response = get_user(user_id)
    assert response["id"] == 1
    assert response["name"] == "Leanne Graham"
    assert response["username"] == "Bret"
    assert response["email"] == "Sincere@april.biz"

def test_get_user_not_found(mocker):
    user_id = 999
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=404, json=lambda: {}))

    response = get_user(user_id)
    assert response == {}
