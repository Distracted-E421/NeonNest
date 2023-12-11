from database.db_operations import *
from utils.encryption_util import *
from utils.input_validation import *

# Function to add a new customer
def add_new_customer():
    # Prompt user for customer information
    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")

    # Validate input
    if not all([
        validate_string_input(first_name),
        validate_string_input(last_name),
        validate_email_format(email),
        validate_phone_number_format(phone)
    ]):
        print("Invalid input")
        return

    # Generate encryption key and encrypt customer email and phone number
    encryption_key = generate_key()
    encrypted_email = encrypt_data(encryption_key, email.encode())
    encrypted_phone = encrypt_data(encryption_key, phone.encode())

    # Create customer data dictionary
    customer_data = {
        "name": f"{first_name} {last_name}",
        "email": encrypted_email,
        "phone": encrypted_phone,
        "encryption_key": encryption_key
    }

    # Insert customer data into the database
    insert_customer(customer_data)
    print("Customer added successfully")

# Function to update customer information
def update_customer_info():
    # Prompt user for customer ID and new information
    customer_id = input("Enter customer ID for update: ")
    new_email = input("Enter new customer email: ")
    new_phone = input("Enter new customer phone number: ")

    # Validate input
    if not (validate_email_format(new_email) and validate_phone_number_format(new_phone)):
        print("Invalid input")
        return

    # Update customer information in the database
    update_customer({
        "id": customer_id,
        "email": new_email,
        "phone": new_phone
    })
    print("Customer information updated successfully")

# Function to list all customers
def list_all_customers():
    # Retrieve all customers from the database
    customers = get_all_customers()

    # Check if customers exist
    if customers:
        print("All customers:")
        # Iterate over each customer and print their decrypted information
        for customer in customers:
            decrypted_email = decrypt_data(customer['encryption_key'], customer['email'])
            decrypted_phone = decrypt_data(customer['encryption_key'], customer['phone'])
            print(f"Name: {customer['name']}, Email: {decrypted_email}, Phone: {decrypted_phone}")
    else:
        print("No customers found.")
