# Дипломный проект. Задание 3: UI

Автотесты для сервиса  "Stellar Burger". 
Сайт: `https://stellarburgers.nomoreparties.site/`

## Файлы:
- allure_results - каталог с отчетом о тестировании

- tests/test_main_page.py - файл с проверками основного функционала 
- tests/test_order_feed.py - файл с проверками ленты заказов
- tests/test_profile_area.py - файл с проверками личного кабинета
- tests/test_recovery_page.py - файл с проверками восстановления пароля

- locators/locators.py - файл с локаторами элементов сервиса

- helpers/user_data.py - файл с методами генерации данных для регистрации
- helpers/helpers.py - файл с методами создания / получения заказа через API

- data/urls - файл с URL сервиса и ручками
- data/ingredients.py -  файл с данными ингредиентов



- pages/base_page.py - файл с базовыми методами взаимодействия
- pages/login_page.py - файл с методами взаимодействия со страницей логина
- pages/main_page.py - файл с методами взаимодействия с главной страницей
- pages/order_feed_page.py - файл с методами взаимодействия со страницей ленты заказов
- pages/profile_area_page.py - файл с методами взаимодействия со страницей личного кабинета
- pages/recovery_page.py - файл взаимодействия со страницей восстановления пароля

- requirements.txt - файл с внешними зависимостями
- conftest.py - файл с фикстурой

Перед работой с репозиторием требуется установить зависимости 
```
pip install -r requirements.txt
```
Запустить все тесты
```
pytest tests --alluredir=allure_results
```
Посмотреть отчет о тестировании
```
allure serve allure_results
```
