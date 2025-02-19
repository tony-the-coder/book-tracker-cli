"""Define a class to manage the connection to the database."""
import sqlite3
import logging

class DatabaseConnection:
    """This class manages the connection to the database."""
    def __init__(self, host):
        """Initialise the class with a host (the database name)."""
        self.connection = None
        self.host = host

    def __enter__(self):
        """Open the connection to the database."""
        self.connection = sqlite3.connect(self.host)
        return self.connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connection to the database.
        exc_type: exception type
        exc_val: exception value
        exc_tb: exception traceback
        """
        if exc_type:
            # Log the full exception traceback
            logging.error("Exception occurred:", exc_info=(exc_type, exc_val, exc_tb))

            # More generic error message
            print("A database error occurred. Please try again.")
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()