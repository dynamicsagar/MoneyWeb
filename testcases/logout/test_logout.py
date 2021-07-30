import unittest
import pytest

from utilities.util import *
from pages.logout.logout_page import LogoutPage


@pytest.mark.run(order=3)
@pytest.mark.usefixtures("oneTimeSetUp")
class LogoutTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.logout = LogoutPage(self.driver)

    def test_001_verify_logout_popup_title(self):
        """Verify logout popup title"""
        self.logout.verifyPopupTitle()

    def test_002_verify_logout_popup_text(self):
        """Verify logout popup text."""
        self.logout.verifyPopupText()

    def test_003_verify_close_icon(self):
        """Verify clicking on the close icon close the logout popup"""
        self.logout.verifyCloseIcon()

    def test_004_verify_cancel_button(self):
        """Verify clicking on cancel button close the logout popup"""
        self.logout.verifyCancelButton()

    def test_005_logout_successfully(self):
        """Verify user is able to logout successfully."""
        self.logout.verifyLogoutSuccessfully()
