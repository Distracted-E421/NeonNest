from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import mysql.connector

# AES encryption and decryption functions
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_data(data, key):
    iv = data[:AES.block_size]
    ciphertext = data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

# Connect to the MariaDB database
db = mysql.connector.connect(
    host="localhost",
    user="e421",
    password="1944",
    database="neon_nest_apt"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to view products
def view_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(product)

# Function to view customer details
def view_customers():
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    for customer in customers:
        customer_id, encrypted_name, encrypted_email = customer
        name = decrypt_data(encrypted_name, b'secretKey')
        email = decrypt_data(encrypted_email, b'secretKey')
        print(f"Customer ID: {customer_id}, Name: {name}, Email: {email}")

# Function to view sales records
def view_sales_records():
    cursor.execute("SELECT * FROM sales")
    sales_records = cursor.fetchall()
    for record in sales_records:
        print(record)

# Function to add new sales records
def add_sales_record():
    product_id = input("Enter product ID: ")
    customer_id = input("Enter customer ID: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    # Use parameterized query to prevent SQL injection
    query = "INSERT INTO sales (product_id, customer_id, quantity, price) VALUES (%s, %s, %s, %s)"
    values = (product_id, customer_id, quantity, price)
    cursor.execute(query, values)
    db.commit()
    print("Sales record added successfully!")

# Main menu
def main_menu():
    while True:
        print("1. View Products")
        print("2. View Customer Details")
        print("3. View Sales Records")
        print("4. Add New Sales Record")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_products()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            view_sales_records()
        elif choice == "4":
            add_sales_record()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main menu function
main_menu()

# Close the database connection
db.close()
