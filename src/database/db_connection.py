# db_connection.py

import mysql.connector
from mysql.connector import errorcode
from .db_config import DB_CONFIG

def create_connection():
    """
    Creates a connection to the database using the provided configuration.

    Returns:
        connection: A connection object if the connection is successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        error_messages = {
            errorcode.ER_ACCESS_DENIED_ERROR: "Invalid credentials",
            errorcode.ER_BAD_DB_ERROR: "Database not found"
        }
        print(error_messages.get(err.errno, err))
        return None
