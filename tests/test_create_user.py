import allure
import pytest
import requests
from utils.urls import Urls
from utils.data import ApiResponses


class TestCreateUser():
    @allure.title('Создание нового пользователя')
    @allure.description('Генерируем данные пользователя, отправляем запрос на создание и проверяем ответ')
    def test_create_new_user_success(self, only_create_user):
        test_user = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=only_create_user)
        user_token = test_user.json()['accessToken']
        requests.delete(Urls.MAIN_URL + Urls.EDIT_USER, headers={'Authorization': user_token})
        assert test_user.status_code == 200 and test_user.json()['success'] == True

    @allure.title('Создание пользователя с повторными данными')
    @allure.description('Проверяем создание пользователя с использованием уже существующих данных и получаем ошибку')
    def test_create_already_existing_user_fail(self, only_create_user):
        test_user = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=only_create_user)
        test_twin_user = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=only_create_user)
        user_token = test_user.json()['accessToken']
        requests.delete(Urls.MAIN_URL + Urls.EDIT_USER, headers={'Authorization': user_token})
        assert test_twin_user.status_code == 403 and test_twin_user.json()[
            'message'] == ApiResponses.USER_EXISTS

    @allure.title('Создание пользователя не заполнив поле почты')
    @allure.description('Создаем пользователя не заполнив обязательное поле и получаем ошибку')
    @pytest.mark.parametrize(
        'failed_user',
        [
            {'password': f'Helpers.generate_random_password()', 'name': f'Helpers.generate_random_name()'},
            {'email': f'Helpers.generate_random_email()', 'name': f'Helpers.generate_random_name()'},
            {'email': f'Helpers.generate_random_email()', 'password': f'Helpers.generate_random_password()'}]
    )
    def test_create_user_with_req_field_fail(self, failed_user):
        test_user = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=failed_user)
        assert test_user.status_code == 403 and test_user.json()[
            'message'] == ApiResponses.CREATE_USER_WITHOUT_PARAM
