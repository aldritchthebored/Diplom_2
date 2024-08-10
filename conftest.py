import pytest
import requests
from utils.urls import Urls
from utils.helpers import Helpers


@pytest.fixture()
def only_create_user():
    user_payload = Helpers.create_data()
    yield user_payload

@pytest.fixture()
def create_and_delete_user():
    user_payload = Helpers.create_data()
    yield user_payload
    requests.post(Urls.MAIN_URL + Urls.LOGIN_USER, data=user_payload)
    requests.delete(Urls.MAIN_URL + Urls.EDIT_USER)

@pytest.fixture
def with_token():
    user_payload = Helpers.create_data()
    response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=user_payload)
    auth_token = response.json()['accessToken']
    yield auth_token
    requests.delete(Urls.MAIN_URL + Urls.EDIT_USER, headers={"Authorization": auth_token})

@pytest.fixture
def no_token():
    user_payload = Helpers.create_data()
    response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=user_payload)
    yield response
    requests.post(Urls.MAIN_URL + Urls.LOGIN_USER, data=user_payload)
    requests.delete(Urls.MAIN_URL + Urls.EDIT_USER)
