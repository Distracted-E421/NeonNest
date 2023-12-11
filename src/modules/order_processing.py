from database.db_operations import *
from utils.input_validation import *

def process_order():
    order_id = int(input("Enter order ID: "))
    if not validate_integer_input(order_id):
        print("Invalid order ID")
        return

    print("1. Update Order Status")
    print("2. Cancel Order")
    print("3. Retrieve Order Details")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_status = input("Enter new status: ")
        update_order_status(order_id, new_status)
        print("Order status updated")

    elif choice == "2":
        cancel_order(order_id)
        print("Order canceled")

    elif choice == "3":
        order_details = get_order_details(order_id)
        print(order_details)

    else:
        print("Invalid choice")

def process_new_order():
    # Get order details
    order_details = input("Enter order details: ")

    encryption_key = generate_key()
    encrypted_order_details = encrypt_data(encryption_key, order_details)

    order_data = {
        "details": encrypted_order_details,
        "encryption_key": encryption_key  # Store this key securely with the order record
    }
    create_order(order_data)
    print("Order processed successfully")