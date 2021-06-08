# import unittest
# import pytest
#
# from utilities.util import *
# from pages.test001_login_page import LoginPage
#
#
# @pytest.mark.run(order=1)
# @pytest.mark.usefixtures("oneTimeSetUp", "setUp")
# class LoginTests(unittest.TestCase):
#     log = cl.customLogger(logging.DEBUG)
#
#     @pytest.fixture(autouse=True)
#     def objectSetup(self, oneTimeSetUp):
#         self.login = LoginPage(self.driver)
#
#     def test_001_verify_user_login_successfully(self):
#         """Verify user is able to login successfully."""
#         self.login.verify_login_successfully()
#
#     def test_002_verify_logout_from_dashboard_screen(self):
#         """Verify user is able to logout from dashboard screen."""
#         self.login.logout()
#
#     def test_003_verify_login_with_invalid_login_id(self):
#         """Verify user is not able to login with an invalid account."""
#         # self.login.anotherUser()
#         # self.login.login_with_invalid_credentials("pankaj@arcgate.com", "Welfdsfsdfsdfcome123!")
#         self.login.verify_invalid_login_validation_message()
