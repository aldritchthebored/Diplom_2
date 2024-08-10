import allure
from utils.methods import UserMethods
from utils.data import ApiResponses


class TestLoginUser:
    @allure.title('Вход в систему пользователем')
    @allure.description('Заходим в систему пользователем и проверяем ответ')
    def test_login_user_success(self, create_and_delete_user):
        UserMethods.create_user(create_and_delete_user)
        test_user = UserMethods.login_user(create_and_delete_user)
        assert test_user.status_code == 200 and test_user.json()['success'] == True

    @allure.title('Пользователь авторизуется с неверной почтой или паролем')
    @allure.step('Проверяем вход с неверной почтой и паролем и получаем ошибку')
    def test_login_invalid_credetentials_fail(self):
        test_user = UserMethods.login_invalid_email_password()
        assert (test_user.status_code == 401 and test_user.json()['message'] ==
                ApiResponses.LOGIN_USER_INVALID_EMAIL_PASSWORD)






