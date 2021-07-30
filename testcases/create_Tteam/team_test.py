import unittest
import pytest

from utilities.util import *
from pages.create_team.team_page import TeamCreationPage
from testcases.test_config import *


@pytest.mark.run(order=2)
@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.team = TeamCreationPage(self.driver)
        self.utility = Util()

    def test_001_verify_team_modal_box_title(self):
        """Verify title of the modal box"""
        self.team.verify_team_modal_title()

    def test_002_click_team_modal_box_close_icon(self):
        """Verify user is able to close the team modal box using close icon."""
        self.team.verify_close_icon_close_the_team_modal_box()

    def test_003_click_team_modal_box_cancel_button(self):
        """Verify user is able to close the team modal box using cancel button"""
        self.team.verify_cancel_button_close_the_team_modal_box()

    def test_004_verify_create_team_button_disable(self):
        """Verify create team button is in disable state."""
        self.team.verify_create_team_button_disable()

    def test_005_create_new_team_successfully(self):
        """Verify user is able to create a new team successfully."""
        self.team.verify_create_team_successfully(name)
