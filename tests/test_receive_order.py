import allure
from utils.methods import OrderMethods
from utils.data import ApiResponses


class TestReceiveOrder:
    @allure.title('Получаем заказы пользователя с авторизацией')
    @allure.step('Получаем заказы пользователя с авторизацией и проверяем ответ')
    def test_receive_orders_with_auth_success(self, with_token):
        OrderMethods.create_order_with_auth(with_token)
        test_order = OrderMethods.receive_orders_with_auth(with_token)
        assert test_order.status_code == 200 and test_order.json()['success'] == True

    @allure.title('Получаем заказы пользователя без авторизации')
    @allure.step('Пытаемся получить заказы пользователя без авторизации и получаем ошибку')
    def test_receive_orders__no_auth_fail(self, no_token):
        OrderMethods.create_order_no_auth()
        test_order = OrderMethods.receive_orders_no_auth()
        assert test_order.status_code == 401 and test_order.json()['message'] == ApiResponses.RECEIVE_ORDERS_NO_AUTH


