import allure

from data.urls import URLS
from helpers.user_data import Person
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        ''')
    def test_follow_to_the_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        assert recovery_page.check_recovery_form() and driver.current_url == URLS.url_recovery

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        4. Заполнение поля "Email"
                        5. Клик на кнопку "Восстановить"
                        ''')
    def test_input_password_and_click_recovery_btn(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.send_email_to_email_field(Person.create_data_correct_user()["email"])
        recovery_page.click_recovery_btn()
        assert recovery_page.check_save_btn() and driver.current_url == URLS.url_reset_password

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        4. Заполнение поля "Email"
                        5. Клик на кнопку "Восстановить"
                        6. Заполнить поле "Пароль"
                        7. Клик на кнопку "Показать"
                        ''')
    def test_checking_the_backlight_of_the_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.send_email_to_email_field(Person.create_data_correct_user()["email"])
        recovery_page.click_recovery_btn()
        assert recovery_page.check_active_password_field(Person.create_data_correct_user()["password"])
