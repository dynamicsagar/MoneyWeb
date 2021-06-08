import unittest
import pytest

from utilities.util import *
from pages.Register.register_page import RegisterPage
from testcases.test_config import *


@pytest.mark.run(order=1)
@pytest.mark.usefixtures("remove_files")
class RegisterTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.register = RegisterPage(self.driver)

    def test_001_register_check_register_page(self):
        """Verify user is on register page."""
        self.register.clickSignUpLink()
        self.register.verifyPageTitle()

    # def test_002_register_when_first_name_empty(self):
    #     """Verify user is not able to register when first_name field is empty."""
    #     self.register.signUpForm('', surname, company_name, user_email, phone, password, confirm_password)
    #     self.register.clickTermsCheckbox()
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_003_register_when_surname_empty(self):
    #     """Verify user is not able to register when surname field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, '', company_name, user_email, phone, password, confirm_password)
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_004_register_when_company_name_empty(self):
    #     """Verify user is not able to register when company_name field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, surname, '', user_email, phone, password, confirm_password)
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_005_register_when_work_email_empty(self):
    #     """Verify user is not able to register when work email field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, surname, company_name, '', phone, password, confirm_password)
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_006_register_when_phone_empty(self):
    #     """Verify user is not able to register when work_phone field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, surname, company_name, user_email, '', password, confirm_password)
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_007_register_when_password_empty(self):
    #     """Verify user is not able to register when password field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, surname, company_name, user_email, phone, '', confirm_password)
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_008_register_when_confirm_password_empty(self):
    #     """Verify user is not able to register when confirm_password field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, surname, company_name, user_email, phone, password, '')
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_009_register_when_terms_checkbox_empty(self):
    #     """Verify user is not able to register when confirm_password field is empty."""
    #     self.register.clearForm()
    #     self.register.signUpForm(first_name, surname, company_name, user_email, phone, password, confirm_password)
    #     self.register.clickTermsCheckbox()
    #     self.register.verifyConfirmButtonDisable()
    #
    # def test_010_register_when_email_invalid(self):
    #     """Verify user is not able to register when email is invalid."""
    #     self.register.clearForm()
    #     self.register.signUpForm(email='test@')
    #     self.register.verifyEmailValidationMessage("invalid")

    # def test_011_register_when_email_is_more_than_255_characters(self):
    #     """Verify user is not able to register when email is more than 255 characters."""
    #     self.register.clearForm()
    #     self.register.signUpForm(email=email_above_max_length)
    #     self.register.verifyEmailValidationMessage()
    #
    # def test_012_register_when_password_is_less_than_8_characters(self):
    #     """Verify user is not able to register when password is less than 8 characters."""
    #     self.register.clearForm()
    #     self.register.signUpForm(password=password_below_min_limit)
    #     self.register.verifyPasswordValidationMessage("min")
    #
    # def test_013_register_when_password_is_more_than_100_characters(self):
    #     """Verify user is not able to register when password is more than 100 characters."""
    #     self.register.clearForm()
    #     self.register.signUpForm(password=password_above_max_limit)
    #     self.register.verifyPasswordValidationMessage('max')
    #
    # def test_014_register_when_password_and_confirm_password_mismatch(self):
    #     """Verify user is not able to register when password and confirm password mismatch."""
    #     self.register.clearForm()
    #     self.register.signUpForm(password=password, confirmPassword=mismatch_confirm_password)
    #     self.register.verifyPasswordValidationMessage('mismatch')
    #
    # def test_015_register_when_password_same_as_email(self):
    #     """Verify user is not able to register when password is similar to email."""
    #     self.register.clearForm()
    #     self.register.signUpForm(email=user_email, password=password_lookalike_email)
    #     self.register.clickTermsCheckbox()
    #     self.register.verifyPasswordValidationMessage("same_as_email")
    #
    # def test_016_register_when_phone_number_is_invalid(self):
    #     """Verify user is not able to register when entered invalid phone number."""
    #     self.register.clearForm()
    #     self.register.signUpForm(phone=invalid_phone_num)
    #     self.register.verifyPhoneValidationMessage()
    #
    # def test_017_register_click_privacy_policy(self):
    #     """Verify privacy policy link navigates user to privacy policy page.."""
    #     self.register.verifyPrivacyPolicyLink()
    #
    # def test_018_register_click_terms_of_service_link(self):
    #     """Verify terms of service link navigates user to terms and services page."""
    #     self.register.verifyTermsOfServiceLink()
    #
    # def test_019_register_click_sdk_agreement_link(self):
    #     """Verify sdk agreement link navigates user to sdk agreement page."""
    #     self.register.verifySDKAgreementLink()
    #
    # def test_020_register_click_ACH_transfer_link(self):
    #     """Verify ACH transfer api link navigates user to ach transfer page."""
    #     self.register.verifyACHTransferApiLink()
    #
    # def test_021_register_click_digital_wallet_api_link(self):
    #     """Verify digital wallet api link navigates user to digital wallet page."""
    #     self.register.verifyDigitalWalletApiLink()
    #
    # def test_022_register_click_bank_account_link(self):
    #     """Verify bank account linking api navigates user to bank account link page"""
    #     self.register.verifyBankAccountLinkingApiLink()
    #
    # def test_023_register_click_kyc_kyb_identity_verification_link(self):
    #     """Verify user navigates to kyb kyc verification page."""
    #     self.register.verifyKYCIdentityVerificationLink()
    #
    # def test_024_register_verify_already_have_account_text(self):
    #     """Verify page contains already have a sila account text."""
    #     self.register.verifyAlreadyHaveSilaAccounText()

    # def test_025_register_click_login_link(self):
    #     """Verify user is navigates to login page."""
    #     self.register.verifyLoginLink()

    def test_012_register_user_successfully(self):
        """Verify user is able to register user successfully."""
        self.register.clearForm()
        self.register.signUpForm(first_name, surname, company_name, user_email, phone, password,
                                 confirm_password)
        self.register.clickTermsCheckbox()
        self.register.clickConfirmAccountButton()
        self.register.verifySignUpSuccessfully()
        # self.register.verifyTeamNameFieldNotEmpty(company_name)
        # self.register.verifyContinueButtonState(False)
        self.register.inviteTeamMember(manager_email)
        time.sleep(25)

    # def test_0020_register_team_name_already_exist_validation(self):
    #     """Verify team name already exist error"""
    #
    # def test_0222_register_add_new_team_name(self):
    #     """Verify user is able to add new team."""
    #
    # def test_0220_register_invite_team_member(self):
    #     """Verify user is able to invite team member from add team box."""
    #
    # def test_0221_register_(self):
    #
    # def test_02222_register_user_successfully_from_email_confirmation_link(self):
    #     """Verify user should redirect to home screen after clicking on email confirmation link"""

    # def test_012_register_user_for_owner_role(self):
    #     """Verify user is able to register user for owner role."""
    #     self.register.getUrl()
    #     self.register.signUpForm(first_name, surname, company_name, owner_email, phone, password,
    #                              confirm_password)
    #     self.register.clickTermsCheckbox()
    #     self.register.clickConfirmAccountButton()
    #     self.register.verifySignUpSuccessfully()
    #
    # def test_012_register_user_for_developer_role(self):
    #     """Verify user is able to register user for developer role."""
    #     self.register.signUpForm(first_name, surname, company_name, developer_email, phone, password,
    #                              confirm_password)
    #     self.register.clickTermsCheckbox()
    #     self.register.clickConfirmAccountButton()
    #     self.register.verifySignUpSuccessfully()
    #     self.register.verifyConfirmEmail(developer)
    #
    # def test_012_register_user_for_manager_role(self):
    #     """Verify user is able to register user for manager role."""
    #     self.register.signUpForm(first_name, surname, company_name, manager_email, phone, password,
    #                              confirm_password)
    #     self.register.clickTermsCheckbox()
    #     self.register.clickConfirmAccountButton()
    #     self.register.verifySignUpSuccessfully()
    #     self.register.verifyConfirmEmail(manager)
    #
    # def test_012_register_user_for_contractor_role(self):
    #     """Verify user is able to register user for contractor role."""
    #     self.register.signUpForm(first_name, surname, company_name, contractor_email, phone, password,
    #                              confirm_password)
    #     self.register.clickTermsCheckbox()
    #     self.register.clickConfirmAccountButton()
    #     self.register.verifySignUpSuccessfully()
    #     self.register.verifyConfirmEmail(contractor)
