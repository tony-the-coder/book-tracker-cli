"""

Concerned with storing and retrieving data from a SQLite3 database.

"""
import sqlite3


def create_book_table():
    """Create the books table in the SQLite3 Database."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books ('
                   '    name text primary key, author text, read integer)')
    connection.commit()
    connection.close()


def add_book(name, author):
    """Add a book the book database."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


def get_all_books():
    """Return a list of all books using a dictionary and comprehension."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT name, author, read FROM Books')
    books = [{'name': row[0],'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()
    return books


def mark_book_as_read(name):
    """Updates aa book as read in the database."""

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    connection.commit()
    connection.close()

def delete_book(name):
    """Deletes a book from the database."""
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()
