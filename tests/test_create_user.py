import allure
from utils.methods import UserMethods
from utils.data import ApiResponses


class TestCreateUser():
    @allure.title('Создание нового пользователя')
    @allure.description('Генерируем данные пользователя, отправляем запрос на создание и проверяем ответ')
    def test_create_new_user_success(self, create_and_delete_user):
        test_user = UserMethods.create_user(create_and_delete_user)
        assert test_user.status_code == 200 and test_user.json()['success'] == True

    @allure.title('Создание пользователя с повторными данными')
    @allure.description('Проверяем создание пользователя с использованием уже существующих данных и получаем ошибку')
    def test_create_already_existing_user_fail(self, only_create_user):
        test_user = UserMethods.create_user(only_create_user)
        test_twin_user = UserMethods.create_user(only_create_user)
        test_user = UserMethods.delete_user(only_create_user)
        assert test_twin_user.status_code == 403 and test_twin_user.json()[
            'message'] == ApiResponses.USER_EXISTS

    @allure.title('Создание пользователя не заполнив поле почты')
    @allure.description('Создаем пользователя не заполнив обязательное поле и получаем ошибку')
    def test_create_user_without_email_fail(self):
        test_user = UserMethods.create_user_without_email()
        assert test_user.status_code == 403 and test_user.json()[
            'message'] == ApiResponses.CREATE_USER_WITHOUT_PARAM

    @allure.title('Создание пользователя не заполнив поле пароля')
    @allure.description('Создаем пользователя не заполнив обязательное поле и получаем ошибку')
    def test_create_user_without_password_fail(self):
        test_user = UserMethods.create_user_without_password()
        assert test_user.status_code == 403 and test_user.json()[
            'message'] == ApiResponses.CREATE_USER_WITHOUT_PARAM

    @allure.title('Создание пользователя не заполнив поле пароля')
    @allure.description('Создаем пользователя не заполнив обязательное поле и получаем ошибку')
    def test_create_user_without_password_fail(self):
        test_user = UserMethods.create_user_without_name()
        assert test_user.status_code == 403 and test_user.json()[
            'message'] == ApiResponses.CREATE_USER_WITHOUT_PARAM



