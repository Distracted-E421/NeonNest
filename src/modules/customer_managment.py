# customer_management.py

from database.db_operations import get_all_customers

def display_customers():
    customers = get_all_customers()
    for customer in customers:
        print(customer)  # Format as needed

# Add more customer-related functions
