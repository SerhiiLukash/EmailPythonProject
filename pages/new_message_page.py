import allure
import selenium
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class NewMessagePage(BasePage):

    PAGE_URL = Links.INBOX_PAGE

    NEW_MESSAGE_BUTTON = ("xpath", "//button[text()='New message']")
    RECIPIENT_FIELD = ("xpath", "//input[@placeholder='To']")
    SUBJECT_FIELD = ("xpath", "//input[@class='input-element w-full']")
    # BODY_AREA = ("xpath", "(//div[@id='rooster-editor']//div)[1]")
    BODY_AREA = ("xpath", "//div/*[contains(text(),'Sent with')]")
    SEND_BUTTON = ("xpath", "//button[text()='Send']")

    @allure.step("Click new message button")
    def click_new_message(self):
        self.wait.until(EC.element_to_be_clickable(self.NEW_MESSAGE_BUTTON)).click()

    @allure.step("Fill in recipient field")
    def fill_in_recipient(self, recipient):
        self.wait.until(EC.element_to_be_clickable(self.RECIPIENT_FIELD)).send_keys(recipient)


    @allure.step("Fill in subject field")
    def fill_in_subject(self, subject):
        self.wait.until(EC.element_to_be_clickable(self.SUBJECT_FIELD)).send_keys(subject)

    @allure.step("Fill in body field")
    def fill_in_body(self, body_text):
        self.wait.until(EC.element_to_be_clickable(self.BODY_AREA)).click()
        self.wait.until(EC.element_to_be_clickable(self.BODY_AREA)).send_keys(body_text)


    @allure.step("Click Send button")
    def click_send(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_BUTTON)).click()