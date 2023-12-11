import re
def validate_string_input(input_string):
    if isinstance(input_string, str) and len(input_string) > 0:
        return True
    else:
        return False

def validate_email_format(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_regex, email):
        return True
    else:
        return False

def validate_integer_input(input_integer):
    if isinstance(input_integer, int):
        return True
    else:
        return False

def validate_date_format(date):
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_regex, date):
        return True
    else:
        return False
