import time

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from utilities.util import *


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    # Locators
    _username_field = "//input[@id='loginForm.handle']"
    _password_field = "//input[@id='loginForm.password']"
    _forgot_password_link = "//a[contains(text(),'Forgot password?')]"
    _forgot_password_page_heading = "//h2[contains(text(),'Forgot password?')]"
    _forgot_password_page_cancel_button = "//a[contains(text(),'Cancel')]"
    _login_button = "//button[contains(text(),'Login')]"
    _username_field_validation_icon = ".fas"
    _username_empty_field_validation_message = "//div[contains(text(),'Username / Email Address is required')]"
    _username_min_character_validation_message = '''//div[contains(text(),"Can't use spaces or special
     characters and must be")]'''
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
        time.sleep(1)
        return self.get_text(self._username_min_character_validation_message)

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
        time.sleep(2)
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
        # userName = self.utility.get_data(userName)
        self.enterUserName(userName)
        self.enterPassword(UserPassword)
        self.clickLoginButton()

    # Assertions
    def verifyForgotPasswordLink(self):
        self.clickForgotPasswordLink()
        text = self.getForgotPasswordPageHeadingText()
        self.verify_text_match(text, FORGOT_PASSWORD_PAGE_HEADING)
        self.clickForgotPasswordPageCancelButton()

    def verifyLoginWithEmptyUsername(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getUserNameFieldEmptyText()
        self.verify_text_match(text, EMPTY_USER_NAME)

    def verifyUserNameFieldValidation(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getUserNameValidationMessage()
        self.verify_text_match(text, USER_NAME_VALIDATION)

    def verifyLoginWithEmptyPassword(self, userName, UserPassword):
        self.login(userName, UserPassword)
        text = self.getPasswordEmptyFieldText()
        self.verify_text_match(text, EMPTY_PASSWORD_MESSAGE)

    def verifyLoginWhenUsernameInvalid(self, userName, UserPassword):
        self.login(userName, UserPassword)
        time.sleep(1)
        text = self.getInvalidUserNameOrPasswordErrorMessage()
        self.verify_text_contains(text, INVALID_LOGIN)

    def verifyLoginWhenPasswordInvalid(self, userName, UserPassword):
        time.sleep(2)
        self.login(userName, UserPassword)
        time.sleep(1)
        text = self.getInvalidUserNameOrPasswordErrorMessage()
        self.verify_text_contains(text, INVALID_PASSWORD_ATTEMPT)

    def verifyLoginSuccessfully(self, userName, UserPassword):
        # utility = Util()
        # user = ''
        # if user == 'owner':
        #     username = utility.get_data(userName)
        #     self.login(userName, UserPassword)
        # elif user == 'manager':
        #     username = utility.get_data(userName)
        #     self.login(userName, UserPassword)
        # elif user == 'dev':
        #     username = utility.get_data(userName)
        #     self.login(userName, UserPassword)
        # elif user == 'contractor':
        #     username = utility.get_data(userName)
        #     self.login(userName, UserPassword)
        # else:
        #     username = utility.get_data(userName)
        #     self.login(userName, UserPassword)
        # userName = self.utility.get_data('admin')
        # userName = self.utility.get_data(1)
        self.login(userName, UserPassword)




