import allure
import pytest

from pages.main_page import HeaderPage
from pages.order_feed_page import OrderFeedPage
from locators.locators import OrderFeedLocators
from data.helpers import Order


class TestOrderFeedPage:

    @allure.title('Проверка если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик на кнопку "Лента заказов";
                        3. Клик на 1 заказ;
                        4. Проверка отображения формы с деталями заказа.
                        ''')
    def test_check_order_info_window(self, driver):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        feed_order.click_order_info()
        assert feed_order.check_order_info_window()

    @allure.title('Проверка после оформления заказа его номер появляется в разделе В работе')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переходим на страницу сервиса;
                        3. Логин в систему;
                        4. Переход на страницу "Лента заказов";
                        5. Получаем заказ в списке "В работе";
                        6. Получаем список заказов пользователя;
                        7. Проверяем, что заказ пользователя в списке заказов "В работе";
                        8. Удаляем пользователя через API.
                        ''')
    def test_check_user_order_in_job(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        Order().create_order(create_new_user)
        orders_in_jobs = feed_order.get_orders_in_jobs()
        user_order = str(Order().get_user_orders(create_new_user))
        assert user_order in orders_in_jobs

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Создаем заказ через API;
                        2. Переходим на страницу сервиса;
                        3. Логин в систему;
                        4. Переход на страницу "Лента заказов";
                        5. Получаем заказа пользователя через API;
                        6. Получаем список заказов на странице "Лента заказов"
                        7. Проверяем отображения заказа пользователя;
                        8. Удаляем пользователя через API.
                        ''')
    def test_check_user_orders_in_orders_history(self, driver, create_new_user, create_order, login):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        user_order = str(Order().get_user_orders(create_new_user))
        orders_history_in_feed = feed_order.get_orders_history()
        assert user_order in orders_history_in_feed

    @allure.title('При создании нового заказа счетчик Выполнено за всё время / Выполнено за сегодня увеличивается')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переходим на страницу сервиса;
                        3. Логин в систему;
                        4. Переход на страницу "Лента заказов";
                        5. Получаем текущее значение счетчика;
                        6. Отправляем запрос на создание заказа через API;
                        7. Проверяем увеличение счетчика;
                        8. Удаляем пользователя через API.
                        ''')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.dayly_orders_counter, OrderFeedLocators.total_orders_counter])
    def test_update_counter_orders(self, driver, create_new_user, login, counter):
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        now_counter = int(feed_order.check_counter_orders(counter))
        Order().create_order(create_new_user)
        new_counter = int(feed_order.check_counter_orders(counter))
        assert new_counter > now_counter
