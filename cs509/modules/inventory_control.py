from database.db_operations import *

def manage_inventory():
    # Displaying the inventory management options
    print("Inventory Management Options:")
    print("1. Add Inventory Item")
    print("2. Update Inventory Item")
    print("3. Delete Inventory Item")
    print("4. View Inventory List")

    # Prompting the user for their choice
    choice = input("Enter your choice: ")

    # Handling the user's choice
    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        view_inventory()
    else:
        print("Invalid choice. Please try again.")

def add_item():
    # Prompting the user to enter item details
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    # Adding the item to the inventory
    add_inventory_item(item_name, quantity)
    print("Item added to inventory")

def update_item():
    # Prompting the user to enter item ID and new quantity
    item_id = int(input("Enter item ID to update: "))
    new_quantity = int(input("Enter new quantity: "))

    # Updating the inventory with the new quantity
    update_inventory(item_id, new_quantity)
    print("Inventory updated")

def delete_item():
    # Prompting the user to enter item ID to delete
    item_id = int(input("Enter item ID to delete: "))

    # Deleting the item from the inventory
    delete_inventory_item(item_id)
    print("Item deleted from inventory")

def view_inventory():
    # Retrieving the inventory list
    inventory = get_inventory()

    # Displaying the inventory list if it is not empty
    if inventory:
        print("Inventory List:")
        for item in inventory:
            print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}")
    else:
        print("No items found in inventory.")
