import mysql.connector
from mysql.connector import errorcode
from db_config import DB_CONFIG

# Global variable for the database connection
connection = None

# Function to initialize the database connection
def initialize_connection():
    global connection
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("Database connection successfully established.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
        else:
            print(f"Error connecting to the database: {err}")

# Function to create a new database connection
def create_connection():
    return connection

# Function to close the database connection
def close_connection():
    global connection
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")

# Function to check if the database connection is active
def check_connection():
    global connection
    if connection and connection.is_connected():
        return True
    else:
        return False
