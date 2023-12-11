# main.py
from database.db_connection import *
from modules.customer_management import *
from modules.inventory_control import *
from modules.order_processing import *
from database.db_operations import *

def main_menu():
    print("Welcome to NeonNest!")
    print("Please select an option:")
    print("1. Manage Customers")
    print("2. Manage Inventory")
    print("3. Process Orders")
    print("4. View Products")
    print("5. View Sales Records")
    print("6. Create New Order")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manage_customers()
    elif choice == "2":
        manage_inventory()
    elif choice == "3":
        process_orders()
    elif choice == "4":
        products = get_all_products()
        for product in products:
            print(product)
    elif choice == "5":
        sales_records = get_all_sales()
        for record in sales_records:
            print(record)
    elif choice == "6":
        process_new_order()
    elif choice == "0":
        print("Exiting NeonNest. Goodbye!")
        close_connection()
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    try:
        initialize_connection()
        main_menu()
    except Exception as e:
        print("An error occurred:", str(e))
        close_connection()
