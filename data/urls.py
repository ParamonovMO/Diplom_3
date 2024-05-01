class URLS:
    """URLs сервиса"""
    url_main = 'https://stellarburgers.nomoreparties.site/'                                # Главная страница сервиса
    url_feed = 'https://stellarburgers.nomoreparties.site/feed'                            # Лента заказов
    url_login = 'https://stellarburgers.nomoreparties.site/login'                          # Авторизация
    url_recovery = 'https://stellarburgers.nomoreparties.site/forgot-password'             # Восстановление пароля
    url_register = 'https://stellarburgers.nomoreparties.site/register'                    # Регистрация пользователя
    url_profile_area = 'https://stellarburgers.nomoreparties.site/account/profile'         # Личный кабинет
    url_history_order = 'https://stellarburgers.nomoreparties.site/account/order-history'  # История заказов
    url_reset_password = 'https://stellarburgers.nomoreparties.site/reset-password'        # Сброс пароля


class Endpoints:
    """Ручки для работы с API"""

    CREATE_USER = 'api/auth/register'
    LOGIN = 'api/auth/login'
    DELETE_USER = 'api/auth/user'
    CREATE_ORDER = 'api/orders'
    GET_ORDERS = 'api/orders'
