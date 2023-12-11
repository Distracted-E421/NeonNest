from database.db_operations import *
from utils.input_validation import *
from utils.encryption_util import *

def process_orders():
    # Display the order processing options to the user
    print("Order Processing Options:")
    print("1. Update Order Status")
    print("2. Cancel Order")
    print("3. Retrieve Order Details")
    choice = input("Enter your choice: ")

    if choice == "1":
        update_order_status()
    elif choice == "2":
        cancel_order()
    elif choice == "3":
        retrieve_order_details()
    else:
        print("Invalid choice. Please try again.")

def update_order_status():
    # Update the status of an order in the database
    order_id = int(input("Enter order ID: "))
    new_status = input("Enter new status: ")
    if validate_integer_input(order_id):
        update_order_status_in_db(order_id, new_status)
        print("Order status updated")
    else:
        print("Invalid order ID")

def cancel_order():
    # Cancel an order in the database
    order_id = int(input("Enter order ID to cancel: "))
    if validate_integer_input(order_id):
        cancel_order_in_db(order_id)
        print("Order canceled")
    else:
        print("Invalid order ID")

def retrieve_order_details():
    # Retrieve and display the details of an order from the database
    order_id = int(input("Enter order ID: "))
    if validate_integer_input(order_id):
        order = get_order_details(order_id)
        if order:
            decrypted_details = decrypt_data(order['encryption_key'], order['details'])
            print("Order Details:", decrypted_details)
        else:
            print("Order not found")
    else:
        print("Invalid order ID")

def process_new_order():
    # Process a new order by encrypting the order details and storing them in the database
    order_details = input("Enter order details: ")
    encryption_key = generate_key()
    encrypted_details = encrypt_data(encryption_key, order_details.encode())
    create_order({
        "details": encrypted_details,
        "encryption_key": encryption_key
    })
    print("Order processed successfully")
