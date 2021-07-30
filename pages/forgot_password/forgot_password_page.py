import time

from base.selenium_driver import SeleniumDriver
from pages.register.register_page import RegisterPage
from pages.login.login_page import LoginPage
from testcases.message import *


class ForgotPasswordPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.register = RegisterPage(driver)
        self.login = LoginPage(driver)

    # Locators
    _user_email_field = "//input[@id='forgotPasswordForm.email']"
    _submit_button = "//button[contains(text(),'Submit')]"
    _email_field_validation_icon = ".ml-2"
    _email_address_required_validation_message = "//div[contains(text(),'Email Address is required')]"

    def getEmptyEmailAddressValidationText(self):
        self.wait_for_element(self._email_field_validation_icon)
        self.element_click(self._email_field_validation_icon)
        return self.get_text(self._email_address_required_validation_message)

    def enterEmailField(self, email):
        self.wait_for_element(self._user_email_field)
        self.element_click(self._user_email_field)
        self.send_keys(clear_field, self._user_email_field)
        self.send_keys(email, self._user_email_field)

    def ClickForgotPasswordLink(self):
        self.login.clickForgotPasswordLink()

    def clickSubmitButton(self):
        self.element_click(self._submit_button)

    # Method
    def forgotPassword(self, email):
        self.enterEmailField(email)
        self.clickSubmitButton()

    # Assertions
    def VerifyEmptyEmailValidation(self):
        text = self.getEmptyEmailAddressValidationText()
        self.verify_text_match(text, email_address_required)

    def verifyInvalidEmail(self):
        self.register.verifyEmailValidationMessage(email_type="invalid")

    def verifyForgotPasswordSuccessfully(self, email):
        self.forgotPassword(email)
