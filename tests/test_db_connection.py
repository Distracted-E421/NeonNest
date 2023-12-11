import unittest
from unittest.mock import patch
from database.db_connection import create_connection

class DBConnectionTests(unittest.TestCase):
    @patch('database.db_connection.mysql.connector.connect')
    def test_create_connection_successful(self, mock_connect):
        # Test if the connection is successfully created
        connection = create_connection()
        self.assertIsNotNone(connection)
        mock_connect.assert_called_once()

    @patch('database.db_connection.mysql.connector.connect', side_effect=mysql.connector.Error(errno=errorcode.ER_ACCESS_DENIED_ERROR))
    def test_create_connection_invalid_credentials(self, mock_connect):
        # Test if the function handles invalid credentials error
        connection = create_connection()
        self.assertIsNone(connection)
        mock_connect.assert_called_once()

    @patch('database.db_connection.mysql.connector.connect', side_effect=mysql.connector.Error(errno=errorcode.ER_BAD_DB_ERROR))
    def test_create_connection_database_not_found(self, mock_connect):
        # Test if the function handles database not found error
        connection = create_connection()
        self.assertIsNone(connection)
        mock_connect.assert_called_once()

    @patch('database.db_connection.mysql.connector.connect', side_effect=mysql.connector.Error)
    def test_create_connection_other_error(self, mock_connect):
        # Test if the function handles other errors
        connection = create_connection()
        self.assertIsNone(connection)
        mock_connect.assert_called_once()

if __name__ == '__main__':
    unittest.main()