from data.ingredients import Ingredients
from data.urls import URLS, Endpoints
import requests
import allure


class Order:
    """Методы отправки запросов API для создания / получения номера заказа"""

    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        requests.post(URLS.url_main + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_data)

    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(URLS.url_main + Endpoints.GET_ORDERS, headers=headers)
        return response.json()["orders"][0]["number"]
