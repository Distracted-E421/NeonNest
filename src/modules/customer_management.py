from ..database.db_operations import *
from ..utils.input_validation import *

def add_new_customer():
    customer_first_name = input("Enter customer first name: ")
    customer_last_name = input("Enter customer last name: ")
    customer_email = input("Enter customer email: ")
    customer_phone = input("Enter customer phone number: ")

    validate_input(customer_first_name, customer_last_name, customer_email, customer_phone)

    customer_data = create_customer_data(customer_first_name, customer_last_name, customer_email, customer_phone)
    save_customer(customer_data)
    print("Customer added successfully")

def update_customer_info():
    customer_email = input("Enter customer email: ")
    customer_phone = input("Enter customer phone number: ")

    validate_input(None, None, customer_email, customer_phone)

    customer_data = create_customer_data(None, None, customer_email, customer_phone)
    update_customer(customer_data)
    print("Customer information updated successfully")

def search_customer_by_name():
    customer_name = input("Enter customer name: ")
    customers = get_all_customers()

    found_customers = []
    for customer in customers:
        if customer['first_name'].lower() == customer_name.lower() or customer['last_name'].lower() == customer_name.lower():
            found_customers.append(customer)

    if len(found_customers) > 0:
        print("Found customers:")
        for customer in found_customers:
            print(f"Name: {customer['first_name']} {customer['last_name']}, Email: {customer['email']}, Phone: {customer['phone']}")
    else:
        print("No customers found with the given name.")

def list_all_customers():
    customers = get_all_customers()

    if len(customers) > 0:
        print("All customers:")
        for customer in customers:
            print(f"Name: {customer['first_name']} {customer['last_name']}, Email: {customer['email']}, Phone: {customer['phone']}")
    else:
        print("No customers found.")
