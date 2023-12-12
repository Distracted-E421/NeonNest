import re

def validate_string_input(input_string):
    """Validates if the given input is a non-empty string."""
    return isinstance(input_string, str) and bool(input_string.strip())

def validate_email_format(email):
    """Validates if the given email matches the email format."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def validate_integer_input(input_integer):
    """Validates if the given input is an integer."""
    return isinstance(input_integer, int)

def validate_date_format(date):
    """Validates if the given date matches the YYYY-MM-DD format."""
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(date_regex, date) is not None

def validate_phone_number_format(phone):
    """Validates if the given phone number matches the XXX-XXX-XXXX format."""
    phone_regex = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(phone_regex, phone) is not None

def validate_first_name(first_name):
    """Validates if the first name is a non-empty string and starts with an uppercase letter."""
    return validate_string_input(first_name) and first_name[0].isupper() and first_name.isalpha()

def validate_last_name(last_name):
    """Validates if the last name is a non-empty string and consists only of alphabetic characters or hyphens."""
    return validate_string_input(last_name) and all(part.isalpha() for part in last_name.split('-'))
