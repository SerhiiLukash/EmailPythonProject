import pytest


from pages.login_page import LoginPage
from pages.new_message_page import NewMessagePage
from config.data import Data
from conftest import driver

class BaseTest:

    data: Data

    login_page: LoginPage
    new_message_page: NewMessagePage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data

        request.cls.login_page = LoginPage(driver)
        request.cls.new_message_page = NewMessagePage(driver)
