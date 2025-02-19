"""

Concerned with storing and retrieving data from a SQLite3 database.

"""
from typing import List, Dict
from .database_connection import DatabaseConnection


def create_book_table() -> None:
    """Creates the 'books' table in the database if it doesn't exist.
        The table contains columns for the book name (primary key), author,
        and whether the book has been read."""

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            name text primary key, 
                            author text, 
                            read integer)''')

def add_book(name: str, author: str) -> None:
    """Adds a new book to the database.

    Args:
        name: The name of the book.
        author: The author of the book.

    Raises:
        ValueError: If the book name or author is empty.
    """
    if not name or not author:
        raise ValueError("Book title and author cannot be empty.")

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES(?,?, 0)', (name, author))
        except Exception as err:
            if "UNIQUE constraint failed" in str(err):
                print(f"{name} by {author} already exists in the database.")
            else:
                raise err


def get_all_books() -> List[Dict[str, str]]:
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
