from utilities.util import Util

# get unique name
utility = Util()
name = utility.get_unique_name(15)

# environments
dev_url = "https://devconsole.silamoney.com/login"
stage_url = "https://stageconsole.silamoney.com/login"
production_url = "https://console.silamoney.com/login"

# register form data
surname = "Role"
company_name = "ArcGate"
phone = "9874585855"
password = "Arcgate1!"
confirm_password = "Arcgate1!"


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
password_below_min_limit = "1234567"
password_above_max_limit = "Automation Testing of max characters limits for sila admin api. Automation Testing of max characters limits"
email_above_max_length = "fakedsadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadassadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadasssadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdgsadadasdasdasdasdasdasdsadasdasdasdasdasdasdasdasdasdasd@gmail.com"
mismatch_confirm_password = "Arcgate12!"
password_lookalike_email = user_email
invalid_email = "test@"
invalid_phone_num = "dadas"
invalid_user_name = "fdd@g"
invalid_password = "arcgate"

