from utilities.util import Util

# get unique name
utility = Util()
name = utility.get_unique_name(15)

# environments
dev_url = "https://devconsole.silamoney.com/login"
stage_url = "https://stageconsole.silamoney.com/login"
production_url = "https://console.silamoney.com/login"

# register form data
FIRST_NAME = "Automation"
SURNAME = "User"
COMPANY_NAME = "ArcGate"
PHONE = "9874585855"
PASSWORD = "Arcgate1!"
CONFIRM_PASSWORD = "Arcgate1!"
RANDOM_EMAIL = name + "@mailiantor.com"

# admin user
admin_first_name = "Sila_Admin"
admin = admin_first_name + name
user_email = "silaqaautomation+" + admin + "@gmail.com"
# admin_email = "testqa+" + admin + "@mailinator.com"

# owner user
owner_first_name = "Owner"
owner = owner_first_name + name
owner_email = "silaqaautomation+" + owner + "@gmail.com"

# manager user
manager_first_name = "manager"
manager = manager_first_name + name
manager_email = "silaqaautomation+" + manager + "@gmail.com"

# developer user
developer_first_name = "developer"
developer = developer_first_name + name
developer_email = "silaqaautomation+" + developer + "@gmail.com"

# contractor user
contractor_first_name = "contractor"
contractor = contractor_first_name + name
contractor_email = "silaqaautomation+" + contractor + "@gmail.com"

# Create team name
team_name = "team_" + name

# register invalid and mix and max data
MORE_THAN_100_CHARACTERS = "testuserforsignuptestuserforsignuptestuserforsignuptestuserforsignuptestuserforsignuptestuserforsisss"
LESS_THAN_8_CHARACTERS = "1234567"
EMAIL_MORE_THAN_254_CHARACTERS = "fakedsadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadassadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadasssadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdgsadadasdasdasdasdasdasdsadasdasdasdasdasdasdasdasdasdasd@gmail.com"
MISMATCH_CONFIRM_PASSWORD = "Arcgate12!"
PASSWORD_LOOKALIKE_EMAIL = user_email
INVALID_EMAIL = "test@"
INVALID_PHONE_NUM = "dadas"
INVALID_USER_NAME = "fdd@g"
INVALID_PASSWORD = "arcgate"

