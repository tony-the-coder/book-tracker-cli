"""Define a class to manage the connection to the database."""
import sqlite3

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
        """Close the connection to the database."""
        self.connection.commit()
        self.connection.close()
