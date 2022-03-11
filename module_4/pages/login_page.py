from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK)

    def should_be_login_form(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*MainPageLocators.EMAIL)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*MainPageLocators.PASSWORD)
        password_input.send_keys(password)

        confirm_password = self.browser.find_element(*MainPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)

        register = self.browser.find_element(*MainPageLocators.REGISTER_BUTTON)
        register.click()
