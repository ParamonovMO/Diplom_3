import allure

from locators.locators import PersonalAreaLocators
from pages.base_page import BasePage


class ProfileAreaPage(BasePage):
    """Методы взаимодействия со страницей 'Личный кабинет'"""

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        return self.check_element(PersonalAreaLocators.profile_form)

    @allure.step('Клик по кнопке "Профиль"')
    def click_profile_btn(self):
        self.click_button(PersonalAreaLocators.profile_btn)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders_btn(self):
        self.click_button(PersonalAreaLocators.order_history_btn)

    @allure.step('Проверка отображения формы "История заказов"')
    def check_history_form(self):
        return self.check_element(PersonalAreaLocators.history_order_form)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_btn(self):
        self.click_button(PersonalAreaLocators.exit_btn)

    @allure.step('Клик по кнопке "Отмена"')
    def click_cansel_btn(self):
        self.click_button(PersonalAreaLocators.exit_btn)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        self.click_button(PersonalAreaLocators.save_btn)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        return self.get_text_locator(PersonalAreaLocators.number_order)
