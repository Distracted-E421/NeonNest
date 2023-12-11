# main.py

from modules.customer_management import display_customers

def main():
    while True:
        # Implement your menu system
        print("1. Display Customers")
        print("Q. Quit")
        choice = input("Enter choice: ")

        if choice == '1':
            display_customers()
        elif choice.upper() == 'Q':
            break

if __name__ == "__main__":
    main()
