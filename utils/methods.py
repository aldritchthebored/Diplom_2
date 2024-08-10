import requests
import allure
from utils.urls import Urls
from utils.helpers import Helpers
from utils.data import TestOrder


class UserMethods:
    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(payload):
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=payload)
        return response
    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(payload):
        response = requests.delete(Urls.MAIN_URL + Urls.EDIT_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Создание пользователя без почты')
    def create_user_without_email():
        only_password = Helpers.create_data()['password']
        only_name = Helpers.create_data()['name']
        payload = {
            'email': '',
            'password': only_password,
            'name': only_name
        }
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Создание пользователя без пароля')
    def create_user_without_password():
        only_email = Helpers.create_data()['email']
        only_name = Helpers.create_data()['name']
        payload = {
            'email': only_email,
            'password': '',
            'name': only_name
        }
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Создание пользователя без имени')
    def create_user_without_name():
        only_email = Helpers.create_data()['email']
        only_password = Helpers.create_data()['password']
        payload = {
            'email': only_email,
            'password': only_password,
            'name': ''
        }
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Войти в систему')
    def login_user(payload):
        requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=payload)
        response = requests.post(Urls.MAIN_URL + Urls.LOGIN_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Войти в систему с неверной почтой или паролем')
    def login_invalid_email_password():
        payload = Helpers.create_data()
        response = requests.post(Urls.MAIN_URL + Urls.LOGIN_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Изменение профиля у пользователя с авторизацией')
    def edit_user_data_with_auth(payload, auth_token):
        response = requests.patch(Urls.MAIN_URL + Urls.EDIT_USER, headers={"Authorization": auth_token}, data=payload)
        return response

    @staticmethod
    @allure.step('Изменение профиля у пользователя без авторизации')
    def edit_user_data_no_auth(payload):
        response = requests.patch(Urls.MAIN_URL + Urls.EDIT_USER, data=payload)
        return response


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа с авторизацией')
    def create_order_with_auth(auth_token):
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_ORDER, headers={"Authorization": auth_token},
                                 data=TestOrder.correct_ingredients)
        return response

    @staticmethod
    @allure.step('Создание заказа без авторизации')
    def create_order_no_auth():
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_ORDER, data=TestOrder.correct_ingredients)
        return response

    @staticmethod
    @allure.step('Создание заказа без указания ингредиентов')
    def create_order_no_ingredients():
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_ORDER)
        return response

    @staticmethod
    @allure.step('Создание заказа с невалидным хешем ингредиентов')
    def create_order_invalid_hash():
        response = requests.post(Urls.MAIN_URL + Urls.CREATE_ORDER, data=TestOrder.incorrect_ingredients)
        return response

    @staticmethod
    @allure.step('Получение заказа с авторизацией')
    def receive_orders_with_auth(auth_token):
        response = requests.get(Urls.MAIN_URL + Urls.CREATE_ORDER, headers={"Authorization": auth_token})
        return response

    @staticmethod
    @allure.step('Получение заказа без авторизации')
    def receive_orders_no_auth():
        response = requests.get(Urls.MAIN_URL + Urls.CREATE_ORDER)
        return response
