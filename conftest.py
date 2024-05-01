import pytest
from selenium import webdriver
import requests

from data.urls import URLS
from data.user_data import Person
from data.urls import Endpoints
from data.ingredients import Ingredients
from pages.main_page import HeaderPage, MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(URLS.url_main)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(URLS.url_main)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user():
    payload = Person.create_data_correct_user()
    response = requests.post(URLS.url_main + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(URLS.url_main + Endpoints.DELETE_USER, headers={"Authorization": token})


@pytest.fixture
def login(driver, create_new_user):
        create_user_data = create_new_user[0]
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        header_page.click_profile_area_btn()
        login_page.login(create_user_data["email"], create_user_data["password"])
        main_page = MainPage(driver)
        main_page.wait_load_main_page()
        return driver


@pytest.fixture
def create_order(create_new_user):
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(URLS.url_main + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_data)
    return response.json()["order"]["number"]


# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)
