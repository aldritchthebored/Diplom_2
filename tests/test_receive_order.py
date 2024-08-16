import allure
import requests
from utils.urls import Urls
from utils.data import ApiResponses, TestOrder


class TestReceiveOrder:
    @allure.title('Получаем заказы пользователя с авторизацией')
    @allure.step('Получаем заказы пользователя с авторизацией и проверяем ответ')
    def test_receive_orders_with_auth_success(self, create_and_delete_user):
        requests.post(Urls.MAIN_URL + Urls.CREATE_ORDER, headers={"Authorization": create_and_delete_user[1]},
                      data=TestOrder.correct_ingredients)
        test_order = requests.get(Urls.MAIN_URL + Urls.CREATE_ORDER, headers={"Authorization":
                                                                                  create_and_delete_user[1]})
        assert test_order.status_code == 200 and test_order.json()['success'] == True

    @allure.title('Получаем заказы пользователя без авторизации')
    @allure.step('Пытаемся получить заказы пользователя без авторизации и получаем ошибку')
    def test_receive_orders__no_auth_fail(self, create_and_delete_user):
        requests.post(Urls.MAIN_URL + Urls.CREATE_ORDER, data=TestOrder.correct_ingredients)
        test_order = requests.get(Urls.MAIN_URL + Urls.CREATE_ORDER)
        assert test_order.status_code == 401 and test_order.json()['message'] == ApiResponses.RECEIVE_ORDERS_NO_AUTH


