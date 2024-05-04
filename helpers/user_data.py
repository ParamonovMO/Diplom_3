from faker import Faker
import allure


class Person:
    """Метод генерации данных для регистрации"""

    @staticmethod
    @allure.step('Генерация email, password, name пользователя')
    def create_data_correct_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data
