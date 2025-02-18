"""

Concerned with storing and retrieving data from a SQLite3 database.

"""
from .database_connection import DatabaseConnection


def create_book_table():
    """Create the books table in the SQLite3 Database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books ('
                       '    name text primary key, author text, read integer)')

def add_book(name, author):
    """Add a book the book database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES(?,?, 0)', (name, author))
        except Exception as e:  # Catch a generic exception
            if "UNIQUE constraint failed" in str(e):  # Check the error message
                print(f"{name} by {author} already exists in the database.")
            else:
                raise e  # Reraise the exception if it's not the one you expect


def get_all_books():
    """Return a list of all books using a dictionary and comprehension."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT name, author, read FROM Books')
        books = [{'name': row[0],'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_book_as_read(name):
    """Updates a book as read in the database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name):
    """Deletes a book from the database."""
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))
