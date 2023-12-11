from .db_connection import *

def get_all_customers():
    # Retrieves all customers from the database.
    # Returns:
    #     A list of tuples representing the customers.

    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM customers"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def insert_customer(customer):
    # Inserts a new customer into the database.
    # Args:
    #     customer: A dictionary containing the customer's name and email.

    conn = create_connection()
    cursor = conn.cursor()
    query = "INSERT INTO customers (name, email) VALUES (?, ?)"
    cursor.execute(query, (customer['name'], customer['email']))
    conn.commit()
    cursor.close()
    conn.close()

def update_customer(customer):
    # Updates an existing customer in the database.
    # Args:
    #     customer: A dictionary containing the customer's name, email, and id.

    conn = create_connection()
    cursor = conn.cursor()
    query = "UPDATE customers SET name = ?, email = ? WHERE id = ?"
    cursor.execute(query, (customer['name'], customer['email'], customer['id']))
    conn.commit()
    cursor.close()
    conn.close()

def delete_customer(customer_id):
    # Deletes a customer from the database.
    # Args:
    #     customer_id: The id of the customer to be deleted.

    conn = create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM customers WHERE id = ?"
    cursor.execute(query, (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_products():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_all_sales():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM sales"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
