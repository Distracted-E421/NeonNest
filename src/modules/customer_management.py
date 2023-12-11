from ..database.db_operations import *
from ..utils.input_validation import *

def add_new_customer():
    # TODO: Implement add_new_customer function
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")
    customer_phone = input("Enter customer phone number: ")

    # Validate input
    if not validate_name(customer_name):
        print("Invalid customer name")
        return

    if not validate_email(customer_email):
        print("Invalid customer email")
        return

    if not validate_phone(customer_phone):
        print("Invalid customer phone number")
        return

    # Save customer information to database
    customer_data = {
        "name": customer_name,
        "email": customer_email,
        "phone": customer_phone
    }
    save_customer(customer_data)
    print("Customer added successfully")


def update_customer_info():
    # TODO: Implement update_customer_info function
    pass

def search_customer_by_name():
    # TODO: Implement search_customer_by_name function
    pass

def list_all_customers():
    # TODO: Implement list_all_customers function
    pass
