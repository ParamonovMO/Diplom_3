import allure

from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators


class RecoveryPage(BasePage):
    """Методы взаимодействия со страницей 'Восстановление пароля'"""

    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        return self.check_element(RecoveryPageLocators.recovery_text_form)

    @allure.step('Заполнение формы Email')
    def send_email_to_email_field(self, email):
        self.send_keys_to_field(RecoveryPageLocators.email_input, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_recovery_btn(self):
        self.click_button(RecoveryPageLocators.recover_btn)

    @allure.step('Клик по кнопке Войти')
    def click_login_btn(self):
        self.click_button(RecoveryPageLocators.login_account_btn)

    @allure.step('Заполнение поля Пароль')
    def send_password_to_password_field(self, password):
        self.send_keys_to_field(RecoveryPageLocators.password_input, password)

    @allure.step('Заполнение поля Код из письма')
    def send_code_to_code_field(self, code):
        self.send_keys_to_field(RecoveryPageLocators.code_from_mail, code)

    @allure.step('Клик по кнопке Сохранить')
    def click_save_btn(self):
        self.click_button(RecoveryPageLocators.save_btn)

    @allure.step('Проверка подсветки поля Пароль')
    def check_active_password_field(self, password):
        self.send_password_to_password_field(password)
        self.click_button(RecoveryPageLocators.show_btn)
        return self.check_element(RecoveryPageLocators.input_field_active)

    @allure.step('Проверка отображения кнопки Сохранить')
    def check_save_btn(self):
        return self.check_element(RecoveryPageLocators.save_btn)
