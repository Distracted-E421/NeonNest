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
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
        else:
            print(err)
        return None
