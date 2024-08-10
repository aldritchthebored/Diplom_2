import allure
import pytest
from utils.helpers import Helpers
from utils.methods import UserMethods
from utils.data import ApiResponses


class TestEditUser:
    @allure.title('Изменение одного из полей у пользователя с авторизацией')
    @allure.description('Заходим в систему пользователем, изменяем одно из полей и проверяем ответ')
    @pytest.mark.parametrize(
        'new_field',
        [
            {"password": Helpers.generate_random_password()},
            {"name": Helpers.generate_random_name()},
            {"email": Helpers.generate_random_email()}
        ]
    )
    def test_edit_user_data_success(self, new_field, with_token):

       test_user = UserMethods.edit_user_data_with_auth(new_field, with_token)
       assert test_user.status_code == 200 and test_user.json()['success']

    @allure.title('Изменение одного из полей у пользователя без авторизации')
    @allure.description('Пытаемся изменить одно из полей без авторизации и получаем ошибку')
    @pytest.mark.parametrize(
        'new_field',
        [
            {"password": Helpers.generate_random_password()},
            {"name": Helpers.generate_random_name()},
            {"email": Helpers.generate_random_email()},
        ]
    )
    def test_edit_user_data_no_auth_fail(self, new_field, no_token):
        test_user = UserMethods.edit_user_data_no_auth(new_field)
        assert test_user.status_code == 401 and test_user.json()['message'] == ApiResponses.EDIT_FIELD_NO_AUTH