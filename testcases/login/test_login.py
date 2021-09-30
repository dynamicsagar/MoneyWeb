import unittest
import pytest

from utilities.util import *
from pages.login.login_page import LoginPage
from testcases.test_config import *


@pytest.mark.run(order=2)
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTest):
        self.login = LoginPage(self.driver)
        self.utility = Util()
        global username
        username = self.utility.get_data(1)
        return username

    def test_001_click_forgot_password_link(self):
        """Verify user is able to navigate to forgot password screen"""
        self.login.verifyForgotPasswordLink()

    # def test_002_login_when_user_name_is_empty(self):
    #     """Verify user is not able to login when username field is empty."""
    #     self.login.verifyLoginWithEmptyUsername(' ', password)

    def test_003_login_when_user_name_is_less_than_min_characters(self):
        """Verify user is not able to login when username field is less than 3 characters."""
        self.login.verifyUserNameFieldValidation('a', PASSWORD)

    # def test_004_login_when_password_field_is_empty(self):
    #     """Verify user is not able to login when password field is empty."""
    #     self.login.verifyLoginWithEmptyPassword(user_email, ' ')

    def test_005_login_with_invalid_user_name(self):
        """Verify user is not able to login when enter invalid username"""
        invalid_user = name + "test" + "@mail.com"
        self.login.verifyLoginWhenUsernameInvalid(invalid_user, PASSWORD)

    def test_006_login_with_invalid_password(self):
        """Verify user is not able to login when enter invalid username"""
        # admin = self.utility.get_data(1)
        self.login.verifyLoginWhenPasswordInvalid(username, INVALID_PASSWORD)

    def test_007_login_successfully(self):
        """Verify user is able to login successfully"""
        self.login.verifyLoginSuccessfully(username, PASSWORD)
        email_after_plus = username.replace("silaqaautomation+", '')
        email_after_plus = email_after_plus.replace("@gmail.com", "")
        print(email_after_plus)
        self.log.info(email_after_plus)
        self.login.get_mfa_code(email_after_plus)



