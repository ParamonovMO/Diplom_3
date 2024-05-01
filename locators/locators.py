from selenium.webdriver.common.by import By


class HeaderPageLocatrors:
    """Хедер"""

    constructor_btn = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")                            # Кнопка конструктор
    order_feed_btn = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")                           # Кнопка лента заказов
    personal_account_btn = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")                    # Кнопка личного кабинета


class MainPageLocators:
    """Главная страница"""

    order_feed_form = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")                    # Форма ленты заказа
    constructor_form = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']") # Форма конструктора
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")                          # Кнопка оформить заказ
    fluorescent_bun_btn = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")                  # Кнопка флюорисцентной булки
    close_popup_form = (By.XPATH, '//button[contains(@class,"close")]')                              # Крестик на модульном окне
    counter_ingredient = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")         # Счетчик ингредиента
    order_form = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")                      # Форма оформленного заказа
    order_basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")             # Корзина
    order_num = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")            # Номер заказа
    personal_account_btn = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")              # Кнопка личного кабинета
    popup_form_ingrediens = (By.XPATH, "//h2[text()= 'Детали ингредиента']")                         # Форма флюорисцентной булки


class AuthPageLocators:
    """Форма авторизации"""

    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")                                   # Форма авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']")                                             # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")                                        # Поле ввода пароля
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']")                                     # Кнопка войти
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")                              # Кнопка зерегистрироваться
    recover_btn = (By.XPATH, "//a[text() = 'Восстановить пароль']")                                  # Кнопка восстановить пароль


class RecoveryPageLocators:
    """Форма восстановления пароля"""

    email_input = (By.XPATH, ".//input[@name = 'name']")                                             # Поле ввода email
    recover_btn = (By.XPATH, ".//button[text() = 'Восстановить']")                                   # Кнопка восстановить
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")                                         # Кнопка войти
    password_input = (By.XPATH, ".//input[@name = 'Введите новый пароль']")                          # Поле ввода нового пароля
    code_from_mail = (By.XPATH, ".//label[text() = 'Введите код из письма']")                        # Поле ввода кода из письма
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         # Кнопка Сохранить
    recovery_text_form = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")                       # ФОрма восстановления пароля
    show_btn = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")                       # Показать пароль
    input_field_active = (By.CSS_SELECTOR, ".input.input_status_active")                             # Подсветка поля пароль


class PersonalAreaLocators:
    """Форма личного кабинета"""

    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")                           # Форма личного кабинета
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")                                             # Кнопка профиль
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")                               # Кнопка история заказов
    history_order_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")                  # Форма истории заказов
    number_order = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")                  # Номер заказа
    cancel_btn = (By.XPATH, ".//button[text() = 'Отмена']")                                          # Кнопка отмена
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         # Кнопка сохранить
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")                                             # Кнопка выход


class OrderFeedLocators:
    """Форма Лента заказов"""

    title_orders_list = (By.XPATH, '//h1[text()="Лента заказов"]')                                   # Заголовок страницы
    orders_info = (By.XPATH, '//p[text()="Cостав"]')                                                 # Окно детали заказа
    total_orders_counter = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик заказов за все время
    dayly_orders_counter = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")    # Счетчик заказов за сегодня
    number_order_in_job = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")          # Заказы "В работе"
    order_info_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")     # 1 заказ в истории
    order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')                 # Все заказы в истории