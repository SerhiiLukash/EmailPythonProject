import random
import time

import allure
import pytest
from base.base_test import BaseTest

TEST_SUBJECT = "test_subject"
TEST_BODY = "test_body"


@allure.feature("Sending Email Functionality")
class TestEmailSending(BaseTest):

    @allure.title("Send email")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_send_email(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_signin_button()
        self.new_message_page.click_new_message()
        self.new_message_page.fill_in_recipient(self.data.LOGIN)
        self.new_message_page.fill_in_subject(TEST_SUBJECT)
        self.new_message_page.fill_in_body(TEST_BODY)
        self.new_message_page.click_send()
