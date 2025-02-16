"""
Concerned with storing and retrieving data from a json file.
Format of the json file:
[
    {
        'name': 'Clean Code',
        'author': 'Robert C. Martin',
        'read': True
    }
]
"""

import json



books_file = 'books.json'

def create_book_table():
    """Create the books.txt file if it doesn't exist and is called
    from app.py."""
    with open(books_file, 'w') as file:
        json.dump([], file)



def add_book(name, author):
    """Add a book to the list of books."""
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    """Return all books in the books.txt file."""
    with open(books_file, 'r') as file:
        return json.load(file)

def _save_all_books(books):
    """The reason that there is an underscore before the function name is to indicate that
    this function is private and should not be called from outside this module."""
    try:
        with open(books_file, 'w') as file:
            json.dump(books, file, indent=4)
    except IOError as e:
        print(f"An error occurred while saving the books: {e}")


def mark_book_as_read(name):
    """Marks a book as read."""
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)





def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)




