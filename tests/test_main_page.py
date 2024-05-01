import allure

from data.urls import URLS
from pages.main_page import MainPage, HeaderPage


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Войти в аккаунт";
                        3. Клик по кнопке "Конструктор";
                        4. Проверяем отображение формы "Конструктор".
                        ''')
    def test_follow_to_constructor_page(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        header.click_constructor_btn()
        assert main_page.check_constructor_form() and driver.current_url == URLS.url_main

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Лента заказов";
                        3. Проверяем отображение формы "Лента заказов".
                        ''')
    def test_follow_to_orders_feed_page(self, driver):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_feed_btn()
        assert main_page.check_orders_feed_form() and driver.current_url == URLS.url_feed

    @allure.title('Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Флюорисцентная булка R2-D3.
                        3. Проверка отображения высплывающего окна с деталями ингредиента.
                        ''')
    def test_check_fluorescent_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()
        assert main_page.check_fluorescent_bun_form()

    @allure.title('Проверка закрытия всплывающего окна по крестику')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Клик по кнопке "Флюорисцентная булка R2-D3;
                        3. Клик по крестику модального окна;
                        4. Проверка закрытия формы "Информация об ингредиенте".
                        ''')
    def test_close_fluorescent_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()
        main_page.close_popup_form()
        assert main_page.check_close_fluorescent_bun_form()

    @allure.title('Проверка при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Добавление "Флюорисцентная булка R2-D3 в корзину";
                        3. Проверка увеличения счетчика ингредиента.
                        ''')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_bun()
        assert int(main_page.check_counter_ingredient()) > 0

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в системе;
                        4. Добавление "Флюорисцентная булка R2-D3 в корзину";
                        5. Клик по кнопке "Оформить заказ";
                        6. Проверка отображения формы заказа;
                        7. Удаляем пользователя через API.
                        ''')
    def test_create_order(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_constructor_btn()
        main_page.create_order()
        assert main_page.check_order_form()
