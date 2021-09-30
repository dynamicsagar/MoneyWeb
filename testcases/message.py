from selenium.webdriver.common.keys import Keys

# keyboard keys
clear_field = Keys.CONTROL + "a" + Keys.DELETE

SIGN_UP_PAGE_TITLE = "Sign Up | Sila API"
LOGIN_PAGE_HEADING = "Log-in to the Console."
FORGOT_PASSWORD_PAGE_HEADING = "Forgot password?"
INVITE_TEAM_MEMBER_TITLE = "Sila Console - register::Invite Team Members"
QUESTIONNAIRE_PAGE_TITLE = "Sila Console - register::Questions"

INVALID_EMAIL_ADDRESS = "Invalid email address"
FIRST_NAME_MORE_THAN_MAX_LENGTH = "(entity.first_name) Ensure this field has no more than 100 characters."
LAST_NAME_MORE_THAN_MAX_LENGTH = "(entity.surname) Ensure this field has no more than 100 characters."
EMAIL_MORE_THAN_MAX_LENGTH = "Maximum of 254 characters."
PASSWORD_LESS_THAN_MIN_LENGTH = "Minimum of 8 characters required."
PASSWORD_MORE_THAN_MAX_LENGTH = "Provide a shorter password."
PASSWORD_MISMATCH_MESSAGE = "Re-enter your password confirmation so it matches your password."
PASSWORD_LOOKALIKE_MESSAGE = "Password can't contain your handle or email."
INVALID_PHONE_MESSAGE = "Invalid phone number"
TEAM_HEADING = "Give your team a name."
TEAM_NAME_ALREADY_EXITS = "Team name already exists."
ALREADY_HAVE_A_SILA_ACCOUNT = "Already have a Sila account? login"
INVITATION_SENT_SUCCESSFULLY = "Invites successfully sent!"
EMAIL_ALREADY_REGISTERED = "This email is already registered:"
INVALID_EMAIL_IN_INVITE_TEAM_MEMBER_BOX = "At least one or more email addresses are invalid."
INVALID_LOGIN = "Invalid login, please try again."
INVALID_PASSWORD_ATTEMPT = "Your account will be temporarily locked after 4 more unsuccessful login attempts."
WELCOME_SCREEN = "Welcome to the Sila Console"

# login
EMPTY_USER_NAME = "Username / Email Address is required"
USER_NAME_VALIDATION = "Can't use spaces or special characters and must be at least 3 characters."
EMPTY_PASSWORD_MESSAGE = "Password is required"

# logout
LOGOUT_POPUP_TEXT = 'Select "Logout" below if you are ready to end your current session.'
LOGOUT_POPUP_TITLE = "Ready to Leave?"

# forgot password
EMAIL_ADDRESS_REQUIRED_MESSAGE = "Email Address is required"

#  Heading after page redirect by clicking on links
REDIRECTED_PRIVACY_PAGE_HEADING = "Privacy Policy"
REDIRECTED_TERMS_PAGE_HEADING = "Terms of Service"
REDIRECTED_SDK_AGREEMENT_PAGE_HEADING = "SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT"
REDIRECTED_ACH_PAGE_HEADING = "Transfer money and initiate ACH transfers fast using the Sila API"
REDIRECTED_DIGITAL_WALLET_API_PAGE_HEADING = "Our Wallet API links any U.S. bank account via API for in-app payments."
REDIRECTED_ACCOUNT_LINKING_PAGE_HEADING = "Link bank accounts and transfer money fast using the Sila API"
REDIRECTED_KYC_KYB_IDENTITY_VERIFICATION_PAGE_HEADING = "Banking, Digital Wallet & ACH Payments API for Software Teams"

# Teams
TEAM_MODAL_BOX_TITLE = "Create new team"

# Application
APPLICATION_HEADING = "Application Detail"
NO_APP_YET_MESSAGE = "You do not have any apps yet."
STEP1_HEADING = "App Pending"
STEP1_SUB_HEADING = "Create an internal and public name for your app."
STEP1_DESCRIPTION = "The internal app name will be what you see within this console and is what Sila uses to identify" \
                    " your activity for support. The publicly facing app name will be used for services like Plaid" \
                    " and in other instances where the app name is shown to the end-user."
STEP2_HEADING = "Give your app a handle."
STEP3_HEADING = "Generate a public Ethereum address, or provide us with one below."
STEP3_DESCRIPTION = "A private key will also be generated for you. Download and store both of these keys in order to" \
                    " access your app. It’s very important that you store these keys in a safe place and do not" \
                    " lose them!"

