import unittest
import pytest

from utilities.util import *
from pages.login.login_page import LoginPage
from testcases.test_config import *


@pytest.mark.run(order=2)
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.login = LoginPage(self.driver)

    def test_001_click_forgot_password_link(self):
        """Verify user is able to navigate to forgot password screen"""
        self.login.verifyForgotPasswordLink()

    # def test_002_login_when_user_name_is_empty(self):
    #     """Verify user is not able to login when username field is empty."""
    #     self.login.verifyLoginWithEmptyUsername(' ', password)

    def test_003_login_when_user_name_is_less_than_min_characters(self):
        """Verify user is not able to login when username field is less than 3 characters."""
        self.login.verifyUserNameFieldValidation('a', password)

    # def test_004_login_when_password_field_is_empty(self):
    #     """Verify user is not able to login when password field is empty."""
    #     self.login.verifyLoginWithEmptyPassword(user_email, ' ')

    def test_005_login_with_invalid_user_name(self):
        """Verify user is not able to login when enter invalid username"""
        self.login.verifyLoginWhenUsernameInvalid("silaqaautomation+Ownerkilssqn07j52qsdfpj@gmail.com", password)

    def test_006_login_with_invalid_password(self):
        """Verify user is not able to login when enter invalid username"""
        self.login.verifyLoginWhenPasswordInvalid("silaqaautomation+Ownerkilqn07j52qsdfpj@gmail.com", invalid_password)

    def test_007_login_successfully(self):
        """Verify user is not able to login when enter invalid username"""
        self.login.verifyLoginSuccessfully(user_email, password)
