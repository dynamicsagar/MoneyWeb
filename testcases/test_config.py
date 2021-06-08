from utilities.util import Util

# Register user data
first_name = "Sila_Admin"
surname = "Automation"
company_name = "ArcGate"
phone = "9874585855"
password = "Arcgate1!"
confirm_password = "Arcgate1!"

# Register users email
utility = Util()
user = utility.get_unique_name(15)
# user_email = "silaqaautomation+" + user + "@gmail.com"
user_email = "testqa+" + user + "@mailinator.com"

# owner email
owner = utility.get_unique_name(15)
owner_email = "silaqaautomation+" + owner + "@gmail.com"

# manager email
manager = utility.get_unique_name(15)
manager_email = "silaqaautomation+" + manager + "@gmail.com"

# developer email
developer = utility.get_unique_name(15)
developer_email = "silaqaautomation+" + developer + "@gmail.com"

# contractor email
contractor = utility.get_unique_name(15)
contractor_email = "silaqaautomation+" + contractor + "@gmail.com"

# Create team name
team_name = "team_" + user

# Register invalid and mix and max data
password_below_min_limit = "1234567"
password_above_max_limit = "Automation Testing of max characters limits for sila admin api. Automation Testing of max characters limits"
email_above_max_length = "fakedsadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadassadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadasssadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdgsadadasdasdasdasdasdasdsadasdasdasdasdasdasdasdasdasdasd@gmail.com"
mismatch_confirm_password = "Arcgate12!"
password_lookalike_email = "silaqaautomation"
invalid_phone_num = "dadas"
