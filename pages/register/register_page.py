import time

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from selenium.webdriver.common.action_chains import ActionChains


class RegisterPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    url = "https://stageconsole.silamoney.com/register"
    _sila_main_logo = "//*[@id='main-logo']"
    _signup_to_move_money_heading = "//h1[contains(text(),'Sign up to move money with Sila.')]"
    _ach_transfer_link = "//a[contains(text(),'ACH Transfer API')]"
    _redirect_ach_transfer_page_heading = "//p[contains(text(),'Transfer money and initiate ACH transfers fast usi')]"
    _digital_wallet_api_link = "//a[contains(text(),'Digital Wallet API')]"
    _redirect_digital_wallet_page_heading = "//p[contains(text(),'Our Wallet API links any U.S. bank account via API')]"
    _bank_account_linking_api_link = "//a[contains(text(),'Bank Account Linking API')]"
    _redirect_bank_account_linking_page_heading = "//p[contains(text(),'Link bank accounts and transfer money fast " \
                                                  "using t')] "
    _kyc_kyb_identity_verification_api_link = "//a[contains(text(),'KYC & KYB Identity Verification API')]"
    _redirect_kyb_kyc_verification_page_heading = "//p[contains(text(),'Banking, Digital Wallet & ACH Payments API " \
                                                  "for Sof')] "
    _already_have_a_sila_account_text = "//p[contains(text(),'Already have a Sila account?')]"
    _sign_up_link = "//span[contains(text(),'Sign up')]"
    _login_link = "//span[contains(text(),'login')]"
    _login_page_heading = "//h2[contains(text(),'Log-in to the Console.')]"
    _privacy_link = "//a[contains(text(),'Privacy Policy')]"
    _redirect_privacy_page_heading = "//h1[contains(text(),'Privacy Policy')]"
    _terms_of_service_link = "//a[contains(text(),'Terms of Service')]"
    _redirect_terms_page_heading = "//h1[contains(text(),'Terms of Service')]"
    _sdk_license_agreement_link = "//a[contains(text(),'SDK License Agreement')]"
    _redirect_sdk_page_heading = "//h1[contains(text(),'SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT')]"
    _first_name_field = "//input[@id='registerForm.first_name']"
    _surname_field = "//input[@id='registerForm.surname']"
    _company_name_field = "//body/div[@id='sila-app']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[" \
                          "1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/input[1] "
    _select_company_name = "//a[@id='registerForm.company_name-item-0']"
    _work_email_field = "//input[@id='registerForm.email']"
    _work_phone_field = "//input[@id='registerForm.phone']"
    _password_field = "//input[@id='registerPasswordForm.password']"
    _confirm_password_field = "//input[@id='registerPasswordForm.confirmPassword']"
    _terms_checkbox = "//input[@name='privacy']"
    _create_account_button = "//button[contains(text(),'CREATE ACCOUNT')]"
    _email_icon = ".email .fas"
    _invalid_email = "//div[contains(text(),'Invalid email address')]"
    _phone_icon = ".phone:nth-child(4) .fas"
    _invalid_phone_validation = "//div[contains(text(),'Invalid phone number')]"
    _password_icon = ".password:nth-child(5) .fas"
    _confirm_password_icon = ".password:nth-child(6) .fas"
    _password_min_length_validation = "//div[contains(text(),'Minimum of 8 characters required.')]"
    _password_max_length_validation = "//div[contains(text(),'Provide a shorter password.')]"
    _password_mismatch_validation = "//div[contains(text(),'Re-enter your password confirmation so it matches ')]"
    _password_lookalike_email_validation = '''//div[contains(text(),"Password can't contain your username or email.")]'''
    _team_field_heading = "//h2[contains(text(),'Give your team a name.')]"
    _team_field_label = "//label[contains(text(),'Team Name')]"
    _add_team_name_field = "//input[@id='InviteTeamMembers.team_name']"
    _team_name_validation_icon = ".fas"
    _team_name_already_exists_validation = "//div[contains(text(),'Team name already exists.')]"
    _add_team_mates_box = "//textarea[@id='InviteTeamMembers.emails']"
    _send_invites_button = "//button[contains(text(),'Send Invites')]"
    _invitation_sent_message = "//div[@id='sila-app']/div/div/div/main/div/div/div/div/div/div/div[2]/div/form/div[3]/p"
    _continue_button = "//button[contains(text(),'Continue')]"
    _invite_your_team_and_collaborate_heading = "//h3[contains(text(),'Invite your team and collaborate.')]"
    _listing__text_1 = "//li[contains(text(),'Save time with faster onboarding')]"
    _listing__text_2 = "//li[contains(text(),'Stay up to date with the latest features')]"
    _listing_text_3 = "//li[contains(text(),'Organize communication with the Sila team')]"
    _add_team_box_placeholder_text = "//label[contains(text(),'Add teammates by email address and use commas to s')]"
    _welcome_screen_heading = '''//h1[contains(text(),"Welcome! Let's get started.")]'''

    # Selectors
    def getUrl(self):
        return self.driver.get(self.url)

    def getInvalidPhoneText(self):
        return self.get_text(self._invalid_phone_validation)

    def getMinPasswordValidationText(self):
        return self.get_text(self._password_min_length_validation)

    def getMaxPasswordValidationText(self):
        return self.get_text(self._password_max_length_validation)

    def getPasswordMisMatchValidationText(self):
        return self.get_text(self._password_mismatch_validation)

    def getPasswordLookAlikeEmailValidationText(self):
        return self.get_text(self._password_lookalike_email_validation)

    def getInvalidEmailText(self):
        return self.get_text(self._invalid_email)

    def getAlreadyHaveSilaAccountText(self):
        return self.get_text(self._already_have_a_sila_account_text)

    def getLoginPageHeading(self):
        self.wait_for_element(self._login_page_heading)
        return self.get_text(self._login_page_heading)

    def getTeamFieldHeading(self):
        self.wait_for_element(self._team_field_heading)
        return self.get_text(self._team_field_heading)

    # def getTeamFieldText(self):
    #     self.wait_for_element(self._add_team_name_field)
    #     self.element_click(self._add_team_name_field)
    #     return self.get_text(self._add_team_name_field)

    def getTeamNameValidationText(self):
        return self.get_text(self._team_name_already_exists_validation)

    def getTeamInvitationSentText(self):
        self.wait_for_element(self._invitation_sent_message)
        return self.get_text(self._invitation_sent_message)

    # Actions
    def clickSignUpLink(self):
        self.wait_for_element(self._sign_up_link)
        self.element_click(self._sign_up_link)

    def clickLoginLink(self):
        self.wait_for_element(self._login_link)
        self.element_click(self._login_link)

    def enterFirstName(self, firstName):
        self.wait_for_element(self._first_name_field)
        self.element_click(self._first_name_field)
        self.send_keys(firstName, self._first_name_field)
        self.log.info("Entered firstName: " + firstName)

    def enterSurName(self, surName):
        self.element_click(self._surname_field)
        self.send_keys(surName, self._surname_field)
        self.log.info("Entered lastName: " + surName)

    def enterCompanyName(self, companyName):
        self.element_click(self._company_name_field)
        self.send_keys(companyName, self._company_name_field)
        self.log.info("Entered companyName: " + companyName)
        time.sleep(1)
        self.selectCompanyName(Keys.ENTER)

    def selectCompanyName(self, pressEnter):
        self.send_keys(pressEnter, self._select_company_name)

    def enterWorkEmail(self, email):
        self.element_click(self._work_email_field)
        self.send_keys(email, self._work_email_field)
        self.log.info("Entered email: " + email)

    def enterWorkPhone(self, phone):
        self.element_click(self._work_phone_field)
        self.send_keys(phone, self._work_phone_field)
        self.log.info("Entered phone: " + phone)

    def enterPassword(self, password):
        self.element_click(self._password_field)
        self.send_keys(password, self._password_field)
        self.log.info("Entered password: " + password)
        self.web_scroll("down")

    def enterConfirmPassword(self, confirmPassword):
        self.element_click(self._confirm_password_field)
        self.send_keys(confirmPassword, self._confirm_password_field)
        self.log.info("Entered confirmPassword: " + confirmPassword)

    def clickTermsCheckbox(self):
        time.sleep(1)
        term_checkbox = self.get_element(self._terms_checkbox)
        hoverover = ActionChains(self.driver).move_to_element(term_checkbox).click().perform()
        self.log.info("Clicked on I agree checkbox")

    def clickConfirmAccountButton(self):
        self.element_click(self._create_account_button)
        self.log.info("Clicked on confirm account button")

    def clickEmailValidationIcon(self):
        self.wait_for_element(self._email_icon, 'css')
        self.element_click(self._email_icon, 'css')
        self.log.info("Clicked on email validation icon")

    def clickPasswordValidationIcon(self):
        self.wait_for_element(self._password_icon, 'css')
        self.element_click(self._password_icon, 'css')
        self.log.info("Clicked on password validation icon")

    def clickConfirmPasswordValidationIcon(self):
        self.wait_for_element(self._confirm_password_icon, 'css')
        self.element_click(self._password_icon, 'css')
        self.log.info("Clicked on confirm password validation icon")

    def clickPhoneValidationIcon(self):
        self.wait_for_element(self._phone_icon, 'css')
        self.element_click(self._phone_icon, 'css')
        self.log.info("Clicked on phone validation icon")

    def clickTeamName(self):
        self.wait_for_element(self._add_team_name_field)
        self.element_click(self._add_team_name_field)
        clear_field = Keys.CONTROL + "a" + Keys.DELETE
        self.send_keys(clear_field, self._add_team_name_field)

    def clickTeamNameValidationIcon(self):
        self.wait_for_element(self._team_name_validation_icon, 'css')
        self.element_click(self._team_name_validation_icon, 'css')

    def enterTeamMemberEmail(self, email):
        self.element_click(self._add_team_mates_box)
        clear_field = Keys.CONTROL + "a" + Keys.DELETE
        self.send_keys(clear_field, self._add_team_mates_box)
        time.sleep(0.5)
        self.send_keys(email, self._add_team_mates_box)

    def clickSendInviteButton(self):
        self.wait_for_element(self._send_invites_button)
        self.element_click(self._send_invites_button)

    def clickTeamPageContinueButton(self):
        self.element_click(self._continue_button)

    # Methods
    def signUpForm(self, firstName='', surName='', companyName='', email='', phone='',
                   password='', confirmPassword=''):
        self.enterFirstName(firstName)
        self.enterSurName(surName)
        if companyName == '':
            clear_field = Keys.CONTROL + "a" + Keys.DELETE
            self.send_keys(clear_field, self._company_name_field)
        else:
            self.enterCompanyName(companyName)
        self.enterWorkEmail(email)
        self.enterWorkPhone(phone)
        self.enterPassword(password)
        self.enterConfirmPassword(confirmPassword)

    def clearForm(self):
        self.web_scroll("up")
        clear_field = Keys.CONTROL + "a" + Keys.DELETE
        self.send_keys(clear_field, self._first_name_field)
        self.send_keys(clear_field, self._surname_field)
        self.send_keys(clear_field, self._company_name_field)
        self.send_keys(clear_field, self._work_email_field)
        self.send_keys(clear_field, self._work_phone_field)
        self.send_keys(clear_field, self._password_field)
        self.send_keys(clear_field, self._confirm_password_field)
        time.sleep(2)

    def addNewTeamName(self, teamName):
        self.clickTeamName()
        self.send_keys(teamName, self._add_team_name_field)
        time.sleep(5)

    def inviteTeamMember(self, email):
        self.enterTeamMemberEmail(email)
        self.clickSendInviteButton()
        self.clickTeamPageContinueButton()

    # Assertions
    def verifyPageTitle(self):
        time.sleep(10)
        title = self.get_title()
        self.verify_text_match(title, sign_up_page_title)
        self.log.info("User is on signup page")

    def verifyConfirmButtonDisable(self):
        self.web_scroll('down')
        self.check_element_state(self._create_account_button, element_name='create account button')

    def verifyPhoneValidationMessage(self):
        self.clickPhoneValidationIcon()
        phone_validation_text = self.getInvalidPhoneText()
        self.verify_text_match(phone_validation_text, invalid_phone_message)

    def verifyEmailValidationMessage(self, email_type=''):
        self.web_scroll('up')
        if email_type == "invalid":
            self.clickEmailValidationIcon()
            email_validation_text = self.getInvalidEmailText()
            self.verify_text_match(email_validation_text, invalid_email_address)
        else:
            self.clickEmailValidationIcon()
            email_validation_text = self.get_text(self._invalid_email)
            self.verify_text_match(email_validation_text, email_more_than_max_length)

    def verifyPasswordValidationMessage(self, val='mismatch'):
        if val == "min":
            self.clickPasswordValidationIcon()
            actual_validation_message = self.getMinPasswordValidationText()
            self.verify_text_match(actual_validation_message, password_less_than_min_length)
        elif val == 'max':
            self.clickPasswordValidationIcon()
            actual_validation_message = self.getMaxPasswordValidationText()
            self.verify_text_match(actual_validation_message, password_more_than_max_length)
        elif val == "same_as_email":
            self.clickPasswordValidationIcon()
            actual_validation_message = self.getPasswordLookAlikeEmailValidationText()
            self.verify_text_match(actual_validation_message, password_lookalike_message)
        else:
            self.clickConfirmPasswordValidationIcon()
            actual_validation_message = self.getPasswordMisMatchValidationText()
            self.verify_text_match(actual_validation_message, password_mismatch)

    def verifyLoginLink(self):
        self.clickLoginLink()
        heading = self.getLoginPageHeading()
        self.verify_text_match(heading, login_page_heading)
        self.clickSignUpLink()

    def verifyPrivacyPolicyLink(self):
        self.web_scroll('down')
        self.link_redirect(self._privacy_link, self._redirect_privacy_page_heading,
                           redirected_privacy_page_heading)

    def verifyTermsOfServiceLink(self):
        self.web_scroll('down')
        self.link_redirect(self._terms_of_service_link, self._redirect_terms_page_heading,
                           redirected_terms_page_heading)

    def verifySDKAgreementLink(self):
        self.web_scroll('down')
        self.link_redirect(self._sdk_license_agreement_link, self._redirect_sdk_page_heading,
                           redirected_sdk_agreement_page_heading)

    def verifyACHTransferApiLink(self):
        self.web_scroll('up')
        self.link_redirect(self._ach_transfer_link, self._redirect_ach_transfer_page_heading,
                           redirected_ach_page_heading)

    def verifyDigitalWalletApiLink(self):
        self.link_redirect(self._digital_wallet_api_link, self._redirect_digital_wallet_page_heading,
                           redirected_digital_wallet_api_page_heading)

    def verifyBankAccountLinkingApiLink(self):
        self.link_redirect(self._bank_account_linking_api_link, self._redirect_bank_account_linking_page_heading,
                           redirected_account_linking_page_heading)

    def verifyKYCIdentityVerificationLink(self):
        self.link_redirect(self._kyc_kyb_identity_verification_api_link,
                           self._redirect_kyb_kyc_verification_page_heading,
                           redirected_kyc_kyb_identity_verification_page_heading)

    def verifyAlreadyHaveSilaAccounText(self):
        self.web_scroll('down')
        actual_text = self.getAlreadyHaveSilaAccountText()
        self.verify_text_match(actual_text, already_have_a_sila_account)

    def verifyUserNavigatesToInviteTeamScreen(self):
        heading = self.getTeamFieldHeading()
        self.verify_text_match(heading, team_heading)

    # def verifyTeamNameFieldNotEmpty(self, name):
    #     team_name = self.getTeamFieldText()
    #     self.verify_text_match(team_name, name)

    def VerifyTeamNameAlreadyExists(self):
        self.clickTeamNameValidationIcon()
        text = self.getTeamNameValidationText()
        self.verify_text_match(text, team_name_already_exits)

    def verifyContinueButtonState(self, value=True):
        self.web_scroll('down')
        if value == False:
            self.check_element_state(self._continue_button, element_name="continue button on team invite screen")
        else:
            self.check_element_state(self._continue_button, value=True, element_name="continue button on team invite screen")

    def verifyInviteAlreadyRegisteredUserValidation(self, alreadyRegisteredUserEmail):
        self.enterTeamMemberEmail(alreadyRegisteredUserEmail)
        time.sleep(2)
        text = self.getTeamInvitationSentText()
        self.verify_text_contains(text, email_already_registered)

    def verifyInviteUserWithInvalidEmail(self, email):
        self.enterTeamMemberEmail(email)
        time.sleep(3)
        text = self.getTeamInvitationSentText()
        self.verify_text_contains(text, invalid_email_in_invite_team_member_box)

    def verifyTeamMemberInvitedSuccessfully(self, email):
        self.inviteTeamMember(email)
        time.sleep(3)
        text = self.getTeamInvitationSentText()
        self.verify_text_match(text, invitation_sent_successfully)

    def verifyConfirmEmail(self, emailPrefix):
        self.log.info("Email verification started")
        get_url = self.verify_email_confirmation(emailPrefix)
        get_url = self.driver.get(get_url)
        time.sleep(5)
        self.log.info(get_url)
        self.verify_text_match(get_url, "Sign Up | Sila API")
