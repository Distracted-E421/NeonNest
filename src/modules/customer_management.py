
from database.db_operations import *
from utils.encryption_util import *

def add_new_customer():
    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")

    encryption_key = generate_key()
    encrypted_email = encrypt_data(encryption_key, email)
    encrypted_phone = encrypt_data(encryption_key, phone)

    customer_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": encrypted_email,
        "phone": encrypted_phone,
        "encryption_key": encryption_key  # Store this key securely with the customer record
    }
    add_customer(customer_data)
    print("Customer added successfully")

    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")

    if not (validate_string_input(first_name) and validate_string_input(last_name)
            and validate_email_format(email) and validate_phone_number_format(phone)):
        print("Invalid input")
        return

    customer_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }
    add_customer(customer_data)
    print("Customer added successfully")

def update_customer_info():
    email = input("Enter customer email to update: ")
    new_phone = input("Enter new customer phone number: ")

    if not (validate_email_format(email) and validate_phone_number_format(new_phone)):
        print("Invalid input")
        return

    update_customer(email, new_phone)
    print("Customer information updated successfully")

def search_customer_by_name():
    name = input("Enter customer name to search: ")
    if not validate_string_input(name):
        print("Invalid name input")
        return

    customers = get_customers(name)
    if customers:
        print("Found customers:")
        for customer in customers:
            print(f"{customer['first_name']} {customer['last_name']}, Email: {customer['email']}, Phone: {customer['phone']}")
    else:
        print("No customers found with the given name.")

def list_all_customers():
    customers = get_customers()
    if customers:
        print("All customers:")
        for customer in customers:
            print(f"{customer['first_name']} {customer['last_name']}, Email: {customer['email']}, Phone: {customer['phone']}")
    else:
        print("No customers found.")
