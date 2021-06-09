import time

from base.selenium_driver import SeleniumDriver
from testcases.message import *


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "//input[@id='loginForm.handle']"
    _password_field = "//input[@id='loginForm.password']"
    _forgot_password_link = "//a[contains(text(),'Forgot password?')]"
    _forgot_password_page_heading = "//h2[contains(text(),'Forgot password?')]"
    _forgot_password_page_cancel_button = "//a[contains(text(),'Cancel')]"
    _login_button = "//button[contains(text(),'Login')]"
    _username_field_validation_icon = ".fas"
    _username_empty_field_validation_message = "//div[contains(text(),'Username / Email Address is required')]"
    _username_enter_special_character_validation_message = '''//div[contains(text(),"Can't use spaces or special characters and must be")]'''
    _password_field_validation_icon = ".ml-2:nth-child(2) > .fas"
    _password_empty_field_validation = "//div[contains(text(),'Password is required')]"
    _flex_error_message = ".fade > .d-flex"

    def getForgotPasswordPageHeadingText(self):
        self.wait_for_element(self._forgot_password_page_heading)
        return self.get_text(self._forgot_password_page_heading)

    def getUserNameFieldEmptyText(self):
        self.wait_for_element(self._username_field_validation_icon, 'css')
        self.element_click(self._username_field_validation_icon, 'css')
        return self.get_text(self._username_empty_field_validation_message)

    def getUserNameValidationMessage(self):
        self.wait_for_element(self._username_field_validation_icon, 'css')
        self.element_click(self._username_field_validation_icon, 'css')
        return self.get_text(self._username_enter_special_character_validation_message)

    def getPasswordEmptyFieldText(self):
        self.wait_for_element(self._password_field_validation_icon, 'css')
        self.element_click(self._password_field_validation_icon, 'css')
        return self.get_text(self._password_empty_field_validation)

    def getInvalidUserNameOrPasswordErrorMessage(self):
        self.wait_for_element(self._flex_error_message, 'css')
        return self.get_text(self._flex_error_message, 'css')

    def enterUserName(self, userName):
        self.wait_for_element(self._username_field)
        self.element_click(self._username_field)
        self.send_keys(clear_field, self._username_field)
        self.send_keys(userName, self._username_field)

    def enterPassword(self, UserPassword):
        self.element_click(self._password_field)
        self.send_keys(clear_field, self._password_field)
        self.send_keys(UserPassword, self._password_field)

    def clickLoginButton(self):
        time.sleep(5)
        self.web_scroll('down')
        self.element_click(self._login_button)

    def clickForgotPasswordPageCancelButton(self):
        self.wait_for_element(self._forgot_password_page_cancel_button)
        self.element_click(self._forgot_password_page_cancel_button)

    def clickForgotPasswordLink(self):
        self.wait_for_element(self._forgot_password_link)
        self.element_click(self._forgot_password_link)

    # Method
    def login(self, userName="", UserPassword=""):
        self.enterUserName(userName)
        self.enterPassword(UserPassword)
        self.clickLoginButton()

    # Assertions
    def verifyForgotPasswordLink(self):
        self.clickForgotPasswordLink()
        text = self.getForgotPasswordPageHeadingText()
        self.verify_text_match(text, forgot_password_page_heading)
        self.clickForgotPasswordPageCancelButton()

    def verifyLoginWithEmptyUsername(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getUserNameFieldEmptyText()
        self.verify_text_match(text, empty_user_name)

    def verifyUserNameFieldValidation(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getUserNameValidationMessage()
        self.verify_text_match(text, user_name_validation)

    def verifyLoginWithEmptyPassword(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getPasswordEmptyFieldText()
        self.verify_text_match(text, empty_password)

    def verifyLoginWhenUsernameInvalid(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getInvalidUserNameOrPasswordErrorMessage()
        self.verify_text_contains(text, invalid_login)

    def verifyLoginWhenPasswordInvalid(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getInvalidUserNameOrPasswordErrorMessage()
        self.verify_text_contains(text, invalid_password_attempt)

    def verifyLoginSuccessfully(self, userName, UserPassword):
        self.login(userName, UserPassword)




