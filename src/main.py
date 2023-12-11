from database import db_connection
from modules import (
    db_operations,
    customer_management,
    inventory_control,
    order_processing,
    input_validation,
    encryption_util
)

def main_menu():
    print("Welcome to NeonNest!")
    print("Please select an option:")
    print("1. Manage Customers")
    print("2. Manage Inventory")
    print("3. Process Orders")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_management.manage_customers()
    elif choice == "2":
        inventory_control.manage_inventory()
    elif choice == "3":
        order_processing.process_orders()
    elif choice == "0":
        print("Exiting NeonNest. Goodbye!")
        db_connection.close_connection()
        return
    else:
        print("Invalid choice. Please try again.")

    main_menu()

if __name__ == "__main__":
    try:
        db_connection.initialize_connection()
        main_menu()
    except Exception as e:
        print("An error occurred:", str(e))
        db_connection.close_connection()