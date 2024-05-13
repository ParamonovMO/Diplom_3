import allure

from pages.base_page import BasePage
from locators.locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step('Получение кол-ва заказов')
    def check_counter_orders(self, locators):
        return self.get_text_locator(locators)

    @allure.step('Клик на 1 заказ в "Лента заказов"')
    def click_order_info(self):
        self.click_button(OrderFeedLocators.order_info_window)

    @allure.step('Проверка видимости формы заказа')
    def check_order_info_window(self):
        return self.check_element(OrderFeedLocators.orders_info)

    @allure.step('Получение заказов "В работе"')
    def get_orders_in_jobs(self):
        elements = self.get_text_locators(OrderFeedLocators.number_order_in_job)
        orders_list = []
        for element in elements:
              order_number = element.text[1:]
              orders_list.append(order_number)
        return orders_list

    @allure.step('Получение списка всех заказов в "Лента заказов"')
    def get_text_all_orders(self):
        elements = self.get_orders_history()
        text_list = []
        for element in elements:
            text_list.append(element)
        return text_list

    @allure.step('Получение номеров заказов')
    def get_orders_history(self):
        elements = self.get_text_locators(OrderFeedLocators.order_history)
        orders_list = []
        for element in elements:
              order_number = element.text[2:]
              orders_list.append(order_number)
        return orders_list
