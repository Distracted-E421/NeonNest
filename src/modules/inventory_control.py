from database.db_operations import *

def manage_inventory():
    print("1. Add Inventory Item")
    print("2. Update Inventory Item")
    print("3. Delete Inventory Item")
    print("4. View Inventory List")
    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_inventory_item(item_name, quantity)
        print("Item added to inventory")

    elif choice == "2":
        item_id = int(input("Enter item ID to update: "))
        new_quantity = int(input("Enter new quantity: "))
        update_inventory(item_id, new_quantity)
        print("Inventory updated")

    elif choice == "3":
        item_id = int(input("Enter item ID to delete: "))
        delete_inventory_item(item_id)
        print("Item deleted from inventory")

    elif choice == "4":
        inventory = get_inventory()
        for item in inventory:
            print(f"Item ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}")

    else:
        print("Invalid choice")
