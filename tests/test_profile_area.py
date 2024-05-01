import allure

from data.urls import URLS
from pages.main_page import HeaderPage
from pages.login_page import LoginPage
from pages.profile_area_page import ProfileAreaPage


class TestProfilelAreaPage:

    @allure.title('Проверка перехода в "Личный кабинет"')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        2. Логин в систему;
                        3. Клик по кнопке "Личный кабинет";
                        4. Проверяем отображение формы "Личный кабинет";
                        5. Удаляем пользователя через API.
                        ''')
    def test_follow_to_profile_area_page(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()
        assert profile_area.check_profile_area_form() and driver.current_url == URLS.url_profile_area

    @allure.title('Проверка перехода в "История Заказов"')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в систему;
                        4. Клик по кнопке "Личный кабинет";
                        5. Клик по кноке "История заказов";
                        6. Провеям отображение формы "История заказов";
                        7. Удаляем пользователя через API.
                        ''')
    def test_follow_to_feed_orders(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()
        profile_area.click_history_orders_btn()
        assert profile_area.check_profile_area_form() and driver.current_url == URLS.url_history_order

    @allure.title('Проверка выхода из аккаунта"')
    @allure.description('''
                        1. Создаем пользователя через API;
                        2. Переход на страницу сервиса;
                        3. Логин в систему;
                        4. Клик по кнопке "Личный кабинет";
                        5. Клик по кноке "Выход";
                        6. Проверяем выход из аккаунта;
                        7. Удаляем пользователя через API.
                        ''')
    def test_exit_profile_area(self, driver, create_new_user, login):
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        login_page = LoginPage(driver)
        header.click_profile_area_btn()
        profile_area.click_exit_btn()
        assert login_page.check_authorization_form_verification() and driver.current_url == URLS.url_login
