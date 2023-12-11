import mysql.connector
from mysql.connector import errorcode
from .db_config import DB_CONFIG

def create_connection():
    # Create a connection to the database using the provided configuration
    connection = mysql.connector.connect(**DB_CONFIG)
    return connection

    try:
        # Attempt to establish a connection to the database
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        # Handle specific error cases
        error_messages = {
            errorcode.ER_ACCESS_DENIED_ERROR: "Invalid credentials",
            errorcode.ER_BAD_DB_ERROR: "Database not found"
        }
        # Print the error message corresponding to the error code
        print(error_messages.get(err.errno, err))
        return None
