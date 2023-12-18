from db_connection import *

# Function to retrieve all customers from the database
def get_all_customers():
    conn = create_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM customers")
        results = cursor.fetchall()
    return results

# Function to insert a new customer into the database
def insert_customer(customer):
    conn = create_connection()
    with conn.cursor() as cursor:
        query = "INSERT INTO customers (name, email) VALUES (%s, %s)"
        cursor.execute(query, (customer['name'], customer['email']))
        conn.commit()

# Function to update an existing customer in the database
def update_customer(customer):
    conn = create_connection()
    with conn.cursor() as cursor:
        query = "UPDATE customers SET name = %s, email = %s WHERE id = %s"
        cursor.execute(query, (customer['name'], customer['email'], customer['id']))
        conn.commit()

# Function to delete a customer from the database
def delete_customer(customer_id):
    conn = create_connection()
    with conn.cursor() as cursor:
        query = "DELETE FROM customers WHERE id = %s"
        cursor.execute(query, (customer_id,))
        conn.commit()

# Function to retrieve all products from the database
def get_all_products():
    conn = create_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        results = cursor.fetchall()
    return results

# Function to retrieve all sales from the database
def get_all_sales():
    conn = create_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sales")
        results = cursor.fetchall()
    return results
