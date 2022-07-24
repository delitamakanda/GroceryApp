from django.core.validators import RegexValidator

phone_message = 'Phone number must be entered in the format: 05999999999' 

# your desired format 
phone_regex = RegexValidator(regex=r'^(\d{2})\d{8}$', message=phone_message)
