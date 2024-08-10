import allure
from utils.methods import OrderMethods
from utils.data import ApiResponses


class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией с ингредиентами')
    @allure.step('Пользователь создает заказ с авторизацией и проверяем ответ')
    def test_create_order_with_auth_success(self, with_token):
        test_order = OrderMethods.create_order_with_auth(with_token)
        assert test_order.status_code == 200 and test_order.json()['success']

    @allure.title('Создание заказа без авторизации')
    @allure.step('Пользователь создаёт заказ без авторизации и получаем ошибку')
    def test_create_order_no_auth_success(self, no_token):
        test_order = OrderMethods.create_order_no_auth()
        assert test_order.status_code == 200 and test_order.json()['success'] == True

    @allure.title('Создание заказа без ингредиентов')
    @allure.step('Пользователь создаёт заказ без ингредиентов и получает ошибку')
    def test_create_order_no_ingredients_fail(self, no_token):
        test_order = OrderMethods.create_order_no_ingredients()
        assert (test_order.status_code == 400 and test_order.json()['message'] ==
                ApiResponses.CREATE_ORDER_NO_INGREDIENTS)

    @allure.title('Создание заказа с невалидным хэшем ингредиентов')
    @allure.step('Пользователь создаёт заказ с невалидным хешем ингредиентов и получает ошибку')
    def test_create_order_invalid_hash_fail(self,no_token):
        test_order = OrderMethods.create_order_invalid_hash()
        assert test_order.status_code == 500 and ApiResponses.INVALID_HASH in test_order.text
