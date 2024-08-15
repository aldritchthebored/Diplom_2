import pytest
import requests
from utils.urls import Urls
from utils.helpers import Helpers


@pytest.fixture()
def only_create_user():
    user_payload = Helpers.create_data()
    yield user_payload

@pytest.fixture
def create_and_delete_user():
    while True:
        try:
            user_payload = Helpers.create_data()
            response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=user_payload)
            auth_token = response.json()['accessToken']
            yield user_payload, auth_token
            requests.delete(Urls.MAIN_URL + Urls.EDIT_USER, headers={"Authorization": auth_token})
            break
        except KeyError:(
            pytest.fail("Failed to create user: 'accessToken' not found in response JSON"))

