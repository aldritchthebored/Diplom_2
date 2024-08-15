import allure
import requests
from utils.urls import Urls
from utils.data import ApiResponses


class TestLoginUser:
    @allure.title('Вход в систему пользователем')
    @allure.description('Заходим в систему пользователем и проверяем ответ')
    def test_login_user_success(self, create_and_delete_user):
        test_user = requests.post(Urls.MAIN_URL + Urls.LOGIN_USER, data=create_and_delete_user[0])
        assert test_user.status_code == 200 and test_user.json()['success'] == True

    @allure.title('Пользователь авторизуется с неверной почтой или паролем')
    @allure.step('Проверяем вход с неверной почтой и паролем и получаем ошибку')
    def test_login_invalid_credetentials_fail(self, only_create_user):
        test_user = requests.post(Urls.MAIN_URL + Urls.LOGIN_USER, data=only_create_user)
        assert (test_user.status_code == 401 and test_user.json()['message'] ==
                ApiResponses.LOGIN_USER_INVALID_EMAIL_PASSWORD)






