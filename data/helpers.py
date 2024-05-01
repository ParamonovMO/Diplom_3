from data.ingredients import Ingredients
from data.urls import URLS, Endpoints
import requests


class Order:
    """Методы отправки запросов API для создания / получения номера заказа"""

    def create_order(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        requests.post(URLS.url_main + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_data)

    def get_user_orders(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(URLS.url_main + Endpoints.GET_ORDERS, headers=headers)
        return response.json()["orders"][0]["number"]
